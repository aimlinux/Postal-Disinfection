#coding:utf-8
import pygame.mixer
import time

def sound(f,i,n):
    pygame.mixer.init() #初期化します
    pygame.mixer.music.load(f) #音声ファイルを読み込みます
    pygame.mixer.music.play(i) #再生します
    time.sleep(n) #再生時間を指定します
    pygame.mixer.music.stop() #終了します

sound("音声再生\sample_cound.mp3",2,3)