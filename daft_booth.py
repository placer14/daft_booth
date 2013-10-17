# Daft Booth v0.1
# Hacklab North Boynton

import pygame
import os, time

FULL_PATH = '/home/pi/python_games/'
def main():
  print('Running...')
  pygame.mixer.init()
  bg_sound = pygame.mixer.Sound(FULL_PATH + 'beep1.ogg')
  while True:
    bg_sound.play()
    time.sleep(2)

if __name__ == '__main__':
  main()
