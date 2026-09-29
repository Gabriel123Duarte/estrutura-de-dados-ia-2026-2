from visualizador_arvore import exibir_arvore
from arvore_BST import ArvoreBusca

arvore = ArvoreBusca()

arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print("Buscando 60:", arvore.buscar(60))
print("Buscando 25:", arvore.buscar(25))

arvore.inserir(25)

print("Buscando 25 após inserir:", arvore.buscar(25))

print("\nÁrvore antes das remoções:")
exibir_arvore(arvore.raiz)


# ==================================================
# PARTE 2 — REMOÇÃO EM BST
# ==================================================

# CASO 1 — REMOVER UMA FOLHA

print("\nRemovendo 25 (folha):")
arvore.remover(25)
exibir_arvore(arvore.raiz)


# CASO 2 — REMOVER UM NÓ COM UM FILHO
#
# Criamos uma árvore separada para demonstrar
# corretamente esse caso.

arvore_um_filho = ArvoreBusca()

for valor in [50, 30, 70, 20]:
  arvore_um_filho.inserir(valor)

print("\nÁrvore com nó que possui um filho:")
exibir_arvore(arvore_um_filho.raiz)

print("\nRemovendo 30 (possui apenas o filho 20):")
arvore_um_filho.remover(30)
exibir_arvore(arvore_um_filho.raiz)


# CASO 3 — REMOVER UM NÓ COM DOIS FILHOS
#
# Voltamos à árvore original.
# Após remover 25, a raiz 50 ainda tem dois filhos.

print("\nRemovendo 50 (dois filhos):")
arvore.remover(50)
exibir_arvore(arvore.raiz)

print("\nBuscando 50:", arvore.buscar(50))
print("Buscando 60:", arvore.buscar(60))


