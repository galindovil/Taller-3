import pygame
import random

#Crear una ventana 

#inicializar pygame
pygame.init()

dimensiones=(500,500)
miventana=pygame.display.set_mode(dimensiones)
x=250
y=250
while True:
    #rellenar ventana de rojo
    miventana.fill((255,0,0))
   
    pygame.draw.circle(miventana, (255,255,255), (x,y), 50)
    
#    lista.append(laPelota)
    pygame.display.update()
    
    x=random.randint(1,500)
    y=random.randint(1,500)