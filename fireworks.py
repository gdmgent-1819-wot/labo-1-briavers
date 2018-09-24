##needs a smal time to startup and make sure every pixel is working

#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep
from random import randint
import threading
#import a random float generater
import random
#defining all the variables
sense = SenseHat()

#create a threads array
threads=[]

#the function that every thread runs
def runner(x, y):
    #activate a set pixel in a random collar 
    sense.set_pixel(x, y, (randint(0,255), randint(0,255), randint(0,255)))
    #let the pixel keep burning
    sleep(random.random())
    #deactivate the pixel
    sense.set_pixel(x, y, 0, 0, 0)
    #keep it of for a random time between 0 and 1 sec
    sleep(random.random())
    #restart the thread 
    runner(x, y)
   
#create a thread for every LED
for x in range(8):
    for y in range(8):
        #create the thread 
        t = threading.Thread(target=runner, args=(x,y))
        #add the thread to the array
        threads.append(t)
        #start the tread
        t.start()
        
    
