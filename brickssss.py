import pygame,sys
from grid import Grid

pygame.init()

dark_background=(44,44,127)
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("python tetris")

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((dark_background))
    pygame.display.flip()
    clock.tick(60)