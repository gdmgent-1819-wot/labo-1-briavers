#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep

from random import randint
#defining all the variables
sense = SenseHat()

#creating the colors
R = (255, 0, 0)
W = (255, 255, 255)
N= (0,0,0)
#creating dice heads
dice1 = [
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
    ]
dice2 = [
     N, N, N, N, N, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, R, R, N, N, N,
     N, N, N, N, N, N, N, N,
    ]
dice3 = [
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, R, R, N,
     N, N, N, N, N, R, R, N,
     N, N, N, R, R, N, N, N,
     N, N, N, R, R, N, N, N,
     N, R, R, N, N, N, N, N,
     N, R, R, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
    ]
dice4 = [
     N, N, N, N, N, N, N, N,
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
     N, N, N, N, N, N, N, N,
     N, N, N, N, N, N, N, N,
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
     N, N, N, N, N, N, N, N,
    ]

dice5 = [
     N, N, N, N, N, N, N, N,
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
     N, N, N, R, R, N, N, N,
     N, N, N, R, R, N, N, N,
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
     N, N, N, N, N, N, N, N,
    ]

dice6 = [
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
     N, N, N, N, N, N, N, N,
     N, R, N, N, N, R, R, N,
     N, R, N, N, N, R, R, N,
     N, N, N, N, N, N, N, N,
     N, R, R, N, N, R, R, N,
     N, R, R, N, N, R, R, N,
    ]

finished = True
free = True
timesPlayed = 0
score = 0


while free:
    acceleration = sense.get_accelerometer_raw()
    x= acceleration['x']
    y= acceleration['y']
    z= acceleration['z']
    
    x = abs(x)
    y = abs(y)
    z = abs(z)
    if x > 1 or y > 1 or z > 1:
            sense.clear()
            free = False
            sense.show_letter("?", R)
            sleep(1)
            
            amount = randint(1,6)
            sense.clear()
            print(amount)
            
            if amount == 1 :
                sense.set_pixels(dice1)
            elif amount == 2 :
                sense.set_pixels(dice2)
            elif amount == 3 :
                sense.set_pixels(dice3)
            elif amount == 4 :
                sense.set_pixels(dice4)
            elif amount == 5 :
                sense.set_pixels(dice5)
            elif amount == 6 :
                sense.set_pixels(dice6)
                
                #not working code
                
##            options  = {
##                    1: sense.set_pixels(dice1),
##                    2: sense.set_pixels(dice2),
##                    3: sense.set_pixels(dice3),
##                    4: sense.set_pixels(dice4),
##                    5: sense.set_pixels(dice5),
##                    6: sense.set_pixels(dice6)
##                    }
##            options[amount]()
            sleep(3)
            score += amount
            timesPlayed += 1
            print(timesPlayed)
            sense.clear()
            free = True
            if (timesPlayed == 3):
                free = False
                finished = True
                def showScore() : 
                    sense.show_message(str(score))
                showScore()
    

while finished:
    for event in sense.stick.get_events():
        free = True
        timesPlayed = 0
        score = 0
        finished = False  
        
                        
