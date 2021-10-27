from math import factorial
from typing import final
import pygame
import random
import time
from itertools import permutations
from sys import _current_frames, maxsize
from subprocess import PIPE,Popen
from pygame import display
from triangle import Pmedio, appendT,appendC, distancia, verficaConecçoes

#cenas iniciais
scalable=1
pygame.font.init()
pygame.init()
screen = pygame.display.set_mode((1000*scalable, 1000*scalable),0,1)
pygame.display.flip()
pygame.display.set_caption('simulations')
running = True
myfont = pygame.font.SysFont('arial', 15)
RED=(255,0,0)
GREEN=(0,200,0)
LIGHTBLUE=(0,255,255)
WHITE=(255,255,255)
BLACK=(0,0,0)


sleepAmount=0









#define posiçoes de nodos random
def setpos(n,C):
    while len(C)<n:
        appendC(C,(random.randint(100*scalable,900*scalable),random.randint(100*scalable,900*scalable)))






#coloca os circulos com o seu numero correspondente
def putCircles(Cords,n,cor,display):
    pygame.draw.circle(display,cor,Cords,15*scalable)
    textsurface = myfont.render(str(n+1), False, WHITE)
    display.blit(textsurface,(Cords[0]-7,Cords[1]-7))
    pygame.display.update()







#coloca uma linha entre 2 circulos
def putLines(circulo1,circulo2,cor,display):
    pygame.draw.line(display,cor,circulo1,circulo2,2)
    pygame.display.update()










#gera linhas aleatorias e coloca-as com o seu texto
def ligaTodos(C,display,L,nNodos):
    while len(L)<nNodos*2:#10 linhas
        j=i=random.randint(0,len(C)-1)
        while j==i:
            j=random.randint(0,len(C)-1)
        appendT(L,(i,scalable*distancia(C[i],C[j]),j))
    for elem in L:
        putLines(C[elem[0]],C[elem[2]],LIGHTBLUE,display)
        textsurface = myfont.render(str(elem[1]), False, WHITE)
        display.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
    for i in range(len(C)):
        putCircles(C[i],i,(255,0,0),screen)






#adiciona a linha de direação oposta a lista
def setmultidirection(L):
    d=len(L)
    for i in range(d):
        L.append((L[i][2],L[i][1],L[i][0]))






#cria um tipo do genero (i,[(d,j),(d2,j2)])
def changeDataType(L):
    L2=[]
    k=0
    for i in L:
        k+=1
        j=k
        temp2=[]
        temp1=i[0]
        temp2.append((i[1],i[2]))
        while j<len(L)-1:
            if L[j][0]==temp1:
                temp2.append((L[j][1],L[j][2]))
                L.pop(j)
            else:
                j+=1
        L2.append((temp1,temp2))
    return L2


#verifica se a sozionjos
def checkC(L2):
    for (i,d) in L2:
        if len(d)<2:
            return 0
    return 1


def arrange(list1):
    listai=[]
    listaj=[]
    for (i,j) in list1:
        if (i in listai):
            index=listai.index(i)
            listaj[index]+=j
        else:
            listai.append(i)
            listaj.append(j)
    finalList=[]
    for i in range(len(listai)):
        finalList.append((listai[i],listaj[i]))
    return finalList







def TSP_BruteForce(graph,screen):
    vertex=[]
    for i in range(1,len(graph)):
        vertex.append(i)
    bestPath = maxsize
    permutation=permutations(vertex)
    for i in permutation:
        i=(0,*i,0)
        screen.fill(BLACK)
        for elem in Lc:
            putLines(C[elem[0]],C[elem[2]],LIGHTBLUE,screen)
            textsurface = myfont.render(str(elem[1]), False, WHITE)
            screen.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
        for l in range(1,len(C)):
            putCircles(C[l],l,RED,screen)
        current_path=0
        for k in range(0,len(i)-1):
            current_path+=graph[i[k]][i[k+1]]
            putLines(C[i[k]],C[i[k+1]],GREEN,screen)
            putCircles(C[i[k]],i[k],GREEN,screen)
            putCircles(C[i[k+1]],i[k+1],GREEN,screen)
        if current_path<bestPath:
            bestPath=current_path
            bestPathP=i
    return (bestPathP,bestPath)
     



