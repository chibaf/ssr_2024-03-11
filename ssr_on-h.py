import RPi.GPIO as GPIO
from time import sleep
import time

ssr_pin =12 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ssr_pin,GPIO.OUT)

pwm_totaltime=10.0
pwm_width=1.0
on_time=10.0 #pwm_totaltime*pwm_width
off_time=10.0 #pwm_totaltime*(1-pwm_width)
while True:  
  GPIO.output(ssr_pin, True)
  time.sleep(on_time)
  GPIO.output(ssr_pin, False)
  time.sleep(off_time)
