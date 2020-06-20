from arestas import aresta
from vertices import vertice
class grafo:
    def __init__(self,campo ):
        self.campo=campo
        self.vertices=[]
        self.arestas=[]
        self.g=[[]]
    
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
        
        return False

    def criar(self):
        Id = 0 
        for i in range(len(self.campo)): # criar vertices
            for j in range(len(self.campo[0])):
                n=0
                J=0
                I=0
 
                if  self.valido(self.campo[i][j]):
                    if i>0 and self.valido(self.campo[i-1][j]):
                            n+=1
                            I-=1
                    if j>0 and self.valido(self.campo[i][j-1]):
                            n+=1
                            J-=1
                    if i<=len(self.campo)-2 and self.valido(self.campo[i+1][j]):
                            n+=1
                            I+=1
                    if j<=len(self.campo[0])-2 and self.valido(self.campo[i][j+1]):
                            n+=1
                            J+=1

                if n>2 or I!=0 or J!=0 :
                    self.vertices.append(vertice(i,j,Id))
                    Id+=1
        arquivo = open('vertices.txt', 'w')
        for x in self.vertices:
            o,l=x.get_position()
            s=str(x.Id) +'('+str(o)+','+str(l)+')\n'
            arquivo.write(s)
        arquivo.close()

        self.g=[[] for x in range(len(self.vertices))]
        for i in range(len(self.vertices)):
            self.finde_arestas(i)
        # for x in self.g:
        #     print(x)
        arquivo = open('novo-arquivo.txt', 'w')
        for x in self.g:
            arquivo.write(str(x)+'\n')
        arquivo.close()
    def get_vertices(self):
        return self.vertices
    def get_arestas(self):
        return self.arestas

    def finde_arestas(self,i):
        X,Y = self.vertices[i].get_position()
        if X>0:
            peso=0
            px=0
            for x in range(X-1,-1,-1):
                
                if self.valido(self.campo[x][Y]):
                    peso+=1 if self.campo[x][Y]== 2 else 2
                    px=x
                    if self.buscar_vertice(x,Y)!= False:
                        break
                else:
                    break
                    
            if peso>0:
                fim=self.buscar_vertice(px,Y)
                self.g[self.vertices[i].get_id()].append((peso,fim.get_id()))
                # print(i)
                # print(self.g[self.vertices[i].get_id()])
                self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])
        if Y>0:
            peso=0
            py=0
            for y in range(Y-1,-1,-1):
                
                if self.valido(self.campo[X][y]):
                    peso+=1 if self.campo[X][y]== 2 else 2
                    py=y
                    if self.buscar_vertice(X,y)!= False:
                        break
                else:
                    break
            if peso>0:
                fim=self.buscar_vertice(X,py)
                self.g[self.vertices[i].get_id()].append((peso,fim.get_id()))
                # print(i)
                # print(self.g[self.vertices[i].get_id()])
                self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

        if X<=len(self.campo)-2:
            peso=0
            px=0
            for x in range(X+1,len(self.campo)):
                
                if self.valido(self.campo[x][Y]):
                    peso+=1 if self.campo[x][Y]== 2 else 2
                    px=x
                    if self.buscar_vertice(x,Y)!= False:
                        break
                else:
                    break
            if peso>0:
                fim=self.buscar_vertice(px,Y)
                self.g[self.vertices[i].get_id()].append((peso,fim.get_id()))
                # print(i)
                # print(self.g[self.vertices[i].get_id()])
                self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

        if Y<=len(self.campo[0])-2:# direita
            peso=0
            py=0
            for y in range(Y+1,len(self.campo[0])):
                
                if self.valido(self.campo[X][y]):
                    peso+=1 if self.campo[X][y]==2 else 2
                    py=y
                    if self.buscar_vertice(X,y)!= False:
                        break
                else:
                    break
            if peso>0:
                fim=self.buscar_vertice(X,py)
                self.g[self.vertices[i].get_id()].append((peso,fim.get_id()))
                # print(i)
                # print(self.g[self.vertices[i].get_id()])
                self.arestas.append(aresta(self.vertices[i].get_id(),fim.get_id(),peso))
                self.vertices[i].add_arestas(self.arestas[len(self.arestas)-1])

    def new_vertice(self,i):
        self.g.append([])
        self.finde_arestas(i)

        Arestas=self.vertices[i].arestas
        for a in Arestas:
            self.g[a.destino].append((a.peso,i))
            self.arestas.append(aresta(self.vertices[a.destino].get_id(),i,a.peso))
            self.vertices[a.destino].add_arestas(self.arestas[len(self.arestas)-1])
    def del_vertice(self,id):
        v=self.vertices[id]
        del(self.vertices[id])
        del(self.g[id])
        for a in v.arestas:
            try:
                del(self.g[a.destino][len(self.g[a.destino])-1])
            except:
                print("já removido")
            self.del_aresta(a.destino,a.origem,a.peso)
            self.del_aresta(a.origem,a.destino,a.peso)
            
    def del_aresta(self,origem, destino, peso):
        for i in range(len(self.arestas)-1,-1,-1):
            if self.arestas[i].origem==origem and self.arestas[i].destino==destino and self.arestas[i].peso==peso:
                del(self.arestas[i])
                break


