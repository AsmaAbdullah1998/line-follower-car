from gpiozero import Robot, LineSensor
from time import sleep
import RPi.GPIO as GPIO
import time



robot = Robot(left=(23, 24), right=(22, 27))
left_sensor = LineSensor(26)
right_sensor= LineSensor(25)




while True:
             left_detect  = int(left_sensor.value)
             right_detect = int(right_sensor.value)
             ## Stage 1
             if left_detect == 0 and right_detect == 0:
                 robot.forward(0.4)  #0.2
             ## Stage 2
             if left_detect == 0 and right_detect == 1:
                 robot.right(0.7)  #0.7 or 0.5
             if left_detect == 1 and right_detect == 0:
                 robot.left(0.7)  #0.7 or 0.5

