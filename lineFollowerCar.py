from gpiozero import Robot, LineSensor
from time import sleep
import time

robot = Robot(left=(23, 24), right=(22, 27))
left_sensor = LineSensor(26)
right_sensor= LineSensor(25)

speed   =  0.35 # 0.3 #0.24

def motor_speed():
    while True:
         left_detect  = int(left_sensor.value)
         right_detect = int(right_sensor.value)
        ## Stage 1
         if left_detect == 0 and right_detect == 0:
             left_mot = 1
             right_mot = 1
        ## Stage 2
         if left_detect == 0 and right_detect == 1:
             left_mot = -1
         if left_detect == 1 and right_detect == 0:
             right_mot = -1
        #print(r, l)
         yield (right_mot * speed, left_mot * speed)

robot.source = motor_speed()

sleep(60)
robot.stop()
robot.source = None
robot.close()
left_sensor.close()
right_sensor.close()

