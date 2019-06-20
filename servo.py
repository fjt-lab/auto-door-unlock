# coding: utf-8
import RPi.GPIO as GPIO
import time

def servo_con(): 
    GPIO.setmode(GPIO.BCM)

    gp_out = 4 
    GPIO.setup(gp_out, GPIO.OUT)

    servo = GPIO.PWM(gp_out, 50) 
    servo.start(0.0)

    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    servo.ChangeDutyCycle(4.875)
    time.sleep(0.5)

    servo.ChangeDutyCycle(2.5)
    time.sleep(0.5)

    GPIO.cleanup()

if __name__ == "__main__":
    servo_con()
