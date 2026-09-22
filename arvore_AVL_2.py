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

    # Guardar o caminho percorrido para balancear depois da inserção
    # caminho = []
    
    while True:
      if valor > atual.valor:
        if atual.direita is None:
          atual.direita = novo
          break

        atual = atual.direita

      elif valor < atual.valor:
        if atual.esquerda is None:
          atual.esquerda = novo
          break

        atual = atual.esquerda

      else:
        # Não inserir valores repetidos
        return
      
    # Verificar o balanceamento de baixo para cima
    # self.rebalancear_caminho(caminho)

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
    # Guardar o caminho percorrido para balancear depois da inserção
    # caminho = []
    
    # Após a remoção, verificar o balanceamento de baixo para cima
    # if caminho:
    #   self.rebalancear_caminho(caminho)

    # elif self.raiz is not None:
    #   self.atualizar_altura(self.raiz)
    return None

  # ROTAÇÃO SIMPLES À DIREITA — CASO LL
  def rotacao_direita(self, no):
    
    # Atualizar as alturas
    # self.atualizar_altura(no)
    # self.atualizar_altura(nova_raiz)
    return None

  # ROTAÇÃO SIMPLES À ESQUERDA — CASO RR
  def rotacao_esquerda(self, no):
    
    # Atualizar as alturas
    # self.atualizar_altura(no)
    # self.atualizar_altura(nova_raiz)
    return None

  # ROTAÇÃO DUPLA ESQUERDA-DIREITA — CASO LR
  def rotacao_esquerda_direita(self, no):
    return None

  # ROTAÇÃO DUPLA DIREITA-ESQUERDA — CASO RL
  def rotacao_direita_esquerda(self, no):
    return None
  
  # Retorna a altura de um nó
  def altura(self, no):
    return 0
  
  # Recalcula a altura de um nó
  def atualizar_altura(self, no):
    return 0
  
  # Calcula o fator de balanceamento
  def fator_balanceamento(self, no):
    return 0

  # Identifica o tipo de desequilibrio e realiza a rotação necessária
  def balancear(self, no):
    return 0
  
  # Percorre o caminho de baixo para cima
  def rebalancear_caminho(self, caminho):
    return 0
  
# ==================================================
# VERSÃO 2 — AVL AUTOMÁTICA
# ==================================================

arvore = ArvoreBusca()


# ==================================================
# INSERÇÕES
# ==================================================

valores = [
  50,
  30,
  70,
  20,
  40,
  60,
  80
]

for valor in valores:
  print("\nInserindo:", valor)
  arvore.inserir(valor)
  exibir_arvore(arvore.raiz)


# ==================================================
# PROVOCANDO UM DESEQUILÍBRIO
# ==================================================

print("\nInserindo 10:")
arvore.inserir(10)
exibir_arvore(arvore.raiz)

print("\nInserindo 5:")
arvore.inserir(5)
exibir_arvore(arvore.raiz)


# ==================================================
# CONTINUANDO NA MESMA ÁRVORE
# ==================================================

print("\nInserindo 65:")
arvore.inserir(65)
exibir_arvore(arvore.raiz)

print("\nInserindo 75:")
arvore.inserir(75)
exibir_arvore(arvore.raiz)


# ==================================================
# REMOÇÕES
# ==================================================

print("\nRemovendo 80:")
arvore.remover(80)
exibir_arvore(arvore.raiz)

print("\nRemovendo 70:")
arvore.remover(70)
exibir_arvore(arvore.raiz)


# ==================================================
# RESULTADO FINAL
# ==================================================

print("\nÁrvore final:")
exibir_arvore(arvore.raiz)