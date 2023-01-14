from websocket_server import WebsocketServer

def sendMessage(client, server):
    server.send_message_to_all("Hello world! This is Raspberry Pi!")

def receivedMessage(client, server, message):
    print message
    server.send_message(client, "recived message: " + message)
    
server = WebsocketServer(5555, host="192.168.100.136")
server.set_fn_new_client(sendMessage)
server.set_fn_message_received(receivedMessage)
server.run_forever()