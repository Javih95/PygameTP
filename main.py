import pygame
import sys
from gameManager import Game
if __name__ == '__main__':
    pygame.init()
    screen_w = 600
    screen_h = 600
    screen = pygame.display.set_mode((screen_w, screen_h))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        teclas = pygame.key.get_pressed()
        screen.fill((30, 30, 30))
        game.run(teclas,screen)

        pygame.display.flip()
        clock.tick(60)
