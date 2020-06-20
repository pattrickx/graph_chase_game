import pygame

class caracter:
    def __init__(self,X,Y,mapa,h,w,s_gap,cels,imgs,screen,Time=0):
        # super().__init__()
        self.X=X
        self.Y=Y
        self.mapa=mapa
        self.h=h
        self.w=w
        self.s_gap=s_gap
        self.old_key=0
        self.cels=cels
        self.imgs=imgs
        self.screen=screen
        self.Key=4
        self.mov=0
        self.pix=0
        self.old_time=Time
        self.time=Time
        self.old_pos=()
    def event_key(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: #Cima
                self.Key=3
                
            elif event.key == pygame.K_a: #Esquerda
                self.Key=1
                
            elif event.key == pygame.K_s: #Baixo 
                self.Key=0
                
            elif event.key == pygame.K_d: #Direita
                self.Key=2
                
            if self.Key<4:
                self.old_key=self.Key
        elif event.type == pygame.KEYUP:
            self.Key=4
            self.mov=0

    def movimento(self,delay,Time):
        self.time=Time-self.old_time
        if self.time>=delay:
            if self.Key==3: #cima
                if self.mapa[int((self.Y+self.h-1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                    self.Y-=1
            elif self.Key==0: #baixo
                if self.mapa[int((self.Y+self.h+1)/self.s_gap)][int((self.X+self.w)/self.s_gap)]!=1:
                    self.Y+=1
            elif self.Key==1: #esquerda
                if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w-1)/self.s_gap)]!=1:
                    self.X-=1
            elif self.Key==2: #direita
                if self.mapa[int((self.Y+self.h)/self.s_gap)][int((self.X+self.w+1)/self.s_gap)]!=1:
                    self.X+=1
            self.old_time=Time
    def show(self):
        if self.Key<4:
            self.pix+=1
            if self.pix==int(self.imgs.get_rect()[2]/40):
                if self.mov <= 2:
                    self.mov+=1
                else:
                    self.mov=0
                self.pix=0
            self.screen.blit(self.imgs,(self.X,self.Y),self.cels[self.Key][self.mov])

        else:
            self.screen.blit(self.imgs,(self.X,self.Y),self.cels[self.old_key][0])
    def get_position(self):
        return self.X,self.Y

    def Hunter_mode(self,caminho,delay,Time):
        
        self.time=Time-self.old_time
        if self.time>=delay:
            self.old_time=Time
            try:
                if self.old_pos==caminho[1][1]:
                    del(caminho[1])
                
                y,x=caminho[1][1]
                # print(caminho[1])
                if self.X != x-10 or self.Y != y-40:
                    self.Key=self.move_to(x-10,y-40)
                    return caminho
                else:
                    self.old_pos=caminho[1][1]
                    del(caminho[1])
                    self.Key=self.old_key
                    return caminho
            except :
                self.Key=4
                return caminho
        return caminho
        
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
        self.Key=4
        return 4
