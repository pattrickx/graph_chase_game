import pygame
from random import * ## para gerar numeros aleatorios
import time ## mede tempo 
import copy 
from caracter import caracter
from grafo import grafo
from vertices import vertice
from arestas import aresta
import dijkstra as dj
import random
pygame.init()

screen = pygame.display.set_mode((1200, 700))
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
# for x in mapa:
#     arquivo.write(str(x)+'\n')
arquivo.close()
grafo= grafo(mapa)
grafo.criar()
ini=time.time()
inih=time.time()

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
assets2=pygame.image.load('asets/JapaneseVillage.png')
rock=(189,0,40,67)


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


# cels=[[(0,160,48,53),(49,160,48,53),(97,160,48,53),(145,160,48,53)], #cima
#     [(0,0,48,53),(49,0,48,53),(97,0,48,53),(145,0,48,53)],          # baixo
#     [(0,54,48,53),(49,54,48,53),(97,54,48,53),(145,54,48,53)],      # esquerda
#     [(0,106,48,53),(48,106,48,53),(96,106,48,53),(144,106,48,53)]]  # direita



def mostrar_grafo(vertice,aresta):
    for i in range(len(aresta)):
        ix,iy =vertice[aresta[i].get_origem()].get_position()
        fx,fy =vertice[aresta[i].get_destino()].get_position()
        pygame.draw.line(screen, (0,0,0), (iy*s_gap+s_gap/2,ix*s_gap+s_gap/2),(fy*s_gap+s_gap/2,fx*s_gap+s_gap/2), 2)
        
    for i in range(len(vertice)):
        x,y =vertice[i].get_position()
        
        pygame.draw.rect(screen, (250,0,0) , pygame.Rect(y*s_gap+s_gap/4,x*s_gap+s_gap/4, s_gap/2, s_gap/2 ))
        campo_induzido=font.render(str(vertice[i].Id), True, (255, 255, 255))
        screen.blit(campo_induzido,pygame.Rect(y*s_gap+s_gap/4,x*s_gap+s_gap/4, s_gap/2, s_gap/2 ))

def show_mapa(rocks):
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j]==1:
                screen.blit(assets,(j*s_gap,i*s_gap),solo)
            elif mapa[i][j]==2:
                screen.blit(assets,(j*s_gap,i*s_gap),estrada)
            elif mapa[i][j]==3:
                screen.blit(assets,(j*s_gap,i*s_gap),areia)
    if len(rocks)>0:
        for i in rocks:
            screen.blit(assets2,(i[0][1]*s_gap-10,i[0][0]*s_gap-30),rock)
            pygame.draw.rect(screen, (250,0,0) , pygame.Rect(int((i[0][1]*s_gap)+s_gap/2)-2,int((i[0][0]*s_gap)+s_gap/2)-2, 4, 4 ))
def show_caminho(cam):
    ix,iy=0,0
    Caminho=cam[1:]
    for c in Caminho:
        if(ix ==0 and iy ==0):
            ix,iy=c[1]
        else:
            fx,fy=c[1]
            pygame.draw.line(screen, (250,250,0), (iy+s_gap/2,ix+s_gap/2),(fy+s_gap/2,fx+s_gap/2), 2)
            pygame.draw.rect(screen, (0,0,250) , pygame.Rect(iy+s_gap/4,ix+s_gap/4, s_gap/2, s_gap/2 ))
            # campo_induzido=font.render(str(c[0]), True, (255, 255, 255))
            # screen.blit(campo_induzido,pygame.Rect(iy+s_gap/4,ix+s_gap/4, s_gap/2, s_gap/2 ))
            ix,iy=fx,fy
    pygame.draw.rect(screen, (0,0,250) , pygame.Rect(iy+s_gap/4,ix+s_gap/4, s_gap/2, s_gap/2 ))
    # campo_induzido=font.render(str(c[0]), True, (255, 255, 255))
    # screen.blit(campo_induzido,pygame.Rect(iy+s_gap/4,ix+s_gap/4, s_gap/2, s_gap/2 ))           

def game_over(jogador,hunter):
    if (abs(jogador[0]-hunter[0])<20 and abs(jogador[1]-hunter[1])<20):
        return False
    return True

def rocks(n,vertices):
    r=[]
    for i in range(n):
        r.append([(vertices[random.randrange(0,len(vertices)-1)].get_position()),0])
    return r
def break_rocks(position,rocks,particles):
    for i in range(len(rocks)):
        # print('--------')
        print('(',rocks[i][0][1],rocks[i][0][0],')    (',int((position[0]+cels[0][0][2])/s_gap),int((position[1]+cels[0][0][3])/s_gap),')')
        if abs(rocks[i][0][1]-int((position[0]+cels[0][0][2])/s_gap))<=2 and abs(rocks[i][0][0]-int((position[1]+cels[0][0][3])/s_gap))<=2:
            if rocks[i][1]<20:
                rocks[i][1]+=1
               
                pygame.mixer.init()
                pygame.mixer.music.load("music/picareta.mp3")
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play()
                particles.append([[rocks[i][0][1]*s_gap,rocks[i][0][0]*s_gap], [random.randint(0, 20) / 10 - 1, -2], random.randint(4, 10)])
                
            else:
                del(rocks[i])
            break

