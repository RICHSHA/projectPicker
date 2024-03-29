import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    pulseStart = time.time()
    
while GPIO.input(ECHO) == 1:
    pulseEnd = time.time()
    
pulseDuration = pulseEnd - pulseStart

ditsance = pulseDuration * 17150
distance = round(distance, 2)

print("Distance: ", distance, "cm")

GPIO.cleanup()