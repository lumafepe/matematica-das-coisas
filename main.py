import pygame
import random
from triangle import Pmedio, appendT,appendC, distancia, verficaConecçoes

#cenas iniciais
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((1000, 1000),0,1)
pygame.display.flip()
pygame.display.set_caption('simulations')
running = True
myfont = pygame.font.SysFont('arial', 15)

#C=[(500,650),(600,600),(500,350),(400,400),(400,600),(600,400),(650,500),(350,500)]#nodos
C=[]#nodos
L=[]#linhas
nNodos=int(input("numero de nodos?"))

def setpos(n,C):
    while len(C)<n:
        appendC(C,(random.randint(100,900),random.randint(100,900)))

def putCircles(Cords,n,cor,display):
    pygame.draw.circle(display,cor,Cords,15)
    textsurface = myfont.render(str(n+1), False, (255, 255, 255))
    display.blit(textsurface,(Cords[0]-7,Cords[1]-7))
    pygame.display.update()

def putLines(circulo1,circulo2,cor,display):
    pygame.draw.line(display,cor,circulo1,circulo2,2)
    pygame.display.update()

def ligaTodos(C,display,L,nNodos):
    while len(L)<nNodos*1.5:#10 linhas
        j=i=random.randint(0,len(C)-1)
        while j==i:
            j=random.randint(0,len(C)-1)
        appendT(L,(i,distancia(C[i],C[j]),j))
    for elem in L:
        putLines(C[elem[0]],C[elem[2]],(0,255,255),display)
        textsurface = myfont.render(str(elem[1]), False, (255, 255, 255))
        display.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
    for i in range(len(C)):
        putCircles(C[i],i,(255,0,0),screen)
        

#gera nodos e conecçoes
setpos(nNodos,C)
ligaTodos(C,screen,L,nNodos)


#nodos vazios

while not verficaConecçoes(C,L):
    setpos(nNodos,C)
    ligaTodos(C,screen,L,nNodos)

while running:
    for event in pygame.event.get():
        pygame.display.update()
        if event.type == pygame.QUIT:
            running = False
     