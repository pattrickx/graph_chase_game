
class vertice:#dot
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
        self.arestas=[]
    def set_arestas(self, arestas):
        self.arestas=arestas 

    def get_position(self):
        return self.X,self.Y
