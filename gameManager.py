import pygame
import sys
from player import Player
from enemy import Enemigo
from ground import Terreno
from plataforma import Plataforma
class Game:
    def __init__(self):
        self.player = Player(300, 300)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        self.balas = pygame.sprite.Group()
        self.balas_1 = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        enemigo = Enemigo(500, 300)
        self.enemigos.add(enemigo)
        self.colision_jugador_enemigo_procesada = False
        self.terrenos = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        # Crear terrenos y plataformas de ejemplo
        terreno = Terreno(0, 550, 600, 50)
        plataforma = Plataforma(200, 400, 200, 20)
        plataforma_1= Plataforma(200, 500, 200, 20)
        self.terrenos.add(terreno)
        self.plataformas.add(plataforma)
        self.plataformas.add(plataforma_1)
    def run(self,teclas,screen):
        self.player.update(self.balas,teclas,self.terrenos, self.plataformas)
        self.balas.update()
        screen.fill((30, 30, 30))
        self.terrenos.draw(screen)
        self.plataformas.draw(screen)
        self.balas.draw(screen)
        self.balas_1.draw(screen)
        self.enemigos.update(self.terrenos, self.plataformas,self.balas_1,self.players)  # Actualizar enemigos
        self.enemigos.draw(screen)
        self.dañar_jugador()
        self.dañar_enmigo()
        screen.blit(self.player.image, self.player.rect)
    def dañar_enmigo(self):
        colisiones = pygame.sprite.groupcollide(self.enemigos, self.balas, True, True)
        for enemigo_dañado in colisiones.keys():
            print("le diste")
            self.player.puntos +=1
            print(self.player.puntos)
    def dañar_jugador(self):
        if not self.colision_jugador_enemigo_procesada:
            colisiones_jugador_enemigos = pygame.sprite.spritecollide(self.player, self.enemigos, False)
            for colision in colisiones_jugador_enemigos:
                print ("te dieron")
                self.player.vidas -=1
                print(self.player.vidas)
                self.colision_jugador_enemigo_procesada = True
        
        
