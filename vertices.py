from arestas import aresta
class vertice:#dot
    def __init__(self,X,Y,Id):
        self.X=X
        self.Y=Y
        self.Id= Id
        self.arestas=[]
    def add_arestas(self, aresta):
        self.arestas.append(aresta) 

    def get_position(self):
        return self.X,self.Y

    def get_id(self):
        return self.Id