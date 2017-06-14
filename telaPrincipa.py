import pygame
import random

pygame.init()

BLACK = [0,0,0]
WHITE = [255,255,255]
# Defina a altura e a largura da tela
tamanho = [400,400]

screen = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Tela Principal")
backgroun_image = pygame.image.load("estrela.png").convert()
backgroun_image = pygame.image.load("ship.png").convert()

# Criar uma matriz vazia
matriz = []

# Loop 50 vezes e adicione
#  um floco de neve em uma posição aleatória x, y
for i in range(50):
    x = random.randrange(0,600)
    y = random.randrange(0,600)
    matriz.append([x,y])
clock = pygame.time.Clock()

# loop até o usuário clicar no botão Fechar.
pressionar = False
while not pressionar:
    for event in pygame.event.get():#o usuario pressionou algo
        if event.type == pygame.QUIT:# Se o usuário clicou em fechar
            pressionar = True  # Indique que estamos preparados para que saia deste loop

    # Defina o fundo da tela
    screen.fill(BLACK)
    screen.blit(backgroun_image, [0, 0])


    # Processe cada floco de neve na lista
    for i in range(len(matriz)):
        # Desenhe o floco de neve
        pygame.draw.circle(screen, WHITE, matriz[i], 2)

        # Mova o floco de neve para baixo um pixel
        matriz[i][1] += 1

        # Se o floco de neve se deslocou da parte inferior da tela
        if matriz[i][1] > 600:

            # Reinicie-o apenas acima do topo
            y = random.randrange(-50, -10)
            matriz[i][1] = y

            # Dê uma nova posição x
            x = random.randrange(0, 400)
            matriz[i][0] = x

    #atualize a tela com o que foi desenhado.
    pygame.display.flip()
    clock.tick(30)
#saindo do processo
pygame.quit()

def desenho (screen, x,y):
    pygame.draw.ellipse(screen,WHITE,[35+x,y,25,25])
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [x, 65 + y, 100, 100])

desenho()