#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep
from random import randint

#defining all the variables
size = 8
speed = 1
color = (50, 0, 255)
sense = SenseHat()

def haveFun():
    sense.clear()
    for x in range(size//2):
        for y in range(size):
            if randint(0,1):
                sense.set_pixel(x, y, color)
                sense.set_pixel(((size-1)-x), y, color)
    sleep(speed)
    haveFun()
haveFun()
            
