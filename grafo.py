from arestas import aresta
from vertices import vertice
class grafo:
    def __init__(self,campo ):
        self.campo=campo
        self.vertices=[]
        self.arestas=[]

    def valido(self,ponto): # verifica se é um ponto jogavel
        if  ponto==2 or ponto==3:
            return True
        else:
            return False

    def buscar_vertice(self,x,y):
        for i in range(len(self.vertices)):
            X,Y=self.vertices[i].get_position()
            if X==x and Y==y:
                return self.vertices[i]

    def criar(self):
        matriz= self.campo
        Id = 0 
        for i in range(len(matriz)): # criar vertices
            for j in range(len(matriz[0])):
                n=0
                J=0
                I=0
                if  self.valido(matriz[i][j]):
                    if i>0 and self.valido(matriz[i-1][j]):
                            n+=1
                            I-=1
                    if j>0 and self.valido(matriz[i][j-1]):
                            n+=1
                            J-=1
                    if i<len(matriz)-2 and self.valido(matriz[i+1][j]):
                            n+=1
                            I+=1
                    if j<len(matriz[0])-2 and self.valido(matriz[i][j+1]):
                            n+=1
                            J+=1
                if n>2 or I!=0 or J!=0 :
                    self.vertices.append(vertice(i,j,Id))
                    Id+=1
        
        for i in range(len(self.vertices)):
            X,Y = self.vertices[i].get_position()
            if X>0:
                peso=0
                px=0
                for x in range(X-1,-1,-1):
                    if self.valido(matriz[x][Y]):
                        peso+=1 if matriz[x][Y]== 2 else 20
                        px=x
                    else:
                        break
                if peso>0:
                    fim=self.buscar_vertice(px,Y)
                    self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                    self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])


            if Y>0:
                peso=0
                py=0
                for y in range(Y-1,-1,-1):
                   if self.valido(matriz[X][y]):
                        peso+=1 if matriz[X][y]== 2 else 20 
                        py=y
                   else:
                        break
                if peso>0:
                    fim=self.buscar_vertice(X,py)
                    self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                    self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

            if X<len(matriz)-2:
                peso=0
                px=0
                for x in range(X+1,len(matriz[0])):
                    if self.valido(matriz[x][Y]):
                        peso+=1 if matriz[x][Y]== 2 else 20
                        px=x 
                    else:
                        break
                if peso>0:
                    fim=self.buscar_vertice(px,Y)
                    self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                    self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

            if Y<len(matriz[0])-2:# direita
                peso=0
                py=0
                for y in range(Y+1,len(matriz[0])):
                    if self.valido(matriz[X][y]):
                        peso+=1 if matriz[X][y]==2 else 20 
                        py=y
                    else:
                        break
                if peso>0:
                    fim=self.buscar_vertice(X,py)
                    self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                    self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

    def get_vertices(self):
        return self.vertices
    def get_arestas(self):
        return self.arestas





