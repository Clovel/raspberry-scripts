import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    print GPIO.input(17)
    if (False == GPIO.input(17)):
        os.system("sudo shutdown -h now")
        break;

    time.sleep(1)

