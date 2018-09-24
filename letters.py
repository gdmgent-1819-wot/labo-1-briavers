#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep
from random import randint

#defining all the variables
sense = SenseHat()
sleepTime = 0.5
waitTime = 1

#creating a function to display the letter
def sayIt(string):
    for x in string:
        #show the letter
        sense.show_letter(x, (randint(0,255), randint(0,255), randint(0,255)))
        #sleep for a specified amount of time
        sleep(sleepTime)
        #clear the display
        sense.clear()
    #calling the repetitive function
    sayIt(string)
#initialzzing the function
sayIt("COOCKIES")
