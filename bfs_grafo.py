from collections import deque

def bfs(grafo, inicio):
  if inicio not in grafo:
    return
  
  fila = deque([inicio])
  visitados = {inicio}
  
  while len(fila) > 0:
    atual = fila.popleft()
    
    print(atual)
    
    for vizinho in grafo[atual]:
      if vizinho not in visitados:
        fila.append(vizinho)
        visitados.add(vizinho)
    


grafo = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"]
}

print("Percurso BFS:")
bfs(grafo, "A")