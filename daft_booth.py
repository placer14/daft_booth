# Daft Booth v0.1
# Hacklab North Boynton

import pygame
import sys
import time
import RPi.GPIO as GPIO
from Adafruit_MCP230xx import Adafruit_MCP230XX

FULL_PATH = './'
ENABLE = 1
ALT_SOUND_TOGGLE = False
HALT_FURTHER_TOGGLE = False
SOUNDBOARD_ADDR = 0x20
CONTROL_ADDR = 0x21

def main():
    pygame.mixer.music.load(FULL_PATH + 'sounds/hbfs/beat_hbfs.mp3')

    pygame.mixer.music.play(-1)
    soundboard = setup_soundboard_bus()
    control = setup_control_bus()

    print('Running...')
    try:
        while True:
            pin_0 = soundboard.input(0)
            pin_1 = soundboard.input(1)
            pin_2 = soundboard.input(2)
            pin_3 = soundboard.input(3)
            pin_4 = soundboard.input(4)
            pin_5 = soundboard.input(5)
            pin_6 = soundboard.input(6)
            pin_7 = soundboard.input(7)
            pin_8 = soundboard.input(8)
            pin_9 = soundboard.input(9)
            pin_10 = soundboard.input(10)
            pin_11 = soundboard.input(11)
            pin_12 = soundboard.input(12)
            pin_13 = soundboard.input(13)
            pin_14 = soundboard.input(14)
            pin_15 = soundboard.input(15)
            if (pin_0 == 0):
                work_it().play()
            if (pin_1 == 0):
                harder().play()
            if (pin_2 == 0):
                make_it().play()
            if (pin_3 == 0):
                better().play()
            if (pin_4 == 0):
                do_it().play()
            if (pin_5 == 0):
                faster().play()
            if (pin_6 == 0):
                makes_us().play()
            if (pin_7 == 0):
                stronger().play()
            if (pin_8 == 0):
                more_than().play()
            if (pin_9 == 0):
                ever().play()
            if (pin_10 == 0):
                hour().play()
            if (pin_11 == 0):
                after().play()
            if (pin_12 == 0):
                our().play()
            if (pin_13 == 0):
                work_is().play()
            if (pin_14 == 0):
                never().play()
            if (pin_15 == 0):
                over().play()
            pin_16 = check_toggle_sounds(control)
            pin_17 = check_toggle_background_track(control)
            print("%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (pin_0, pin_1, pin_2, pin_3, pin_4, pin_5, pin_6, pin_7, pin_8, pin_9, pin_10, pin_11, pin_12, pin_13, pin_14, pin_15, pin_16, pin_17))
    except KeyboardInterrupt:
        cleanup()
        exit(1)

def check_toggle_sounds(control):
    global HALT_FURTHER_TOGGLE
    pin_16 = control.input(0)
    if (pin_16 == 0):
        toggle_alt_sounds()
    else:
        HALT_FURTHER_TOGGLE = False
    return pin_16

def toggle_alt_sounds():
    global ALT_SOUND_TOGGLE
    global HALT_FURTHER_TOGGLE
    if HALT_FURTHER_TOGGLE == False:
        ALT_SOUND_TOGGLE = False if (ALT_SOUND_TOGGLE == True) else True
        HALT_FURTHER_TOGGLE = True
        print("Sound toggle is %s" % ALT_SOUND_TOGGLE)
    return ALT_SOUND_TOGGLE

def check_toggle_background_track(control):
    global HALT_FURTHER_PAUSE_PLAY
    pin_17 = control.input(1)
    if (pin_17 == 0):
        toggle_background_track()
    else:
        HALT_FURTHER_PAUSE_PLAY = False
    return pin_17

def toggle_background_track():
    global HALT_FURTHER_PAUSE_PLAY
    if (HALT_FURTHER_PAUSE_PLAY == False):
        if (pygame.mixer.music.get_busy() == 1):
            pygame.mixer.music.stop()
            HALT_FURTHER_PAUSE_PLAY = True
            print("BG track is stopped")
        else:
            pygame.mixer.music.play(-1)
            HALT_FURTHER_PAUSE_PLAY = True
            print("BG track is started")

def work_it():
    return get_sound(work_it_A, work_it_B)

def harder():
    return get_sound(harder_A, harder_B)

def make_it():
    return get_sound(make_it_A, make_it_B)

def better():
    return get_sound(better_A, better_B)

def do_it():
    return get_sound(do_it_A, do_it_B)

def faster():
    return get_sound(faster_A, faster_B)

def makes_us():
    return get_sound(makes_us_A, makes_us_B)

def stronger():
    return get_sound(stronger_A, stronger_B)

def more_than():
    return get_sound(more_than_A, more_than_B)

def ever():
    return get_sound(ever_A, ever_B)

def hour():
    return get_sound(hour_A, hour_B)

def after():
    return get_sound(after_A, after_B)

def our():
    return get_sound(our_A, our_B)

def work_is():
    return get_sound(work_is_A, work_is_B)

def never():
    return get_sound(never_A, never_B)

def over():
    return get_sound(over_A, over_B)

def get_sound(sound_A, sound_B):
    if (is_alt_sound_toggled() == False):
        return sound_A
    else:
        return sound_B

def is_alt_sound_toggled():
    return ALT_SOUND_TOGGLE

def load_sound(file):
    sound = pygame.mixer.Sound(file)
    sound.set_volume(0.4)
    return sound

def setup():
    pygame.mixer.init(buffer=2048)
    pygame.init()
    return True

    # Just need screen for development, in order to easily get keyboard events.
    # screen = pygame.display.set_mode([300, 100])
    # screen.fill([255, 255, 255])
    # return screen

def setup_soundboard_bus():
    soundboard = Adafruit_MCP230XX(address=SOUNDBOARD_ADDR, num_gpios=16)
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

def setup_control_bus():
    control = Adafruit_MCP230XX(address=CONTROL_ADDR, num_gpios=16)
    control.pullup(0, ENABLE)
    control.pullup(1, ENABLE)
    return control

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    work_it_A = load_sound(FULL_PATH + 'sounds/hbfs/101_work_it.wav')
    harder_A = load_sound(FULL_PATH + 'sounds/hbfs/102_harder.wav')
    make_it_A = load_sound(FULL_PATH + 'sounds/hbfs/103_make_it.wav')
    better_A = load_sound(FULL_PATH + 'sounds/hbfs/104_better.wav')
    do_it_A = load_sound(FULL_PATH + 'sounds/hbfs/105_do_it.wav')
    faster_A = load_sound(FULL_PATH + 'sounds/hbfs/106_faster.wav')
    makes_us_A = load_sound(FULL_PATH + 'sounds/hbfs/107_makes_us.wav')
    stronger_A = load_sound(FULL_PATH + 'sounds/hbfs/108_stronger.wav')
    more_than_A = load_sound(FULL_PATH + 'sounds/hbfs/109_more_than.wav')
    ever_A = load_sound(FULL_PATH + 'sounds/hbfs/110_ever.wav')
    hour_A = load_sound(FULL_PATH + 'sounds/hbfs/111_hour.wav')
    after_A = load_sound(FULL_PATH + 'sounds/hbfs/112_after.wav')
    our_A = load_sound(FULL_PATH + 'sounds/hbfs/113_our.wav')
    work_is_A = load_sound(FULL_PATH + 'sounds/hbfs/114_work_is.wav')
    never_A = load_sound(FULL_PATH + 'sounds/hbfs/115_never.wav')
    over_A = load_sound(FULL_PATH + 'sounds/hbfs/116_over.wav')
    work_it_B = load_sound(FULL_PATH + 'sounds/hbfs/201_work_it.wav')
    harder_B = load_sound(FULL_PATH + 'sounds/hbfs/202_harder.wav')
    make_it_B = load_sound(FULL_PATH + 'sounds/hbfs/203_make_it.wav')
    better_B = load_sound(FULL_PATH + 'sounds/hbfs/204_better.wav')
    do_it_B = load_sound(FULL_PATH + 'sounds/hbfs/205_do_it.wav')
    faster_B = load_sound(FULL_PATH + 'sounds/hbfs/206_faster.wav')
    makes_us_B = load_sound(FULL_PATH + 'sounds/hbfs/207_makes_us.wav')
    stronger_B = load_sound(FULL_PATH + 'sounds/hbfs/208_stronger.wav')
    more_than_B = load_sound(FULL_PATH + 'sounds/hbfs/209_more_than.wav')
    ever_B = load_sound(FULL_PATH + 'sounds/hbfs/210_ever.wav')
    hour_B = load_sound(FULL_PATH + 'sounds/hbfs/211_hour.wav')
    after_B = load_sound(FULL_PATH + 'sounds/hbfs/212_after.wav')
    our_B = load_sound(FULL_PATH + 'sounds/hbfs/213_our.wav')
    work_is_B = load_sound(FULL_PATH + 'sounds/hbfs/214_work_is.wav')
    never_B = load_sound(FULL_PATH + 'sounds/hbfs/215_never.wav')
    over_B = load_sound(FULL_PATH + 'sounds/hbfs/216_over.wav')
    main()
