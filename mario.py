#importing the sensehat, the sleep function and a random generater
from sense_hat import SenseHat
from time import sleep


#defining all the variables
sense = SenseHat()

#fixing dsplay because short cables
sense.set_rotation(180)

#creating the colors
R = (255, 0, 0)
W = (255, 255, 255)
Z= (0,0,0)
S = (245, 222, 179)
B = (50, 50, 255)
E = (139, 69, 19)

#creating mario
mario_pixels = [
     Z, Z, R, R, R, Z, Z, Z,
     Z, R, R, R, R, R, R, Z,
     Z, E, E, S, S, S, Z, Z,
     E, E, S, S, Z, S, Z, Z,
     Z, E, S, S, S, S, Z, Z,
     Z, Z, Z, B, B, B, Z, Z,
     Z, Z, B, B, Z, B, B, Z,
     Z, Z, B, B, Z, B, B, Z,
    ]

#creating mario JUMP
mario_pixels_jump = [
     Z, E, E, S, S, S, Z, Z,
     E, E, S, S, Z, S, Z, Z,
     Z, E, S, S, S, S, Z, Z,
     Z, Z, Z, B, B, B, Z, Z,
     Z, Z, B, B, Z, B, B, Z,
     Z, Z, B, B, Z, B, B, Z,
     Z, Z, Z, Z, Z, Z, Z, Z,
     Z, Z, Z, Z, Z, Z, Z, Z, 
    ]
     
     
sense.set_pixels(mario_pixels)


while True:
    for event in sense.stick.get_events():
        sense.set_pixels(mario_pixels_jump)
        sleep(0.2)       
        sense.set_pixels(mario_pixels)


        
