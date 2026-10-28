grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

def dijkstra(grafo, origem):
  distancias = {}
  for vertice in grafo:    
    distancias[vertice] = float('inf')
  
  distancias[origem] = 0
  visitados = set() 
  
  while len(visitados) < len(grafo): 
    atual = None
    for vertice in grafo:
      if vertice not in visitados: 
        if atual is None or distancias[vertice] < distancias[atual]: 
          atual = vertice 
    
    if atual is None or distancias[atual] == float('inf'):
      break
    
    visitados.add(atual)
    
    for vizinho, peso in grafo[atual].items(): 
      nova_distancia = distancias[atual] + peso
      if nova_distancia < distancias[vizinho]:
        distancias[vizinho] = nova_distancia
    
    
  return distancias
    

distancias = dijkstra(grafo, 'A')
for destino in grafo:
    print(destino, 'distância:', distancias[destino])