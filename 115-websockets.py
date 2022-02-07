from datetime import datetime
import websocket, json, statistics

#buffer dictionary with prices list: key: start minute; value: list of prices
price_list = {}
#sum of the price volumes product for each entity per interval
price_volume_sum = 0.0
volume_sum = 0.0
vwap = 0.0

start_time=None
end_time=None


def sort_message(message):
    global start_time, end_time, price_list, price_volume_sum, volume_sum, vwap
    
    mydict=json.loads(message)['data']
    for data in mydict:

        ts=datetime.utcfromtimestamp(data['t']/1000.0).strftime('%Y-%m-%d %H:%M:%S')    

        print(data['s'], "|", "time:", ts, " price:" , data['p'], " volume:", data['v'])        
        print(" ")
        
        #calculate avg price per interval
        if(start_time is not None):
            if(data['t']/1000.0 < end_time and start_time in price_list):
                
                price_list[start_time].append(data['p'])
                price_volume_sum = price_volume_sum + (data['v'] * data['p'])
                volume_sum = volume_sum + data['v']                        
            else:
                #buffers are being restarted for the next interval
                start_time=data['t']/1000.0
                end_time=data['t']/1000.0 + 60

                #when we go above the time limit, we print the vwap
                vwap = round(price_volume_sum/volume_sum, 2)
                print('VWAP for the past minute is: ', vwap)

                price_list.clear()
                price_list[start_time]=[data['p']]
                price_volume_sum=0.0
                volume_sum=0.0
        else:
            start_time=data['t']/1000.0
            end_time=data['t']/1000.0 + 60
            price_list[start_time]=[data['p']]
            price_volume_sum = price_volume_sum + (data['v'] * data['p'])
            volume_sum = volume_sum + data['v']
            

def on_message(ws, message):
    sort_message(message)

def on_error(ws, error):
    print(error, 'k')

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print('Succesfully opened a connection!')
    ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')

websocket.enableTrace(True)
ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=c7l8mfiad3i9ji44i6u0",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close,
                            on_open = on_open)
ws.run_forever()