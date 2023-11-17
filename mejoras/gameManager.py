import pygame
import sys
from player import Player
from enemy import Enemigo
from ground import Terreno
from plataforma import Plataforma
from vidas import *
from enemyGenerator import EnemyGenerator
from trap import Trap
class Game:
    def __init__(self):
        #Player
        self.player = Player(300, 300)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        #Balas
        self.balas = pygame.sprite.Group()
        self.balas_1 = pygame.sprite.Group()
        #Enemigo
        self.enemyGenerator = EnemyGenerator()
        #Vidas
        self.vidas = pygame.sprite.Group()
        vida = Vida(50,500,15,15)
        self.vidas.add(vida)
        #Frutas
        self.frutas =pygame.sprite.Group()
        fruta = Frutas (150,500,20,20)
        self.frutas.add(fruta)
        # Crear terrenos y plataformas de ejemplo
        self.terrenos = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        terreno = Terreno(0, 550, 600, 50)
        plataforma = Plataforma(200, 400, 200, 20)
        plataforma_1= Plataforma(200, 500, 200, 20)
        self.terrenos.add(terreno)
        self.plataformas.add(plataforma)
        self.plataformas.add(plataforma_1)
        #Trampas
        self.trap = pygame.sprite.Group()
        trampa = Trap(200,540,60,20)
        self.trap.add(trampa)
        self.colision_jugador_enemigo_procesada = False
        self.collision_clock = 0
    def run(self,teclas,screen):
        self.collision_clock += 1
        self.player.update(self.balas,teclas,self.terrenos, self.plataformas)
        self.balas.update()
        self.balas_1.update()
        self.enemyGenerator.update()
        screen.fill((30, 30, 30))
        self.terrenos.draw(screen)
        self.plataformas.draw(screen)
        self.trap.draw(screen)
        self.frutas.draw(screen)
        self.vidas.draw(screen)
        self.balas.draw(screen)
        self.balas_1.draw(screen)
        #self.enemigos.update(self.terrenos, self.plataformas,self.balas_1,self.player)  # Actualizar enemigos
        self.enemyGenerator.enemies.update(self.terrenos, self.plataformas,self.balas_1,self.player)  # Actualizar enemigos
        #self.enemigos.draw(screen)
        self.enemyGenerator.enemies.draw(screen)
        self.dañar_jugador()
        self.dañar_enmigo()
        self.sumar_vidas()
        self.sumar_puntos()
        self.daño_trampa()
        screen.blit(self.player.image, self.player.rect)
        
    def dañar_enmigo(self):
        colisiones = pygame.sprite.groupcollide(self.enemyGenerator.enemies, self.balas, True, True)
        for enemigo_dañado in colisiones.keys():
            print("le diste")
            self.player.puntos +=1
            print(self.player.puntos)
    def dañar_jugador(self):
            if not self.colision_jugador_enemigo_procesada:
                colisiones_jugador_enemigos = pygame.sprite.spritecollide(self.player, self.enemyGenerator.enemies, False)
                for colision in colisiones_jugador_enemigos:
                    print ("te dieron")
                    self.player.vidas -=1
                    print(self.player.vidas)
                    self.colision_jugador_enemigo_procesada = True
                colisiones_balas = pygame.sprite.spritecollide(self.player, self.balas_1, False)
                for colision in  colisiones_balas:
                    print ("te dieron")
                    self.player.vidas -=1
                    print(self.player.vidas)
                    self.colision_jugador_enemigo_procesada = True
    def sumar_vidas(self):
        colisiones_vidas = pygame.sprite.spritecollide(self.player, self.vidas, True)
        for colision in colisiones_vidas:
            print ("sumaste vida")
            self.player.vidas +=1
            print(self.player.vidas)
    def sumar_puntos(self):
        colisiones_frutas = pygame.sprite.spritecollide(self.player, self.frutas, True)
        for colision in colisiones_frutas:
            print ("sumaste puntos")
            self.player.puntos +=100
            print(self.player.puntos)
    def daño_trampa(self):
        colision_trampa= pygame.sprite.spritecollide(self.player, self.trap, True)
        for colision in colision_trampa:
            print ("te dieron")
            self.player.vidas -=1
            print(self.player.vidas)

