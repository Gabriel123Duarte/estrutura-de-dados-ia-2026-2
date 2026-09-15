class NoArvore:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None
    
    
class ArvoreBusca:
  def __init__(self):
    self.raiz = None
    
  def inserir(self, valor):
    novo = NoArvore(valor)
    
    if self.raiz is None:
      self.raiz = novo
      return

    atual = self.raiz
    
    while True: 
      if valor > atual.valor:
        # Indo para direita
        if atual.direita is None:
          atual.direita = novo
          return
        atual = atual.direita
        
      elif valor < atual.valor:
        # Indo para esquerda
        if atual.esquerda is None:
          atual.esquerda = novo
          return
        atual = atual.esquerda
      else: 
        # Se for igual
        return
    
      
  def buscar(self, valor):
    atual = self.raiz
    
    while atual is not None: 
      if atual.valor == valor:
        return True
      if valor < atual.valor:
        atual = atual.esquerda
      elif valor > atual.valor:
        atual = atual.direita
        
        
    return False
  
arvore = ArvoreBusca()

arvore.inserir(50)
arvore.inserir(30)
arvore.inserir(70)
arvore.inserir(20)
arvore.inserir(40)
arvore.inserir(60)
arvore.inserir(80)

print(arvore.buscar(60))
print(arvore.buscar(25))

arvore.inserir(25)

print(arvore.buscar(25))