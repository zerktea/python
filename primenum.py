from cgitb import text
from distutils import dir_util
import sys
import time
import os
from tkinter.font import BOLD
import pygame
pygame.init()
BLACK = (0, 0, 0)
RED = (136, 8, 8)
YELLOW = (251, 206, 177)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1200, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(RED)
pygame.display.set_caption("Prime Numbers Game")


def is_prime(num):
    for i in range(2, num-1):
        if(num % i == 0):
            return False

    return True


def display_number(num, Xpos, Ypos, primecounter):
    pygame.draw.rect(window, YELLOW, pygame.Rect(0, 0, 1800, 50))

    BOLD = False
    Textcolor = YELLOW
    if(is_prime(num)):
        Textcolor = BLACK

    myFont = pygame.font.SysFont("Times New Roman", 18, 1)

    pygame.draw.line(window, Textcolor, (Xpos, Ypos), (Xpos, Ypos+4), 5)
    numofprime = myFont.render(
        str(primecounter), True, BLACK)
    window.blit(numofprime, (200, 10))
    numofnumbers = myFont.render(
        str(num), True, BLACK)
    window.blit(numofnumbers, (WIDTH-50, 10))
    text1 = myFont.render(
        "NUMBER OF PRIMES:", True, BLACK)
    text2 = myFont.render(
        "NUMBER:", True, BLACK)
    window.blit(text1, (10, 10))
    window.blit(text2, (WIDTH-140, 10))
    pygame.display.update()


def main():
    primecounter = 0
    Xpos = WIDTH/2
    Ypos = HEIGHT/2
    Xstep = 5
    Ystep = 0
    Mxmovpercyc = 1
    crntmov = 0
    clockobject = pygame.time.Clock()
    run = True
    i = 0
    while run:
        clockobject.tick(15)
        pygame.display.flip()

        i = i+1
        if (is_prime(i)):
            primecounter += 1
        display_number(i, Xpos, Ypos, primecounter)
        Xpos = Xstep+Xpos
        Ypos = Ystep+Ypos
        if(crntmov == Mxmovpercyc):
            if(Xstep < 0):
                Xstep = 0
                Ystep = 5
            elif(Xstep > 0):
                Xstep = 0
                Ystep = -5
            elif(Ystep < 0):
                Ystep = 0
                Xstep = -5
            else:
                Ystep = 0
                Xstep = 5

            crntmov = 0
            Mxmovpercyc = Mxmovpercyc + 1
        else:
            crntmov = crntmov+1

        for e in pygame.event.get():

            if e.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()


main()
