from ast import If
from operator import truediv
import pygame


pygame.init()
background_color = (0, 255, 0)

black = (0,0,0)
White = (255,255,255)

screen = pygame.display.set_mode((700, 700))
  
pygame.display.set_caption('Tick Tak Toe')
  
pygame.display.flip()
  
running = True

Rows = 3
Colum = 3

C1R1 = False
C2R1 = False
C3R1 = False
C1R2 = False
C2R2 = False
C3R2 = False
C1R3 = False
C2R3 = False
C3R3 = False


def AvalibeSpot(Row,Col):
    ValOf = False
    if Row == 1 & Col == 1:
        print(C1R1)
        if C1R1 == False:
            ValOf = False
        if C1R1 == True:
            ValOf = True

    if Row == 1 & Col == 2:
        if C2R1 == False:
            ValOf = False
        if C2R1 == True:
            ValOf = True
    if Row == 1 & Col == 3:
        if C3R1 == False:
            ValOf = False
        if C3R1 == True:
            ValOf = True
    if Row == 2 & Col == 1:
        if C1R2 == False:
            ValOf = False
        if C1R2 == True:
            ValOf = True
    if Row == 2 & Col == 2:
        print(C2R2)
    if Row == 2 & Col == 3:
        print(C2R2)
    if Row == 3 & Col == 1:
        print(C1R3)
    if Row == 3 & Col == 2:
        print(C2R3)
    if Row == 3 & Col == 3:
        print(C3R3)
        return
    
        
    



while running:

    for event in pygame.event.get():
         
        if event.type == pygame.KEYDOWN:
            AvalibeSpot(1,1)
            
            if event.type == pygame.K_LEFT:
                print("123")

        if event.type == pygame.QUIT:
            running = False
    

    pygame.display.update()

    screen.fill(background_color)

    #Lines
    #Vertical
    pygame.draw.rect(screen,black, [200,100,5,500])
    #Hortizantal
    pygame.draw.rect(screen,black, [50,250,500,5])
    #Vertical
    pygame.draw.rect(screen,black, [400,100,5,500])
    #Hortizantal
    pygame.draw.rect(screen,black, [50,450,500,5])

pygame.quit()