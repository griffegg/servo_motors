#!/usr/bin/python

from Tkinter import *
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

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        scale = Scale(frame, from_=500, to=2500,
              orient=HORIZONTAL, command=self.update)
        scale.grid(row=0)


    def update(self, microseconds):
        duty = calc_dc(microseconds)
        pwm.ChangeDutyCycle(duty)

root = Tk()
root.wm_title('Servo Control')
app = App(root)
root.geometry("800x200+0+0")
root.mainloop()
