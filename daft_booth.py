# Daft Booth v0.1
# Hacklab North Boynton

import pygame
import sys
import time
import RPi.GPIO as GPIO
from Adafruit_MCP230xx import Adafruit_MCP230XX

FULL_PATH = './'
ENABLE = 1

def main():
    setup()
    pygame.mixer.music.load(FULL_PATH + 'sounds/hbfs/beat_hbfs.mp3')
    work_it_A = load_sound(FULL_PATH + 'sounds/hbfs/101_work_it.wav')
    harder_A = load_sound(FULL_PATH + 'sounds/hbfs/102_harder.wav')
    make_it_A = load_sound(FULL_PATH + 'sounds/hbfs/103_make_it.wav')
    better_A = load_sound(FULL_PATH + 'sounds/hbfs/104_better.wav')
    do_it_A = load_sound(FULL_PATH + 'sounds/hbfs/105_do_it.wav')
    faster_A = load_sound(FULL_PATH + 'sounds/hbfs/106_faster.wav')
    makes_us_A = load_sound(FULL_PATH + 'sounds/hbfs/107_makes_us.wav')
    stronger_A = load_sound(FULL_PATH + 'sounds/hbfs/108_stronger.wav')

    pygame.mixer.music.play(-1)
    soundboard = setup_soundboard_bus()

    print('Running...')
    try:
        while True:
            if (soundboard.input(0) == 0):
                work_it_A.play()
    except KeyboardInterrupt:
        cleanup()
        exit(1)

def load_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(1.0)
    return sound

def setup():
    pygame.mixer.init()
    pygame.init()

    # Just need screen for development, in order to easily get keyboard events.
    screen = pygame.display.set_mode([300, 100])
    screen.fill([255, 255, 255])
    return screen

def setup_soundboard_bus():
    soundboard = Adafruit_MCP230XX(address=0x21, num_gpios=16)
    soundboard.pullup(0, ENABLE)
    return soundboard
    
def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    main()
