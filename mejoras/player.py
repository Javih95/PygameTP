import pygame
from bala import Bala

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        BLANCO = (255, 255, 255)
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
        self.velocidad = 5
        self.velocidad_salto = 75
        self.en_suelo = False
        self.direccion = "derecha"  # Dirección inicial del jugador
        self.vidas = 5
        self.puntos = 0
        self.shoot_timer = 0
    def update(self,balas,teclas,terrenos, plataformas):
        self.shoot(balas,teclas)
        self.shoot_timer += 1
        self.jump(teclas)
        self.move(teclas)
        self.limitar()
        self. gravedad(terrenos,plataformas)
    def gravedad(self,terrenos,plataformas):
        colision_terreno = pygame.sprite.spritecollide(self, terrenos, False)
        colision_plataforma = pygame.sprite.spritecollide(self, plataformas, False)
        if not colision_terreno and not colision_plataforma :
            self.rect.y += 1  # Aplicar gravedad
            self.en_suelo = False
        elif colision_terreno:
            self.en_suelo = True
        elif colision_plataforma:
            if self.rect.bottom <= colision_plataforma[0].rect.top+5:  # Ajustar valor de tolerancia
                self.en_suelo = True
        if not self.en_suelo:
            self.rect.y += 1 # Aplicar gravedad
    def move(self,teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
            self.direccion = "izquierda"
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
            self.direccion = "derecha"
        if teclas[pygame.K_UP]:
            self.direccion = "arriba"
        if teclas[pygame.K_UP] and teclas[pygame.K_LEFT]:
            self.direccion = "diagonal_izquierda"
        if teclas[pygame.K_UP] and teclas[pygame.K_RIGHT]:
            self.direccion = "diagonal_derecha"
    def jump(self,teclas):
        if teclas[pygame.K_SPACE]:
            if self.en_suelo:
                self.rect.y -= self.velocidad_salto
                self.en_suelo = False
    def shoot(self, balas,teclas):
        # Crear una nueva bala en la posición del jugador y con la dirección actual
        if teclas[pygame.K_s]:
            
            if self.shoot_timer >= 20:
                bala = Bala(self.rect.x + self.rect.width // 2, self.rect.y, self.direccion)
                balas.add(bala)
                self.shoot_timer = 0
    def limitar(self):
        if self.rect.y >= 550:
            self.rect.y = 550
            self.en_suelo = True
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 550:
            self.rect.x = 550
    