import cv2
import datetime

dt_now = datetime.datetime.now()
file_name = dt_now.strftime('%Y年%m月%d日%H時%M分%S秒')

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite(file_name + '.jpg', frame)
cap.release()