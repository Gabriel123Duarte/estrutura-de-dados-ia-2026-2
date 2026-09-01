class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    
    
class Fila: 
  def __init__(self):
    self.inicio = None
    self.fim = None
    
  def estaVazia(self):
    return self.inicio is None
    
    
  def enfileirar(self, valor):
    novo = No(valor)
    
    if self.estaVazia():
      self.inicio = novo
      self.fim = novo
      return 
    
    self.fim.proximo = novo
    self.fim = novo 
    
    
  def desenfileirar(self):
    if self.estaVazia():
      print("Fila vazia")
      return None
    
    valor = self.inicio.valor 
    
    self.inicio = self.inicio.proximo
    
    if self.inicio is None:
      self.fim = None
    
    return valor
    
    
  def verInicio(self):
    if self.estaVazia():
        print("Fila vazia")
        return None        
    return self.inicio.valor 
    
    
  def exibir(self):
    atual = self.inicio
    
    print("Inicio", end=" -> ")

    while atual is not None:
      print(atual.valor, end=" -> ")
      atual = atual.proximo
      
    print("None")
    

fila = Fila() 

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

fila.exibir() 

print("Primeiro:", fila.verInicio())

print("Removendo:", fila.desenfileirar())

fila.exibir()
fila.enfileirar(40)
fila.exibir()