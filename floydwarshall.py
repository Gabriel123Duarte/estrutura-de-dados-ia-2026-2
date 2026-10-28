INF = float('inf')
grafo = [
  [0, 4, 2, INF, INF],
  [4, 0, 1, 5, INF],
  [2, 1, 0, 8, 10],
  [INF, 5, 8, 0, 2],
  [INF, INF, 10, 2, 0]
]


def floydWarshall(grafo):
  n = len(grafo[0])
  
  for k in range(n):
    for i in range(n):
      for j in range(n):
        nova_distancia = grafo[i][k] + grafo[k][j]
        if nova_distancia < grafo[i][j]:
          grafo[i][j] = nova_distancia
  
  
  return grafo
    
  

grafo = floydWarshall(grafo)
for linha in grafo:
    print(linha) 