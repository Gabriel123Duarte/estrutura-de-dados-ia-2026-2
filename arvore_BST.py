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
  

