import pygame
import random
from bala import Bala_enemigo
from raycast import Ray
class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        ROJO = (255, 0, 0)
        self.image = pygame.Surface((50, 50))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.en_suelo = False
        self.velocidad = 3
        self.direccion_move = random.choice([-1, 1])
        self.direccion = "derecha"
    def update(self,terrenos,plataformas,balas,jugador):
        self.move()
        self.limitar()
        self. gravedad(terrenos,plataformas)
        #self.shoot(balas)
        #self.mirar(jugador)
    def gravedad(self,terrenos,plataformas):
        colision_terreno = pygame.sprite.spritecollide(self, terrenos, False)
        colision_plataforma = pygame.sprite.spritecollide(self, plataformas, False)
        if not colision_terreno and not colision_plataforma:
            self.rect.y += 1  # Aplicar gravedad
            self.en_suelo = False
        elif colision_terreno:
            self.en_suelo = True
        elif colision_plataforma:
            if self.rect.bottom <= colision_plataforma[0].rect.top+5:  # Ajusta el valor según tu necesidad
                self.en_suelo = True
        if not self.en_suelo:
            self.rect.y += 1
    def move(self):
        self.rect.x += self.velocidad * self.direccion_move
        if self.direccion_move == -1:
            self.direccion = "izquierda"
        elif self.direccion_move == 1:
            self.direccion = "derecha"
    def limitar(self):
        if self.rect.y >= 550:
            self.rect.y = 550
            self.en_suelo = True
        if self.rect.x < 0:
            self.direccion_move *= -1  # Cambia la dirección
        elif self.rect.x > 550:
            self.direccion_move *= -1  # Cambia la dirección
