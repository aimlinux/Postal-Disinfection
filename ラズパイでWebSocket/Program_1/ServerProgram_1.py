#ラズパイからWebSocketでブラウザへ「Hello world! This is Raspberry Pi!」を送信するプログラム


#-----websocket-severのインストール後-----

from websocket_server import WebsocketServer

def sendMessage(client, server):
    server.send_message_to_all("Hello world! This is Raspberry Pi!")

server = WebsocketServer(5555, host="127.0.0.1")
server.set_fn_new_client(sendMessage)
server.run_forever()



#-----hostにはラズパイのIPアドレスを設定する。-----
#-----IPアドレスを調べるには、$ ifconfig を実行して -----
#-----wlan0 の inet に書かれている。-----
