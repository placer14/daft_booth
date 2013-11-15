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
            if (soundboard.input(1) == 0):
                harder_A.play()
            if (soundboard.input(2) == 0):
                make_it_A.play()
            if (soundboard.input(3) == 0):
                better_A.play()
            if (soundboard.input(4) == 0):
                do_it_A.play()
            if (soundboard.input(5) == 0):
                faster_A.play()
            if (soundboard.input(6) == 0):
                makes_us_A.play()
            if (soundboard.input(7) == 0):
                stronger_A.play()
            if (soundboard.input(8) == 0):
                work_it_A.play()
            if (soundboard.input(9) == 0):
                work_it_A.play()
            if (soundboard.input(10) == 0):
                work_it_A.play()
            if (soundboard.input(11) == 0):
                work_it_A.play()
            if (soundboard.input(12) == 0):
                work_it_A.play()
            if (soundboard.input(13) == 0):
                work_it_A.play()
            if (soundboard.input(14) == 0):
                work_it_A.play()
            if (soundboard.input(15) == 0):
                work_it_A.play()
    except KeyboardInterrupt:
        cleanup()
        exit(1)

def load_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(0.4)
    return sound

def setup():
    pygame.mixer.init(buffer=2048)
    pygame.init()

    # Just need screen for development, in order to easily get keyboard events.
    screen = pygame.display.set_mode([300, 100])
    screen.fill([255, 255, 255])
    return screen

def setup_soundboard_bus():
    soundboard = Adafruit_MCP230XX(address=0x21, num_gpios=16)
    soundboard.pullup(0, ENABLE)
    soundboard.pullup(1, ENABLE)
    soundboard.pullup(2, ENABLE)
    soundboard.pullup(3, ENABLE)
    soundboard.pullup(4, ENABLE)
    soundboard.pullup(5, ENABLE)
    soundboard.pullup(6, ENABLE)
    soundboard.pullup(7, ENABLE)
    soundboard.pullup(8, ENABLE)
    soundboard.pullup(9, ENABLE)
    soundboard.pullup(10, ENABLE)
    soundboard.pullup(11, ENABLE)
    soundboard.pullup(12, ENABLE)
    soundboard.pullup(13, ENABLE)
    soundboard.pullup(14, ENABLE)
    soundboard.pullup(15, ENABLE)
    return soundboard
    
def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    main()
