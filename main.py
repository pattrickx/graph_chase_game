import pygame
from random import * ## para gerar numeros aleatorios
import time ## mede tempo 
import copy 
from caracter import caracter
from grafo import grafo
from vertices import vertice
from arestas import aresta
import dijkstra as dj
pygame.init()

screen = pygame.display.set_mode((1210, 710))
clock = pygame.time.Clock()
done = False
font = pygame.font.SysFont("arial", 20)

screen.fill((250, 250, 250)) # cor de fundo da tela


mapa=[[1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
      [2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
      [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,2],
      [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,2,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,2,2,2,2,2,2,2,1,1,1,2,1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,2,1,2,3,3,3,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,2,1,2,3,3,3,2,2,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,2,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,2,2,1,2,1],
      [1,1,1,2,1,1,1,1,2,1,2,3,3,3,3,3,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,3,3,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,3,3,2,1,2,1],
      [2,2,2,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2,1,1,1,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2],
      [1,1,1,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1,1,1,1,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1,1,1,1,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1],
      [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1],
      [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1],
      [1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,3,3,3,3,3,3,3,3,3,3,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,1,1,1,1,1,2,3,3,3,3,3,3,3,3,3,3,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
      [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,1,1,1,2,1],
      [1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,2,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,2,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,2,2,2,1,2,1],
      [1,1,1,2,1,1,1,1,1,1,2,3,3,3,3,3,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,3,3,2,1,2,1,1,1,1,2,1,1,1,1,1,1,2,3,3,3,3,3,2,1,2,1],
      [2,2,2,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,1,1,1,1,2,2,2,3,3,3,3,3,2,2,2,2],
      [1,1,1,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1,2,2,2,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1,1,1,1,2,1,1,1,1,2,3,2,3,3,3,3,3,3,2,1,1],
      [1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1],
      [1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1]]
arquivo = open('mapa.txt', 'w')
for x in mapa:
    arquivo.write(str(x)+'\n')
arquivo.close()
grafo= grafo(mapa)
grafo.criar()
ini=time.time()
X=0
Y=-20

Key=4
lKey=1
# personagem
'''
'redxiii.png'
'death_scythe.png'
'devil.png'
'greebo.png'
'pinkbat.png'
'sadako.png'
'tonberry.png'
'bahamut.png'
'ifrit.png'
'odin.png'
'leviathan.png'
'schoolboy.png'
'goldbat.png'
'silverticebat.png'
'mandar.png'
'dayita.png'
'''
assets=pygame.image.load('asets/BrightForest-A2.png')
s_gap=20
areia=(400,240,s_gap,s_gap)
solo=(0,0,s_gap,s_gap)
estrada=(64,98,s_gap,s_gap)

player=pygame.image.load('asets/devil.png')
# player = pygame.transform.scale(player,(int(player.get_rect()[2]/2),int(player.get_rect()[3]/2)))
def gerar_cels(n,image):
    cels=[]
    l=image.get_rect()[2]/n
    a=image.get_rect()[3]/n
    for i in range(n):
        linha=[]
        for j in range(n):
            linha.append((j*l,i*a,l,a))
        cels.append(linha)
    return cels
cels=gerar_cels(4,player)

# cels=[[(0,160,48,53),(49,160,48,53),(97,160,48,53),(145,160,48,53)], #cima
#     [(0,0,48,53),(49,0,48,53),(97,0,48,53),(145,0,48,53)],          # baixo
#     [(0,54,48,53),(49,54,48,53),(97,54,48,53),(145,54,48,53)],      # esquerda
#     [(0,106,48,53),(48,106,48,53),(96,106,48,53),(144,106,48,53)]]  # direita
mov=0
pix=0
atraso=0.02


def mostrar_grafo(vertice,aresta):
    for i in range(len(aresta)):
        ix,iy =vertice[aresta[i].get_origem()].get_position()
        fx,fy =vertice[aresta[i].get_destino()].get_position()
        pygame.draw.line(screen, (0,0,0), (iy*s_gap+s_gap/2,ix*s_gap+s_gap/2),(fy*s_gap+s_gap/2,fx*s_gap+s_gap/2), 1)
        
    for i in range(len(vertice)):
        x,y =vertice[i].get_position()
        
        pygame.draw.rect(screen, (250,0,0) , pygame.Rect(y*s_gap+s_gap/4,x*s_gap+s_gap/4, s_gap/2, s_gap/2 ))
        campo_induzido=font.render(str(vertice[i].Id), True, (255, 255, 255))
        screen.blit(campo_induzido,pygame.Rect(y*s_gap+s_gap/4,x*s_gap+s_gap/4, s_gap/2, s_gap/2 ))

caminho = dj.dijkstra(grafo.g,3,272,grafo.get_vertices(),s_gap)
# print(d)
# print(pai)
print(caminho)
jogador=caracter(X,Y,mapa,cels[0][0][3],cels[0][0][2]/2,s_gap)
old_premonition=time.time()
while not done:
    
    for event in pygame.event.get(): #condições para encerrar a janela
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #Cima
                Key=3
                
            elif event.key == pygame.K_a: #Esquerda
                Key=1
                
            elif event.key == pygame.K_s: #Baixo 
                Key=0
                

            elif event.key == pygame.K_d: #Direita
                Key=2
                

            if Key<4:
                lKey=Key

        elif event.type == pygame.KEYUP:
            
            Key=4
            mov=0
        
        

    T = time.time() - ini
    if T>=atraso: # delay de geração
        # jogador.movimento(Key)
        if caminho:
            Key,caminho=jogador.Hunter_mode(caminho)
        else:
            Key=4
        ini=time.time()

    premonition=time.time()-old_premonition
    if premonition>=200:
        caminho=dj.dijkstra(grafo.g,caminho[0][0],21,grafo.get_vertices(),s_gap)
        old_premonition=time.time()

    x,y=jogador.get_position()
    # print(x,' , ',y)
    if mapa[int(((cels[0][0][3])+y)/s_gap)][int((x+(cels[0][0][2]/2))/s_gap)]==2:
        # atraso=0.0083 # velocidade maxima para 120 fms
        # atraso=0.0041 # velocidade maxima para 240 fms
        atraso=0.002 # velocidade maxima para 480 fms
    if mapa[int(((cels[0][0][3])+y)/s_gap)][int((x+(cels[0][0][2]/2))/s_gap)]==3:
        atraso=0.05
    # screen.fill((250, 250, 250))
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j]==1:
                screen.blit(assets,(j*solo[2],i*solo[3]),solo)
            elif mapa[i][j]==2:
                screen.blit(assets,(j*solo[2],i*solo[3]),estrada)
            elif mapa[i][j]==3:
                screen.blit(assets,(j*solo[2],i*solo[3]),areia)
    
    # mostrar_grafo(grafo.get_vertices(),grafo.get_arestas())

    if Key<4:
        pix+=1
        if pix==int(player.get_rect()[2]/40):
            if mov <= 2:
                mov+=1
            else:
                mov=0
            pix=0
        screen.blit(player,(x,y),cels[Key][mov])
        
    else:
        screen.blit(player,(x,y),cels[lKey][0])
    # pygame.draw.rect(screen, (250,0,0) , pygame.Rect(int(x+(cels[0][0][2]/2))-2,int(y+(cels[0][0][3]))-2, 5, 5 ))
    

    


    pygame.display.flip()
    clock.tick(1200)