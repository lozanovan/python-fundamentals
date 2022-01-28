from datetime import datetime
import websocket, json, statistics

#dictionary with prices list: key: minute; value: list of prices
price_list = {}

#dictionary with average prices: key: minute; value: average price per minute
avg_prices = {}
start_time=None
end_time=None

def sort_message(message):
    global start_time, end_time, avg_prices

    mydict=json.loads(message)['data']
    for data in mydict:

        ts=datetime.utcfromtimestamp(data['t']/1000.0).strftime('%Y-%m-%d %H:%M:%S')    

        print(data['s'], "|", "time:", ts, " price:" , data['p'], " volume:", data['v'])        
        print(" ")
        
        #calculate avg price per minute
        if(start_time is not None):
            if(data['t']/1000.0 < end_time and start_time in price_list):
                price_list[start_time].append(data['p'])

                buffer = round(statistics.mean(price_list[start_time]), 2)
                avg_prices[start_time]=buffer

            else:
                start_time=data['t']/1000.0
                end_time=data['t']/1000.0 + 60
                avg_prices[start_time]=[data['p']]

                buffer = round(statistics.mean(price_list[start_time]), 2)
                avg_prices[start_time]=buffer
        else:
            start_time=data['t']/1000.0
            end_time=data['t']/1000.0 + 60
            price_list[start_time]=[data['p']]

            buffer = round(statistics.mean(price_list[start_time]), 2)
            avg_prices[start_time]=buffer

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