import pygame
import math

def somaVetores(vetor1,vetor2):
    return (vetor1[0]+vetor2[0],vetor1[1]+vetor2[1])
"""tentativa de setas 
def defpontos(circulo1,circulo2):
    vetorDiretor=(circulo2[0]-circulo1[0],-(circulo2[1]-circulo1[1]))
    anglo = math.atan2(vetorDiretor[0],vetorDiretor[1])
    distance1 = math.sqrt((vetorDiretor[0]**2)+vetorDiretor[1]**2)-15
    ponto1 = somaVetores(circulo1,(distance1*math.cos(anglo),-(distance1*math.sin(anglo))))
    pontoI = somaVetores(circulo1,((distance1-7)*math.cos(anglo),-((distance1-7)*math.sin(anglo))))
    vectorPerpendicular = (vetorDiretor[1],-vetorDiretor[0])
    anglo2 = math.atan2(vectorPerpendicular[0],vectorPerpendicular[1])
    ponto2 = somaVetores(pontoI,(4*math.cos(anglo2),-(4*math.sin(anglo2))))
    vectorPerpendicular = (-vetorDiretor[1],vetorDiretor[0])
    anglo3 = math.atan2(vectorPerpendicular[0],vectorPerpendicular[1])
    ponto3 = somaVetores(pontoI,(4*math.cos(anglo3),-(4*math.sin(anglo3))))
    return [ponto1,ponto2,ponto3]

"""


def appendT(L,elem):
    c=True
    for i in L:
        if (i[0]==elem[0] and i[1]==elem[1]) or (i[1]==elem[0] and i[0]==elem[1]):
            c=False
            break
    if c:
        L.append(elem)
    
def Pmedio(p1,p2):
    return (round((p1[0]+p2[0])/2),round((p1[1]+p2[1])/2))

def appendC(C,elem):
    c=True
    for i in C:
        if math.sqrt((i[0]-elem[0])**2+(i[1]-elem[1])**2)<100:
            c=False
            break
    if c:
        C.append(elem)

def verficaConecçoes(C,L):
    for i in range(len(C)-1):
        apareceu=False
        for j in L:
            if j[0]==i or j[2]==i:
                apareceu=True
                break
        if not apareceu:
            return False
    return True

def distancia(elem,i):
    return round(math.sqrt((i[0]-elem[0])**2+(i[1]-elem[1])**2)/50)