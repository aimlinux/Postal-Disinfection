import time
import picamera
import io
import tornado
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
from threading import Thread

WIDTH = 480
HEIGHT = 360
FPS = 30
class HttpHandler(tornado.web.RequestHandler):
    def initialize(self):
            pass

    def get(self):
        self.render("./index.html")  #最初のHTTPアクセスを受け付け、WebSocket接続を確立させるスクリプトが入ったindex.htmlを返す

class WSHandler(tornado.websocket.WebSocketHandler):
    def initialize(self, camera):
        self.camera = camera
        self.state = True

    def open(self):
        print(self.request.remote_ip, ": connection opened")
        t = Thread(target=self.loop)    #撮影&送信スレッドの作成
        t.setDaemon(True)
        t.start()

    def loop(self):
        stream = io.BytesIO()

        for foo in self.camera.capture_continuous(stream, "jpeg"):
            stream.seek(0)
            self.write_message(stream.read(), binary=True)
            stream.seek(0)
            stream.truncate()
            if not self.state:
                break

    def on_close(self):
        self.state = False     #映像送信のループを終了させる
        self.close()     #WebSocketセッションを閉じる
        print(self.request.remote_ip, ": connection closed")

def piCamera():
    camera = picamera.PiCamera()
    camera.resolution = (WIDTH, HEIGHT)
    camera.framerate = FPS
    camera.start_preview()
    
    time.sleep(2)        #カメラ初期化
    return camera

def main():
    camera = piCamera()
    print("complete initialization")
    app = tornado.web.Application([
        (r"/", HttpHandler),                     #最初のアクセスを受け付けるHTTPハンドラ
        (r"/camera", WSHandler, dict(camera=camera)),   #WebSocket接続を待ち受けるハンドラ
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()