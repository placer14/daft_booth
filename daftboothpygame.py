#Daft Booth v0.2
#Hacklab North Boynton

import pygame, sys, random, math, os
from pygame.locals import *
import pygame.mixer
from RPi import GPIO
import smbus
import time


class level():
    color = (255, 255, 255)
    #gameover = false
    gamelevel = 1
    FPS = 30
    #countdown print (10,0)
    screen = pygame.display.set_mode((500, 500))   
    rect55 = pygame.Rect(50,50,50,50)
    pygame.draw.rect(screen,(255, 255, 0), rect55)

def init ():
    game_init ()


def game_init ():
   level.gamelevel = 0
   level.gameover_t = 0.0
   gamelevel_init ()

def gamelevel_init ():
    FPS = 24   

pygame.init()
pygame.mixer.init()
pygame.font.init()

#count down
time = 10
pygame.time.set_timer(USEREVENT+1, 1000)#1 second is 1000 mill


#Needed first to setup
bus = smbus.SMBus(1)
bus.write_byte_data(0x21,0x00,0x80) #To set group A as outputs
#bus.write_byte_data(0x20,0x14,0x00) #Sets all them to zero
#test output 1
#bus.write_byte_data(0x20,0x14,0x02)
#var = bus.read_byte_data(0x20,0x12)

FPS = 24
clock = pygame.time.Clock()
#text
dafttext = pygame.font.Font("banshee.ttf", 45) 
#dbtext = pygame.font.SysFont("monospace", 20)
#dbtext.set_bold(True)
boothlabel = pygame.font.SysFont("monospace", 26)
 
size = (500, 500)
screen = pygame.display.set_mode((size))
bounds = screen.get_rect()
# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (124, 252,   0)
BLUE  = (30, 144, 255 )
PURPLE = (148, 0, 211)
ORANGE = (255, 140, 0)
YELLOW = (255, 255, 0)


rect = pygame.Rect(30, 30, 15, 15)
rectA = pygame.Rect(45, 30, 15, 15)
rectB = pygame.Rect(60, 30, 15, 15)
rectC = pygame.Rect(75, 30, 15, 15)
rect2 = pygame.Rect(100, 45, 64, 64)
rectStart = pygame.Rect(200, 400, 85, 35)

#image = pygame.image.load("image.png")

pygame.display.set_caption('DAFT BOOTH')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

workit = pygame.mixer.Sound("sounds/hbfs/101_work_it.wav")
harder = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
makeit = pygame.mixer.Sound("sounds/hbfs/103_make_it.wav")
better = pygame.mixer.Sound("sounds/hbfs/104_better.wav")
doit = pygame.mixer.Sound("sounds/hbfs/105_do_it.wav")
faster = pygame.mixer.Sound("sounds/hbfs/106_faster.wav")
makesus = pygame.mixer.Sound("sounds/hbfs/107_makes_us.wav")
stronger = pygame.mixer.Sound("sounds/hbfs/108_stronger.wav")
morethan = pygame.mixer.Sound("sounds/hbfs/109_more_than.wav")
ever = pygame.mixer.Sound("sounds/hbfs/110_ever.wav")
hour = pygame.mixer.Sound("sounds/hbfs/111_hour.wav")
after = pygame.mixer.Sound("sounds/hbfs/112_after.wav")
our = pygame.mixer.Sound("sounds/hbfs/113_our.wav")
workis = pygame.mixer.Sound("sounds/hbfs/114_work_is.wav")
never = pygame.mixer.Sound("sounds/hbfs/115_never.wav")
over = pygame.mixer.Sound("sounds/hbfs/116_over.wav")
#next round
workit2 = pygame.mixer.Sound("sounds/hbfs/101_work_it.wav")
harder2 = pygame.mixer.Sound("sounds/hbfs/101_work_it.wav")
makeit2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
better2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
doit2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
faster2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
makesus2 = pygame.mixer.Sound("sounds/hbfs/101_work_it.wav")
stronger2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
morethan2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
ever2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
hour2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
after2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
our2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
workis2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
never2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")
over2 = pygame.mixer.Sound("sounds/hbfs/102_harder.wav")

# add sound file

sound_pins_1 = {
    1: workit,
    2: harder,
    4: makeit,
    8: better,
    16: doit,
    32: faster,
    64: makesus,
    128: stronger,
   # ?: morethan,
   # ?: ever,
   # ?: hour,
   # ?: after,
   # ?: our,
   # ?: workis,
    #add pin number and sound
}

labels = {
    1: "work it",
    2: "harder",
    4: "make it",
    8: "better",
    16: "do it",
    32: "faster",
    64: "makes us",
    128: "stronger",
   # ?: "more than",
   # ?: "ever",
   # ?: "hour",
   # ?: "after",
   # ?: "our",
   # ?: "work is",
   ##0: "never",
   ##0: "over",
}


