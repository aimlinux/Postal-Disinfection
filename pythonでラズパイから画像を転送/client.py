#-*- coding:utf-8 -*-

from websocket import create_connection
import sys
import base64
from io import BytesIO 
import cv2
import numpy as np

ws = create_connection("ws://172.27.2.111:8080/camera")


# decode
while True:
    arr = np.asarray(bytearray(ws.recv()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)  # 'load it as it is'
    cv2.imshow('image', img)
    cv2.waitKey(10)
cv2.destroyAllWindows()

ws.close()