def TSP_MC(graph,fac,screen):
    vertex=[]
    for i in range(1,len(graph)):
        vertex.append(i)
    bestPath = maxsize
    p=4000000/fac
    permutation=permutations(vertex)
    for i in permutation:
        if (random.random()<fac):
            i=(0,*i,0)
            screen.fill(BLACK)
            for elem in Lc:
                putLines(C[elem[0]],C[elem[2]],LIGHTBLUE,screen)
                textsurface = myfont.render(str(elem[1]), False, WHITE)
                screen.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
            for l in range(1,len(C)):
                putCircles(C[l],l,RED,screen)
            current_path=0
            for k in range(0,len(i)-1):
                current_path+=graph[i[k]][i[k+1]]
                putLines(C[i[k]],C[i[k+1]],GREEN,screen)
                putCircles(C[i[k]],i[k],GREEN,screen)
                putCircles(C[i[k+1]],i[k+1],GREEN,screen)
            if current_path<bestPath:
                bestPath=current_path
                bestPathP=i
    return (bestPathP,bestPath)




#transforma a matriz num string
def setstring(List):
    string=""
    for i in List:
        for j in i:
            string+=" "
            string+=str(j)
        string+="\n" 
    return string   

def resetMapa(screen):
    screen.fill(BLACK)
    for elem in Lc:
        putLines(C[elem[0]],C[elem[2]],LIGHTBLUE,screen)
        textsurface = myfont.render(str(elem[1]), False, WHITE)
        screen.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
    for l in range(0,len(C)):
        putCircles(C[l],l,(255,0,0),screen)


def strip2moves(string):
    linhas=string.split('\n')
    linhas.pop()
    Ba=0
    As=[]
    for i in linhas:
        (a,b)=i.split()
        a,b=int(a),int(b)
        while (b<Ba):
            aa=As.pop()
            putCircles(C[aa],aa,RED,screen)
            putLines(C[aa],C[As[-1]],LIGHTBLUE,screen)
            Ba-=1
        if (b==Ba==0):
            if (len(As)!=0):
                aa=As.pop()
                putCircles(C[aa],aa,RED,screen)
            putCircles(C[a],a,GREEN,screen)
            As.append(a)
        elif (b==Ba):
            aa=As.pop()
            putCircles(C[aa],aa,RED,screen)
            putLines(C[aa],C[As[-1]],LIGHTBLUE,screen)
            putCircles(C[a],a,GREEN,screen)
            putLines(C[a],C[As[-1]],GREEN,screen)
            As.append(a)
        elif (b>Ba):
            putCircles(C[a],a,GREEN,screen)
            putLines(C[a],C[As[-1]],GREEN,screen)
            As.append(a)
            Ba+=1
        time.sleep(sleepAmount)

def setCAm(string):
    list=string.split("-")
    i=0
    aa=0
    for a in list:
        a=int(a)
        putCircles(C[a],a,GREEN,screen)
        if i!=0:
            putLines(C[a],C[aa],GREEN,screen)
        aa=a
        i+=1




