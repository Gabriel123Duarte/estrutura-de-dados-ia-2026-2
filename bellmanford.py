grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2},
    'E': {'C': 10, 'D': 2}
}

def bellmanFord(grafo, origem):
  distancias = {}
  for vertice in grafo:
    distancias[vertice] = float('inf')
  distancias[origem] = 0
  
  
  for _ in range(len(grafo)-1):
    for atual in grafo: 
      for vizinho, peso in grafo[atual].items():
        nova_distancia = distancias[atual] + peso
        
        if nova_distancia < distancias[vizinho]:
          distancias[vizinho] = nova_distancia
  
  for atual in grafo: 
    for vizinho, peso in grafo[atual].items():
      nova_distancia = distancias[atual] + peso
      
      if nova_distancia < distancias[vizinho]:
        print('Existe um ciclo negativo')
        return None
  
  return distancias
    
  


distancias = bellmanFord(grafo, 'A')
for destino in grafo:
    print(destino, 'distância:', distancias[destino])