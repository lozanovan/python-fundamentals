import websocket, sys, json
from datetime import datetime

def sort_message(message):
    mydict=json.loads(message)['data']
    for data in mydict:

        ts=datetime.utcfromtimestamp(data['t']/1000.0).strftime('%Y-%m-%d %H:%M:%S')        
        print(data['s'], "|", "time:", ts, " price:" , data['p'], " volume:", data['v'])        
        print(" ")  

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