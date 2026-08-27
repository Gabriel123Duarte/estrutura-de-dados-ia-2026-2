class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    
class ListaEncadeada:
  def __init__(self):
    self.cabeca = None
    
  def adicionar(self, valor): 
    novo = No(valor)
    
    if self.cabeca is None:
      self.cabeca = novo
      return
    
    atual = self.cabeca 
    
    while atual.proximo is not None: 
      atual = atual.proximo 
      
    atual.proximo = novo
    
  def adicionarInicio(self, valor):
    novo = No(valor)
    
    novo.proximo = self.cabeca
    self.cabeca = novo
    
  def buscar(self, valor):
    atual = self.cabeca
    
    while atual is not None: 
      if atual.valor == valor:
          return True
      atual = atual.proximo
      
    return False
  
  def exibir(self):
    atual = self.cabeca
    
    while atual is not None:
      print(atual.valor, end=" -> ")
      atual = atual.proximo
      
    print("None")
    
lista = ListaEncadeada()
lista.exibir()

lista.adicionar(10)
lista.adicionar(20)
lista.adicionar(30)
lista.adicionar(40)

lista.exibir()

print(lista.buscar(30))
print(lista.buscar(100)) 

lista.adicionarInicio(5)

lista.exibir()