from arestas import aresta
from vertices import vertice
class grafo:
    def __init__(self,campo ):
        self.campo=campo
        self.vertices=[]

    def valido(self,ponto):
        if  ponto==2 or ponto==3:
            return True
        else:
            return False

    def criar(self):
        matriz= self.campo
        for i in range(len(matriz)):
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
                    self.vertices.append(vertice(i,j))
    def get_vertices(self):
        return self.vertices


                    
                    




