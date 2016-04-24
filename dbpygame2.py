import pygame.mixer
from RPi import GPIO

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(25, GPIO.IN, GPIO.PUD_DOWN)

work = pygame.mixer.Sound("sounds/hbfs/101_work_it.wav")

def play(pin):
    print("playing")
    work.play()

GPIO.add_event_detect(25, GPIO.FALLING, play, 100)

print("ready")

while True:
    pass
