import pygame
class caracter:
    def __init__(self,X,Y):
        # super().__init__()
        self.X=X
        self.Y=Y
    def movimento(self,dir,mapa,h,w,s_gap):

        if dir==3: #cima
            if mapa[int((self.Y+h-1)/s_gap)][int((self.X+w)/s_gap)]!=1:
                self.Y-=1
        elif dir==0: #baixo
            if mapa[int((self.Y+h+1)/s_gap)][int((self.X+w)/s_gap)]!=1:
                self.Y+=1
        elif dir==1: #esquerda
            if mapa[int((self.Y+h)/s_gap)][int((self.X+w-1)/s_gap)]!=1:
                self.X-=1
        elif dir==2: #direita
            if mapa[int((self.Y+h)/s_gap)][int((self.X+w+1)/s_gap)]!=1:
                self.X+=1
    def get_position(self):
        return self.X,self.Y