class sim():
    def __init__(self):
        pass
    def BF(self):
        cam,custo=TSP_BruteForce(L5,1,screen)
        cam2=""
        for i in cam:
            cam2+=str(i)+"-"
        self.rm()
        setCAm(cam2[:-1])
        print(custo)

    def MC(self):
        cam,custo=TSP_MC(L5,factorial(nNodos),screen)
        cam2=""
        for i in cam:
            cam2+=str(i)+"-"
        self.rm()
        setCAm(cam2[:-1])
        print(custo)


    def BFT(self):
        child = Popen(["./tsp_bf"],stdin=PIPE, stdout=PIPE)
        output = (child.communicate((str(nNodos)+setstring(L5)).encode())[0]).decode()
        print("TEMPO: "+output[10:-1]+" ms")
    
    def MCT(self):
        child = Popen(["./tsp_mc"],stdin=PIPE, stdout=PIPE)
        output = (child.communicate((str(nNodos)+setstring(L5)).encode())[0]).decode()
        print("TEMPO: "+output[10:-1]+" ms")
    def NN(self):
        child = Popen(["./tsp_nn"],stdin=PIPE, stdout=PIPE)
        output = (child.communicate((str(nNodos)+setstring(L5)).encode())[0]).decode()
        (li,rescam)=output.split("RESPOSTA: ")
        (custo,camtemp)=rescam.split("CAMINHO: ")
        (cam,tempo) = camtemp.split("DURACAO: ")
        custo=int(custo)+L5[int(cam[-3])][0]
        print(f"CUSTO:{custo}\nTEMPO:{int(tempo)} ms")
        strip2moves("0 0\n"+li)
        resetMapa(screen)
        setCAm((cam[1:-1]+"0").replace(" ","-"))
        

    def DP(self):
        child = Popen(["./tsp_dp"],shell=True,stdin=PIPE, stdout=PIPE)
        output = (child.communicate((str(nNodos)+setstring(L5)).encode())[0]).decode()
        (li,rescam)=output.split("RESPOSTA: ")
        (custo,camtemp)=rescam.split("CAMINHO: ")#0-4-3-2-1-0
        (cam,tempo) = camtemp.split("DURACAO: ")
        print(f"CUSTO:{int(custo)}\nTEMPO:{int(tempo)} ms")
        strip2moves(li)
        resetMapa(screen)
        setCAm(cam)
    def DPT(self):
        child = Popen(["./tsp_dp"],shell=True,stdin=PIPE, stdout=PIPE)
        output = (child.communicate((str(nNodos)+setstring(L5)).encode())[0]).decode()
        (li,rescam)=output.split("RESPOSTA: ")
        (custo,camtemp)=rescam.split("CAMINHO: ")#0-4-3-2-1-0
        (cam,tempo) = camtemp.split("DURACAO: ")
        print(f"CUSTO:{int(custo)}\nTEMPO:{int(tempo)} ms")
        resetMapa(screen)
        setCAm(cam)
    def rm(self):
        resetMapa(screen)

    def SetSleep(self,a):
        global sleepAmount
        sleepAmount=a


    def f5(self):
        pygame.display.update()

    def gen(self,a):
        global nNodos,L2,C,Lc,L3,L,L5
        nNodos=a
        L2=[]
        while ((not checkC(L2)) or len(L2)!=nNodos):
            screen.fill(BLACK)
            C=[]#nodos
            L=[]#linhas
            setpos(nNodos,C)
            ligaTodos(C,screen,L,nNodos)
            Lc=L.copy()
            setmultidirection(L)
            L3=[]
            for i in range(nNodos):
                L4=[]
                for j in range(nNodos):
                    L4.append(-1)
                L3.append(L4)
            for i in range(nNodos):
                L3[i][i]=0
            for (i,d,f) in L:
                L3[i][f]=d
            L5=[]
            for i in range(nNodos):
                L4=[]
                for j in range(nNodos):
                    L4.append(maxsize)
                L5.append(L4)
            for i in range(nNodos):
                L5[i][i]=0
            for (i,d,f) in L:
                L5[i][f]=d
            Ltemp=changeDataType(L)
            L2=arrange(Ltemp)
    def genZ(self,a):
        global nNodos,L2,C,Lc,L3,L,L5
        nNodos=a
        L2=[]
        screen.fill(BLACK)
        C=[]#nodos
        L=[]#linhas
        setpos(nNodos,C)
        for i in range(len(C)):
            for j in range(len(C)):
                if j!=i:
                    appendT(L,(i,distancia(C[i],C[j]),j))
        for elem in L:
            putLines(C[elem[0]],C[elem[2]],LIGHTBLUE,screen)
            textsurface = myfont.render(str(elem[1]), False, WHITE)
            screen.blit(textsurface,Pmedio(C[elem[0]],C[elem[2]]))
        for i in range(len(C)):
            putCircles(C[i],i,(255,0,0),screen)
        Lc=L.copy()
        L3=[]
        for i in range(nNodos):
            L4=[]
            for j in range(nNodos):
                L4.append(0)
            L3.append(L4)
        for (i,d,f) in L:
            L3[i][f]=d
        L5=L3.copy()
        Ltemp=changeDataType(L)
        L2=arrange(Ltemp)

s=sim()
'''
s.BF()
s.BFT()
s.NN()
s.DP()
s.rm()
s.SetSleep(a)
s.f5()
s.reg(a)
'''