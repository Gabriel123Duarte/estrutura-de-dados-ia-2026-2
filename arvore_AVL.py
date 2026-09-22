from visualizador_arvore import exibir_arvore

class NoArvore:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None


class ArvoreBusca:
  def __init__(self):
    self.raiz = None

  # INSERÇÃO
  def inserir(self, valor):
    novo = NoArvore(valor)

    if self.raiz is None:
      self.raiz = novo
      return

    atual = self.raiz

    while True:
      if valor > atual.valor:
        if atual.direita is None:
          atual.direita = novo
          return

        atual = atual.direita

      elif valor < atual.valor:
        if atual.esquerda is None:
          atual.esquerda = novo
          return

        atual = atual.esquerda

      else:
        # Não inserir valores repetidos
        return

  # BUSCA
  def buscar(self, valor):
    atual = self.raiz

    while atual is not None:
      if atual.valor == valor:
        return True

      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita

    return False

  def remover(self, valor):
    return None


  # ROTAÇÃO SIMPLES À DIREITA — CASO LL
  def rotacao_direita(self, no):
    return None

  # ROTAÇÃO SIMPLES À ESQUERDA — CASO RR
  def rotacao_esquerda(self, no):
    return None

  # ROTAÇÃO DUPLA ESQUERDA-DIREITA — CASO LR
  def rotacao_esquerda_direita(self, no):
    return None

  # ROTAÇÃO DUPLA DIREITA-ESQUERDA — CASO RL
  def rotacao_direita_esquerda(self, no):
    return None



# ==================================================
# INTRODUÇÃO ÀS ROTAÇÕES AVL
# ==================================================
#
# Cada exemplo usa uma árvore nova.
# As rotações são chamadas manualmente.
# A inserção ainda NÃO balanceia automaticamente.


# EXEMPLO 1 — LL: ROTAÇÃO À DIREITA

arvore_ll = ArvoreBusca()

for valor in [30, 20, 10]:
  arvore_ll.inserir(valor)

print("\nCASO LL — Antes:")
exibir_arvore(arvore_ll.raiz)

arvore_ll.raiz = arvore_ll.rotacao_direita(arvore_ll.raiz)

print("\nCASO LL — Depois:")
exibir_arvore(arvore_ll.raiz)


# EXEMPLO 2 — RR: ROTAÇÃO À ESQUERDA

arvore_rr = ArvoreBusca()

for valor in [10, 20, 30]:
  arvore_rr.inserir(valor)

print("\nCASO RR — Antes:")
exibir_arvore(arvore_rr.raiz)

arvore_rr.raiz = arvore_rr.rotacao_esquerda(arvore_rr.raiz)

print("\nCASO RR — Depois:")
exibir_arvore(arvore_rr.raiz)


# EXEMPLO 3 — LR: ESQUERDA-DIREITA

arvore_lr = ArvoreBusca()

for valor in [30, 10, 20]:
  arvore_lr.inserir(valor)

print("\nCASO LR — Antes:")
exibir_arvore(arvore_lr.raiz)

arvore_lr.raiz = arvore_lr.rotacao_esquerda_direita(
  arvore_lr.raiz
)

print("\nCASO LR — Depois:")
exibir_arvore(arvore_lr.raiz)


# EXEMPLO 4 — RL: DIREITA-ESQUERDA

arvore_rl = ArvoreBusca()

for valor in [10, 30, 20]:
  arvore_rl.inserir(valor)

print("\nCASO RL — Antes:")
exibir_arvore(arvore_rl.raiz)

arvore_rl.raiz = arvore_rl.rotacao_direita_esquerda(
  arvore_rl.raiz
)

print("\nCASO RL — Depois:")
exibir_arvore(arvore_rl.raiz)