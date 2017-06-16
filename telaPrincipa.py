import pygame
from pygame.locals import *
from sys import exit
from random import randrange
import random
pygame.init()

BLACK = [0,0,0]
WHITE = [255,255,255]
tamanho = [620,498]

def tela_flocos():
    screen = pygame.display.set_mode(tamanho)
    pygame.display.set_caption("Tela Principal")
    background_filename = 'estrela.jpg'
    background = pygame.image.load(background_filename).convert()
    ship_filename = 'ship.png'
    ship = pygame.image.load(ship_filename).convert_alpha()
    ship_position = [randrange(100), randrange(200)]

    clock = pygame.time.Clock()
    while True:
        speed = {
            'x': 0,
            'y': 0
        }
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            speed['y'] = -5
        elif pressed_keys[K_DOWN]:
            speed['y'] = 5
        if pressed_keys[K_LEFT]:
            speed['x'] = -5
        elif pressed_keys[K_RIGHT]:
            speed['x'] = 5
        screen.blit(background, (0, 0))
        ship_position[0] += speed['x']
        ship_position[1] += speed['y']
        screen.blit(ship, ship_position)
        pygame.display.update()
        time_passed = clock.tick(100)

        matriz = []
        for i in range(50):
            x = random.randrange(0, 600)
            y = random.randrange(0, 750)
            matriz.append([x, y])
            clock = pygame.time.Clock()
            for i in range(len(matriz)):
               # Desenhe o floco de neve
               pygame.draw.circle(screen, WHITE, matriz[i], 1)
               matriz[i][1] += 1
               if matriz[i][1] > 500:
                   y = random.randrange(-50, -20)
                   matriz[i][1] = y
                   x = random.randrange(0, 400)
                   matriz[i][0] = x
        pygame.display.flip()
        clock.tick(30)
pygame.quit()

def desenho (screen, x,y):
    pygame.draw.ellipse(screen,WHITE,[35+x,y,25,25])
    pygame.draw.ellipse(screen, WHITE, [23+ x, 19 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])


tela_flocos()
desenho()

