import pygame
class caracter:
    def __init__(self,X,Y,mapa,h,w,s_gap):
        # super().__init__()
        self.X=X
        self.Y=Y
        self.mapa=mapa
        self.h=h
        self.w=w
        self.s_gap=s_gap
        self.old_key=4
    def movimento(self,dir):

        if dir==3: #cima
            if self.mapa[int((self.Y+self.h-1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                self.Y-=1
        elif dir==0: #baixo
            if self.mapa[int((self.Y+self.h+1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                self.Y+=1
        elif dir==1: #esquerda
            if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w-1)/self.s_gap)]!=1:
                self.X-=1
        elif dir==2: #direita
            if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w+1)/self.s_gap)]!=1:
                self.X+=1
    def get_position(self):
        return self.X,self.Y

    def Hunter_mode(self,caminho):
        if caminho:
            y,x=caminho[0][1]
            # print(caminho[0])
            if self.X != x-10 or self.Y != y-40:
                return self.move_to(x-10,y-40),caminho
            else:
                del(caminho[0])
                return self.old_key,caminho
        return 4,caminho
    def move_to(self,x,y):
        if self.X<x:
            if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w+1)/self.s_gap)]!=1:
                self.X+=1
                self.old_key=2
                return 2
        if self.X>x:
            if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w-1)/self.s_gap)]!=1:
                self.X-=1
                self.old_key=1
                return 1
        if self.Y<y:
            if self.mapa[int((self.Y+self.h+1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                self.Y+=1
                self.old_key=0
                return 0
        if self.Y>y:
            if self.mapa[int((self.Y+self.h-1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                self.Y-=1
                self.old_key=3
                return 3
        self.old_key=4
        return 4
