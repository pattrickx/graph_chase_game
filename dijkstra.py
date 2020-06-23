
from vertices import vertice
def initialize_single_source(grafo, inicio):
   
    distance = [None] * len(grafo)
    pai = [None] * len(grafo)
    for v in range(len(grafo)):          # para v ← 1 até n faça
        distance[v] = float("+infinity") # dist[v] ← ∞
        pai[v] = None                    # dist[r] ← 0
    distance[inicio] = 0
    return distance, pai
def extract_min(vertices, S):

    min = None
    for v in range(len(vertices)): 
        if not S[v]:
           if min == None:
               min = v
           elif vertices[v] < vertices[min]:
               min = v
    return min
def dijkstra(grafo, inicio, destino,vertices,s_gap):
    distance, pai = initialize_single_source(grafo, inicio)
    
    S = [False] * len(grafo)
                    
    Q = distance  # Q ← Nova-Fila-com-Prioridades ( )  cria uma fila-com-prioridades vazia     
                    
    for i in range(len(grafo)):  #enquanto Q não está vazia faça
        v_min = extract_min(Q, S)    #  q ← Extraia-Min (Q) remove de Q um vértice q para o qual dist[q] é mínimo
        S[v_min] = True 
        for peso_adj, vertice_adj in grafo[v_min]:    # para cada w em Adj[q] faça
            if distance[vertice_adj] > distance[v_min] + peso_adj:  # se dist[w] > dist[q] + f(qw)
                #Diminua-Chave (w, Q, dist[q] + f(qw))
                distance[vertice_adj] = distance[v_min] + peso_adj  
                pai[vertice_adj] = v_min
    
    caminho=[]
    vertice_atual = destino
    v=vertices[vertice_atual]
    while vertice_atual != inicio:
        try:
            x,y = vertices[vertice_atual].get_position()
            caminho.insert(0,[vertice_atual,(x*s_gap,y*s_gap)] )
            vertice_atual = pai[vertice_atual]
        except:
            print('Caminho não acessível')
            break
    x,y = vertices[inicio].get_position()
    caminho.insert(0,[vertice_atual,(x*s_gap,y*s_gap)] )
    
    # if d[destino] < float("+infinity"):
    #     print('A menor distância é ' + str(d[destino]))
    #     print('E o caminho é ' + str(caminho))

    return caminho
