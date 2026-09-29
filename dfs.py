from arvore_BST import ArvoreBusca
from visualizador_arvore import exibir_arvore


def dfs(raiz):
  if raiz is None:
    return
  
  pilha = [raiz]
  
  while len(pilha) > 0:
    atual = pilha.pop()
    
    print(atual.valor)
    
    if atual.direita is not None:
      pilha.append(atual.direita)
    
    if atual.esquerda is not None:
      pilha.append(atual.esquerda)
   
    


arvore = ArvoreBusca()

for valor in [50, 30, 70, 20, 40, 60, 80]:
  arvore.inserir(valor)


print("Árvore:")
exibir_arvore(arvore.raiz)


print("\nDFS:")
dfs(arvore.raiz)