from arvore_BST import ArvoreBusca
from visualizador_arvore import exibir_arvore


arvore = ArvoreBusca()

for valor in [50, 30, 70, 20, 40, 60, 80]:
    arvore.inserir(valor)


print("Árvore:")
exibir_arvore(arvore.raiz)


def bfs(raiz):
    if raiz is None:
        return
    
    fila = [raiz]
    
    while fila:
        atual = fila.pop(0)
        
        print(atual.valor)
        
        if atual.esquerda is not None:
            fila.append(atual.esquerda)
        if atual.direita is not None:
            fila.append(atual.direita)


print("\nBFS:")
bfs(arvore.raiz)