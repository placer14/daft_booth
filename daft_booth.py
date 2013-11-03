# Daft Booth v0.1
# Hacklab North Boynton

import pygame
import sys
import time

FULL_PATH = './'


def main():
    print('Running...')
    pygame.mixer.init()
    pygame.init()
    
    pygame.mixer.music.load(FULL_PATH + 'sounds/beat.mp3')
    button_sound = []
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/CallIt.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/After1.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/Better1.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/BurnIt.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/ChangeIt.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/CodeIt.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/CrackIt.wav'))
    button_sound.append(pygame.mixer.Sound(FULL_PATH + 'sounds/CutIt.wav'))
    
    pygame.mixer.music.play(-1)
    
    # Just need screen for development, in order to easily get keyboard events.
    screen = pygame.display.set_mode([300, 100])
    screen.fill([255, 255, 255])

    while True:

        # See commented out code below to get events from inputs.        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                print('Quiting')
                pygame.quit()
                sys.exit()
                
                break
            elif event.type == pygame.KEYDOWN:
                print('KeyPressed')
                if (event.key == pygame.K_1):
                    button_sound[0].play()
                elif (event.key == pygame.K_2):
                    button_sound[1].play()
                elif (event.key == pygame.K_3):
                    button_sound[2].play()
                elif (event.key == pygame.K_4):
                    button_sound[3].play()
                elif (event.key == pygame.K_5):
                    button_sound[4].play()
                elif (event.key == pygame.K_6):
                    button_sound[5].play()
                elif (event.key == pygame.K_7):
                    button_sound[6].play()
                elif (event.key == pygame.K_8):
                    button_sound[7].play()
                    
        
if __name__ == '__main__':
    main()
    
    
    
#mport pygame.mixer
#from time import sleep
#import RPi.GPIO as GPIO
#from sys import exit
#
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(23, GPIO.IN)
#GPIO.setup(24, GPIO.IN)
#GPIO.setup(25, GPIO.IN)
#
#pygame.mixer.init(48000, -16, 1, 1024)
#
#sndA = pygame.mixer.Sound("buzzer.wav")
#sndB = pygame.mixer.Sound("clap.wav")
#sndC = pygame.mixer.Sound("laugh.wav")
#
#soundChannelA = pygame.mixer.Channel(1)
#soundChannelB = pygame.mixer.Channel(2)
#soundChannelC = pygame.mixer.Channel(3)
#
#print "Sampler Ready."
#
#while True:
#   try:
#      if (GPIO.input(23) == True):
#         soundChannelA.play(sndA)
#      if (GPIO.input(24) == True):
#         soundChannelB.play(sndB)
#      if (GPIO.input(25) == True):
#         soundChannelC.play(sndC)
#      sleep(.01)
#   except KeyboardInterrupt:
#     exit()
 
