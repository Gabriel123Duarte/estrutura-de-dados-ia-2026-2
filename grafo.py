grafo = {
  "A": ["B", "C"],
  "B": ["A", "D", "E"],
  "C": ["A", "F"],
  "D": ["B"],
  "E": ["B", "F"],
  "F": ["C", "E"],
}

print("Lista de adjacência:")

for vertice in grafo:
  print(vertice, "->", grafo[vertice])