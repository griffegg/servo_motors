#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(18, 50)  # channel = 18, frequency = 50Hz

# duty cycle is Pulse Width divided by Period
# Period at 50Hz is 0.02 or 20 milliseconds, or 20000 microseconds
PERIOD = float(20000.0)
# to center the servo, a 1500 microsecond pulse is used
# therefore, duty cycle = 1500 / 20000 = 0.075 = 7.5 %
def calc_dc(pulse_in_us):
        return ((float(pulse_in_us) / PERIOD)*100.0)

pwm.start(calc_dc(500))

delay_period = 0.01

try:
    while True:
        for microseconds in range(50, 250):
            duty_cycle = calc_dc(microseconds*10)
            print('pulse1: '+str(microseconds*10)+' duty cycle: '+str(duty_cycle))
            pwm.ChangeDutyCycle(duty_cycle)
	    time.sleep(delay_period)

except KeyboardInterrupt:
    pwm.stop()
