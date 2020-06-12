
from vertices import vertice
def initialize_single_source(g, inicio):
    n = len(g)
    d = [None] * n
    pai = [None] * n
    for v in range(n): 
        d[v] = float("+infinity")
        pai[v] = None
    d[inicio] = 0
    return d, pai
def extract_min(Q, S):
    n = len(Q)
    min = None
    for v in range(n): 
        if not S[v]:
           if min == None:
               min = v
           elif Q[v] < Q[min]:
               min = v
    return min
def dijkstra(g, inicio, destino,vertices,s_gap):
    d, pai = initialize_single_source(g, inicio)
    n = len(g)
    S = [False] * n 
                    
    Q = d           
                    
    for i in range(n):
        u = extract_min(Q, S)
        S[u] = True 
        for w, v in g[u]: 
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pai[v] = u
        caminho=[]
        vertice_atual = destino
    while vertice_atual != inicio:
        try:
            x,y = vertices[vertice_atual].get_position()
            caminho.insert(0,[vertice_atual,(x*s_gap,y*s_gap)] )
            vertice_atual = pai[vertice_atual]
        except KeyError:
            print('Caminho não acessível')
            break
    x,y = vertices[inicio].get_position()
    caminho.insert(0,[vertice_atual,(x*s_gap,y*s_gap)] )
    # if d[destino] < float("+infinity"):
    #     print('A menor distância é ' + str(d[destino]))
    #     print('E o caminho é ' + str(caminho))

    return caminho