rocks=rocks(15,grafo.vertices)
mov=0
pix=0
atraso=0.005


X=0
Y=-20
Imgs=pygame.image.load('asets/devil.png')
cels=gerar_cels(4,Imgs)
hunter=caracter(X,Y,mapa,cels[0][0][3],cels[0][0][2]/2,s_gap,cels,Imgs,screen,time.time())
h_position=vertice(int(((cels[0][0][3])+Y-2)/s_gap),int((X-2+(cels[0][0][2]/2))/s_gap),len(grafo.vertices))


grafo.vertices.append(h_position)
grafo.new_vertice(h_position.Id)

old_premonition=time.time()
Key=4
lKey=1
Imgs=pygame.image.load('asets/mandar.png')
cels=gerar_cels(4,Imgs)

X=int(27*s_gap-(cels[0][0][2]/2)-2)#200
Y=int(5*s_gap-(cels[0][0][3])-2)#200

jogador=caracter(X,Y,mapa,cels[0][0][3],cels[0][0][2]/2,s_gap,cels,Imgs,screen)

j_position=vertice(int(((cels[0][0][3])+Y)/s_gap),int((X+(cels[0][0][2]/2))/s_gap),len(grafo.vertices))


grafo.vertices.append(j_position)
grafo.new_vertice(j_position.Id)
caminho = dj.dijkstra(grafo.g,h_position.Id,j_position.Id,grafo.get_vertices(),s_gap)
k_g=0
k_c=0
pygame.mixer.init()
pause=False
particles = []
while not done:
    for event in pygame.event.get(): #condições para encerrar a janela
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g: #Cima
                k_g=1-k_g
            if event.key == pygame.K_c: #Cima
                k_c=1-k_c
            if event.key == pygame.K_b:
                break_rocks(jogador.get_position(),rocks,particles)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_p:
                pause=True
                while pause:
                    for event in pygame.event.get(): #condições para encerrar a janela
                        if event.type == pygame.QUIT:
                            done = True
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                pause=False
        jogador.event_key(event)
    if len(rocks)==0:
        screen.fill((0, 0, 0))
        you_win=pygame.image.load('asets/you_win.jpg')
        screen.blit(you_win, (100,0))
        pygame.mixer.init()
        pygame.mixer.music.load("music/you_win.mp3")
        pygame.mixer.music.play()
        while True:
            for event in pygame.event.get(): #condições para encerrar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            pygame.display.flip()
            clock.tick(5)
    elif game_over(jogador.get_position(),hunter.get_position()):

            
        premonition=time.time()-old_premonition
        if premonition>=5 or len(caminho)<2:
            
            grafo.del_vertice(j_position.Id)
            grafo.del_vertice(h_position.Id)

            x,y=hunter.get_position()
            h_position=vertice(int(((cels[0][0][3])+y)/s_gap),int((x+(cels[0][0][2]/2))/s_gap),len(grafo.vertices))
            grafo.vertices.append(h_position)
            grafo.new_vertice(h_position.Id)
            

            x,y=jogador.get_position()
            j_position=vertice(int(((cels[0][0][3])+y)/s_gap),int((x+(cels[0][0][2]/2))/s_gap),len(grafo.vertices))
            grafo.vertices.append(j_position)
            grafo.new_vertice(j_position.Id)

            caminho=dj.dijkstra(grafo.g,h_position.Id,j_position.Id,grafo.get_vertices(),s_gap)
            
            old_premonition=time.time()

        x,y=hunter.get_position()
        # print(x,' , ',y)
        if mapa[int(((cels[0][0][3])+y)/s_gap)][int((x+(cels[0][0][2]/2))/s_gap)]==2:
            
            # atraso=0.0083 # velocidade maxima para 120 fms
            # atraso=0.0041 # velocidade maxima para 240 fms
            atraso=0.0002 # velocidade maxima para 480 fms
        else:
            atraso=0.09
        # screen.fill((250, 250, 250))

        show_mapa(rocks)
        try:
            if k_g==1:
                mostrar_grafo(grafo.get_vertices(),grafo.get_arestas())
            if k_c==1:
                show_caminho(caminho)
        except:
            print("print erro")
        jogador.movimento(0.00027,time.time())
        caminho=hunter.Hunter_mode(caminho,atraso,time.time())
        

        xj,yj=jogador.get_position()
        if yj>y:
            hunter.show()
            jogador.show(1)
        else:
            jogador.show(1)
            hunter.show()
        
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)
    else:
        
        game_over=pygame.image.load('asets/gameover.png')
        screen.blit(game_over, (0,0))
        pygame.mixer.init()
        pygame.mixer.music.load("music/evil-laugh.mp3")
        pygame.mixer.music.play()
        while True:
            for event in pygame.event.get(): #condições para encerrar a janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            pygame.display.flip()
            clock.tick(5)
        
    # pygame.draw.rect(screen, (250,0,0) , pygame.Rect(int(x+(cels[0][0][2]/2))-2,int(y+(cels[0][0][3]))-2, 5, 5 ))
    # pygame.draw.rect(screen, (250,0,0) , pygame.Rect(int(X+(cels[0][0][2]/2)),int(Y+(cels[0][0][3])), 10, 10 ))
    pygame.display.flip()
    clock.tick(480)