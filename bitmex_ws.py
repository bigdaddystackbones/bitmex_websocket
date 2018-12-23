import json
from websocket import create_connection


#-----------------------------------------------------------------------------------------------

#create websocket connection

BITMEX_URL = "wss://www.bitmex.com"

VERB = "GET"
ENDPOINT = "/realtime"


def bitmex_websocket():

    ws = create_connection(BITMEX_URL + ENDPOINT)
    print("Receiving Welcome Message...")
    result = ws.recv()
    print("Received '%s'" % result)
    
    #add here the channels you like to subscribe to
    request = {"op": "subscribe", "args": ["orderBook10:XRPZ18", "orderBook10:LTCZ18"]}
    ws.send(json.dumps(request))
    print("Sent subscribe")

    result = ws.recv()
    print("Received '%s'" % result)

    result = ws.recv()
    msg = json.loads(result)
    
    #keeps websocket alive
    while True:
        msg = ws.recv()
        print(msg)
    
#---------------------------------------------------------------------------------

#calls websocket function
bitmex_websocket()

#---------------------------------------------------------------------------------


