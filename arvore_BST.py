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
    atual = self.raiz
    pai = None

    # 1. Procurar o nó que será removido
    while atual is not None and atual.valor != valor:
      pai = atual

      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita
    
    if atual is None: 
      print("Valor não encontrado", valor)
      return
    
    # 2. Caso o nó tenha no máximo um filho
    filho = None 
    if atual.esquerda is None: 
      filho = atual.direita
    elif atual.direita is None:
      filho = atual.esquerda
    # 3. Caso o nó tenha dois filhos   
    else: 
      pai_sucessor = atual 
      sucessor = atual.direita
      
      while sucessor.esquerda is not None:
        pai_sucessor = sucessor 
        sucessor = sucessor.esquerda
      
      # Copiar o valor do sucessor
      atual.valor = sucessor.valor
      
      atual = sucessor 
      pai = pai_sucessor
      
      filho = sucessor.direita
      
    # 4. Atualizar a referência do pai
    if pai is None: 
      # O nó era a raiz
      self.raiz = filho
    elif pai.esquerda is atual:
      pai.esquerda = filho
    else:
      pai.direita = filho
  

# ==================================================
# PARTE 1 — CONTINUAÇÃO DA AULA ANTERIOR
# ==================================================

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


