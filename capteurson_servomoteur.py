from gpiozero import DistanceSensor
from time import sleep
import RPi.GPIO as GPIO
import time 

ultrason = DistanceSensor(23, 24)
ultrason1 = DistanceSensor (16, 20)
ultrason2 = DistanceSensor(18, 25)
ultrason3 = DistanceSensor (12, 21)

pin =17
pin2 = 21
pin3 = 22
pin4 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

p = GPIO.PWM(pin, 100)
p.start(1)

p2 = GPIO.PWM(pin2, 100)
p2.start(1)

p3 = GPIO.PWM(pin3, 100)
p3.start(1)

p4 = GPIO.PWM(pin4, 100)
p4.start(1)


while True:
	if ultrason.distance > 0.10:
		print (str(ultrason.distance) + "m")
		p.ChangeDutyCycle(18)
		time.sleep(0.8)
		
	elif ultrason.distance < 0.10:
		print (str(ultrason.distance )+ "m")
		p.ChangeDutyCycle(5)
		time.sleep(0.8)
		
	if ultrason1.distance > 0.10:
		print (str(ultrason.distance1) + "m")
		p2.ChangeDutyCycle(18)
		time.sleep(0.8) 
		
	elif ultrason1.distance < 0.10:
		print (str(ultrason.distance1 )+ "m")
		p2.ChangeDutyCycle(5)
		time.sleep(0.8)
		
	if ultrason2.distance > 0.10:
		print (str(ultrason.distance2 )+ "m")
		p3.ChangeDutyCycle (18)
		time.sleep(1)
		
	else:
		print (str(ultrason.distance2 )+ "m")
		p3.ChangeDutyCycle (5)
		time.sleep(1)
		
	if ultrason3.distance < 0.10:
		print (str(ultrason.distance3 )+ "m")
		p4.ChangeDutyCycle(18)
		time.sleep(0.8)
	else:
		print (str(ultrason.distance3 )+ "m")
		p4.ChangeDutyCycle(5)
		time.sleep(0.8)	
GPIO.cleanup()


