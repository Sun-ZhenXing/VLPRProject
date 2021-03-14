from gpiozero import Buzzer
from time import sleep
import cv2

def buzzer_run(pin, t):
    '''
    pin 针脚输出(有源)蜂鸣器信号，持续 t 秒
    '''
    buzzer = Buzzer(pin)
    buzzer.on()
    sleep(t)
    buzzer.off()

def get_pic():
    video_capture = cv2.VideoCapture(0)
    process_this_frame = True
    