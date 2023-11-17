import pygame
class Plataforma(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)