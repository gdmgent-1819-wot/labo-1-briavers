#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep
from random import randint
#defining all the variables
sense = SenseHat()
x = 0
y = 0

def sayIt():
    sense = SenseHat()
    x = 0
    y = 0
    while x < 8:
        while y < 8 :
            sense.set_pixel(x, y, (randint(0,255), randint(0,255), randint(0,255)))
            y+= 1
            sleep(0.1)
            sense.clear()
        x += 1
        y = 0
    sayIt()

sayIt()