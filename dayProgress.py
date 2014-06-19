import pygame, sys, time, math
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 1000
WINDOWHEIGHT = 200
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Day Progress')


STARTTIME = 7
ENDTIME = 16

#TOTALMINUTES = (ENDTIME - STARTTIME) * 60
#CURRENTMINUTE = 0

TOTALSECONDS = (ENDTIME - STARTTIME) * 60 * 60
currentSecond = 0

CURRENTTIME = time.localtime()

SCALE = WINDOWWIDTH / TOTALSECONDS

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

while currentSecond < TOTALSECONDS:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    CURRENTTIME = time.localtime()    
    #CURRENTMINUTE = ((CURRENTTIME[3] - STARTTIME) * 60) + CURRENTTIME[4]
    currentSecond = ((CURRENTTIME[3] - STARTTIME) * 60 * 60) + (CURRENTTIME[4] * 60) + (CURRENTTIME[5])

    windowSurface.fill(BLACK)
    
    line25 = {'rect':pygame.Rect(WINDOWWIDTH * .25, 25, 1, 150), 'color':WHITE}
    line50 = {'rect':pygame.Rect(WINDOWWIDTH * .5, 25, 1, 150), 'color':WHITE}
    line75 = {'rect':pygame.Rect(WINDOWWIDTH * .75, 25, 1, 150), 'color':WHITE}

    if currentSecond < (TOTALSECONDS * 0.5):
        bar = {'rect':pygame.Rect(0, 50, currentSecond * SCALE, 100), 'color':GREEN}
    elif currentSecond < (TOTALSECONDS * 0.75):
        bar = {'rect':pygame.Rect(0, 50, currentSecond * SCALE, 100), 'color':YELLOW}
    else :        
        bar = {'rect':pygame.Rect(0, 50, currentSecond * SCALE, 100), 'color':RED}
       
    pygame.draw.rect(windowSurface, line25['color'], line25['rect'])
    pygame.draw.rect(windowSurface, line50['color'], line50['rect'])
    pygame.draw.rect(windowSurface, line75['color'], line75['rect'])
    pygame.draw.rect(windowSurface, bar['color'], bar['rect'])
        
    pygame.display.update()
    
    time.sleep(0.5)
