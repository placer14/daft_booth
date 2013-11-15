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
    work_it_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/101_work_it.wav')
    harder_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/102_harder.wav')
    make_it_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/103_make_it.wav')
    better_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/104_better.wav')
    do_it_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/105_do_it.wav')
    faster_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/106_faster.wav')
    makes_us_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/107_makes_us.wav')
    stronger_A = pygame.mixer.Sound(FULL_PATH + 'sounds/hbfs/108_stronger.wav')

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
                    work_it_A.play()
                elif (event.key == pygame.K_2):
                    harder_A.play()
                elif (event.key == pygame.K_3):
                    make_it_A.play()
                elif (event.key == pygame.K_4):
                    better_A.play()
                elif (event.key == pygame.K_5):
                    do_it_a.play()
                elif (event.key == pygame.K_6):
                    faster_A.play()
                elif (event.key == pygame.K_7):
                    makes_us_A.play()
                elif (event.key == pygame.K_8):
                    stronger_A.play()


if __name__ == '__main__':
    main()
