#simple H-drive demo move code.

#!/usr/bin/env pybricks-micropython
import time
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

brick.sound.beep()


rightMotor = Motor(Port.A)
leftMotor = Motor(Port.D)
centerMotor = Motor(Port.B)

def movement(num1, num2,num3):
    leftMotor.run(num1)
    rightMotor.run(num2)
    centerMotor.run(num3)
while True:
    movement(500,480,0)
    time.sleep(1)
    movement(-500,-480,0)
    time.sleep(1)
    movement(0,0,700)
    time.sleep(1)
    movement(0,0,-700)
    time.sleep(1)
    movement(250,-250,700)
    time.sleep(2)
    movement(0,0,0)
    time.sleep(0.2)
    movement(-250,250,-700)
    time.sleep(2)
    break
