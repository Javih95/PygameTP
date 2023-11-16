import pygame
import sys

class Bala_enemigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direccion):
        super().__init__()
        ROJO = (255, 0, 0)
        self.image = pygame.Surface((10, 10))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direccion = direccion
    def update(self):
        # Mover la bala en la dirección en la que se disparó
        if self.direccion == "izquierda":
            self.rect.x -= 10
        elif self.direccion == "derecha":
            self.rect.x += 10
        # Eliminar la bala si sale de la pantalla
        if self.rect.y < 0 or self.rect.x < 0 or self.rect.x > 600:
            self.kill()
class Bala(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direccion):
        super().__init__()
        ROJO = (255, 0, 0)
        self.image = pygame.Surface((10, 10))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.direccion = direccion
    def update(self):
        # Mover la bala en la dirección en la que se disparó
        if self.direccion == "izquierda":
            self.rect.x -= 10
        elif self.direccion == "derecha":
            self.rect.x += 10
        # Eliminar la bala si sale de la pantalla
        if self.rect.y < 0 or self.rect.x < 0 or self.rect.x > 600:
            self.kill()
