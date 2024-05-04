#########MODULOS IMPORTADOS 
from turtle import distance
import pygame
from pygame import mixer
import math
#INICIAR FUNCION PRINCIPAL
pygame.init()

#CONFIGURACION DE RESOLUCION DE PANTALLA
pantalla = pygame.display.set_mode((728,455))

#ELEGIR TITULO DEL JEUGO
pygame.display.set_caption("Ataque Ovni")

#MUSICA Y EFECTOS
mixer.music.load("./MusicaFondo.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

def boom():
    mixer.Sound("Explosion.mp3").play()
    
#ELEGIR Y PONER FAV_ICON
icono= pygame.image.load("Icon.jpg")
pygame.display.set_icon(icono)

#ELECCION DE FONDO (NO PLANO), UBICACION
fondo=pygame.image.load("Fondo.jpg")
fondoX=0
fondoY=0

#ELECION JUGADOR Y ENEMIGOS
playerMain = pygame.image.load("Nave3.png")
playerMainX=364
playerMainY=400
playerMov=0

enemigos = pygame.image.load("Enemigos3.png")
enemigoX=364
enemigoY=5
eneX=0.5
eneY=3
enemigo_vive=True

bala=pygame.image.load("Bala1.png")
balaX = playerMainX
balaY= 350
balaMov = 0
bala2 = 0
global shut
shut= False

#CREAR FUNCIONES PARA EL FONDO Y PERSONAJES
def fondoB():
    pantalla.blit(fondo,(fondoX,fondoY))
    
def player(x,y):
    pantalla.blit(playerMain,(x,y))
    
def enemigo(x,y):
    pantalla.blit(enemigos,(x,y))
    
def balafun(x,y):
    pantalla.blit(bala,(x,y))
 
def funcionDestruccion(x1,x2,y1,y2):
    distancia = math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))
    if  distancia <= 50:
        boom()
        global enemigo_vive
        enemigo_vive = False 
         
#LOOP DEL JUEGOd
ejecutar=True
while ejecutar:
    fondoB()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar= False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                playerMov = -0.5
            if evento.key == pygame.K_d:
                playerMov = 0.5
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                playerMov = 0
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if not shut:
                    mixer.Sound("Laser.mp3").play()
                    bala2 = playerMainX 
                    balaX = bala2
                    balaMov= -0.5
                    shut = True
               
    playerMainX += playerMov
    balaY += balaMov
    
    if balaY< -49:
        balaY=350
        balaMov=0
        shut = False
    if playerMainX <= 0 or playerMainX>=678:
        playerMov=0
        
    enemigoX += eneX 
    if enemigoX >= 678:
        eneX = -0.5
        enemigoY += eneY
    elif enemigoX <=0:
        eneX = 0.5
        enemigoY += eneY
        
        
    player(playerMainX, playerMainY)
    
    funcionDestruccion(enemigoX,balaX,enemigoY,balaY)
    
    if enemigo_vive:
       enemigo(enemigoX,enemigoY)
   
    
    
    if shut:
        balafun(balaX,balaY)
        
    
    pygame.display.update()