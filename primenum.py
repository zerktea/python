import sys
import time
import os
import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WIDTH, HEIGHT = 1200, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(WHITE)
pygame.display.set_caption("primenumbersgame")


def display_number(num, xpos, ypos):
    myFont = pygame.font.SysFont("Times New Roman", 18)
    text = myFont.render(str(num), True, BLACK)
    window.blit(text, (xpos, ypos))
    pygame.display.update()


def main():
    run = True
    while run:
        display_number(5, WIDTH/2, HEIGHT/2)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
