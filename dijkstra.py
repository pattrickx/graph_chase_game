grafo = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


def dijkstra(grafo, inicio, destino):
    menor_distancia = {}
    antecessor = {}
    vertices_nao_vistos = grafo
    infinito = 9999999
    caminho = []
    for vertice in vertices_nao_vistos:
        menor_distancia[vertice] = infinito
    menor_distancia[inicio] = 0

    while vertices_nao_vistos:
        min_vertice = None
        for vertice in vertices_nao_vistos:
            if min_vertice is None:
                min_vertice = vertice
            elif menor_distancia[vertice] < menor_distancia[min_vertice]:
                min_vertice = vertice

        for vertice_filho, peso in grafo[min_vertice].items():
            if peso + menor_distancia[min_vertice] < menor_distancia[vertice_filho]:
                menor_distancia[vertice_filho] = peso + menor_distancia[min_vertice]
                antecessor[vertice_filho] = min_vertice
        vertices_nao_vistos.pop(min_vertice)

    vertice_atual = destino
    while vertice_atual != inicio:
        try:
            caminho.insert(0, vertice_atual)
            vertice_atual = antecessor[vertice_atual]
        except KeyError:
            print('Caminho não acessível')
            break
    caminho.insert(0, inicio)
    if menor_distancia[destino] != infinito:
        print('A menor distância é ' + str(menor_distancia[destino]))
        print('E o caminho é ' + str(caminho))


dijkstra(grafo, 'a', 'b')