def play(pin):
   sound = sound_pins_1[pin]
   print("playing note from pin %s" % pin)
   sound.play()
   label = labels[pin]
   newlabel = boothlabel.render(label, 1, BLACK)
   screen.blit(newlabel, (bounds.centerx, bounds.centery - bounds.height / 4))
   # GPIO.setup(19, GPIO.OUT)
   # GPIO.output(19, GPIO.LOW)
   
#for pin in sound_pins:
   # GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
   # GPIO.add_event_detect(pin, GPIO.FALLING, play, 100)


print("ready")

direction = "down"

def getInput():
    key = pygame.key.get_pressed()

while True: # main game loop
    #pass
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            time -= 1

        if level.gamelevel == 1:
            screen = pygame.display.set_mode((500, 500))
            rect55 = pygame.Rect(50,50,50,50)
            pygame.draw.rect(screen,(255, 255, 0), rect55)
  
    if time == 0:
        print "GAME OVER"
        level.gamelevel = 1
        
        if event.type == KEYDOWN:
             level.gamelevel = 1
               
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    
    var1 = bus.read_byte_data(0x20,0x12) #first 8 buttons
    var2 = bus.read_byte_data(0x20,0x13) # second 8 buttons
    var3 = bus.read_byte_data(0x21,0x12) # orange buttons

    print(var1)
    if var1 == 1:
	workit.play()
    if var1 == 2:
        harder.play()
    if var1 == 4:
        makeit.play()
    if var1 == 8:
        workit.play()
    if var1 == 16:
        stronger.play()
    if var1 == 32:
        workit.play()
    if var1 == 64:
        workit.play()
    if var1 == 128:
        workit.play()

    print(var2)
    if var2 == 1:
        workit.play()
    if var2 == 2:
        workit.play()
    if var2 == 4:
        workit.play()
    if var2 == 8:
        workit.play()
    if var2 == 16:
        workit.play()
    if var2 == 32:
        workit.play()
    if var2 == 64:
        workit.play()
    if var2 == 128:
        workit.play()

    print(var3)
    if var3 == 1:
        workit.play()
    if var3 == 2:
        workit.play()
    if var3 == 4:
        workit.play()
    if var3 == 8:
        workit.play()
    if var3 == 16:
        workit.play()
    if var3 == 32:
        workit.play()
    if var3 == 64:
        workit.play()
    if var3 == 128:
        workit.play()


    screen.fill(WHITE)
    pygame.draw.rect(screen, WHITE, rect)
    dlabel = dafttext.render("d", 1, PURPLE)
    pygame.draw.rect(screen, WHITE, rectA)
    alabel = dafttext.render("a", 1, ORANGE)
    pygame.draw.rect(screen, WHITE, rectB)
    flabel = dafttext.render("f", 1, GREEN)
    pygame.draw.rect(screen, WHITE, rectC)
    tlabel = dafttext.render("t", 1, BLUE)
    pygame.draw.rect(screen, WHITE, rect2)
    boothtext = boothlabel.render("BOOTH", 1, BLACK)
    pygame.draw.rect(screen, BLUE, rectStart)
    start = boothlabel.render("START", 1, BLACK)

    for x in range (20):
            pygame.draw.circle(screen, BLUE, (x * 40, 10), 10, 10)
            pygame.draw.circle(screen, YELLOW, (x * 40, 50), 10, 10)
            pygame.draw.circle(screen, ORANGE, (x * 40, 90), 10, 10)
            pygame.draw.circle(screen, PURPLE, (x * 40, 130), 10, 10)
  

    if direction == "down":
         rect2.centery += 1
    elif direction == "up":
         rect2.centery -= 1

    if rect2.bottom > size[1]:
        direction = "up"
    if rect2.top < 0:
        direction = "down"
   #daft letters
    if direction == "down":
         rect.centery += 1
    elif direction == "up":
         rect.centery -= 1

    if rect.bottom > size[1]:
        direction = "up"
    if rect.top < 0:
        direction = "down"

    if direction == "down":
         rectA.centery += 1
    elif direction == "up":
         rectA.centery -= 1

    if rectA.bottom > size[1]:
        direction = "up"
    if rectA.top < 0:
        direction = "down"

    if direction == "down":
         rectB.centery += 1
    elif direction == "up":
         rectB.centery -= 1

    if rectB.bottom > size[1]:
        direction = "up"
    if rectB.top < 0:
        direction = "down"

    if direction == "down":
         rectC.centery += 1
    elif direction == "up":
         rectC.centery -= 1

    if rectC.bottom > size[1]:
        direction = "up"
    if rectC.top < 0:
        direction = "down"
    
     
   
    screen.blit(start, rectStart)
    screen.blit(dlabel, rect)
    screen.blit(alabel, rectA)
    screen.blit(flabel, rectB)
    screen.blit(tlabel, rectC)
    screen.blit(boothtext, rect2)
    clock.tick(FPS)
    pygame.display.update()
