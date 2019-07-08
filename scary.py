import pygame
from pygame.mixer import Sound
from gpiozero import MotionSensor
from time import sleep
import random

pygame.init()
pygame.mixer.init()
#play a wav file from the same foler as the script

sounds = [
        pygame.mixer.Sound("/home/pi/1.wav"),
        pygame.mixer.Sound("/home/pi/2.wav"),
        pygame.mixer.Sound("/home/pi/3.wav"),
        pygame.mixer.Sound("/home/pi/4.wav")
        ]

		#GPIO pin that the pir sensor is connected to
pir = MotionSensor(18)
while True:
    if pir.motion_detected:
        print("Motion detected")
        playSound = random.choice(sounds)
        playSound.play()
        # to make sure that the sound has fully played it waits 15 seconds, or make the wait longer to increase the spookyness!!
        sleep(15)
        playSound.stop()
    else:
        print ("No motion")