import RPi.GPIO as GPIO
import time
import json

GPIO.setmode(GPIO.BOARD)

REED_gas = 21
GPIO.setup(REED_gas, GPIO.IN, pull_up_down=GPIO.PUD_UP)

with open("gas_readings.txt", "a") as gas_readings:
    gas_readings.write("# Started at {:.3f}\n".format(time.time()))

contact_status_previous = 1
while True:
    contact_status_current = GPIO.input(REED_gas)
    if contact_status_current == 0 and contact_status_previous == 1:
        print "Trigger"
        with open("gas_readings.txt", "a") as gas_readings:
          gas_readings.write("{:.1f}\n".format(time.time()))
    contact_status_previous = contact_status_current
    time.sleep(1)

