class No:
  def __init__(self, valor):
    self.valor = valor
    self.proximo = None
    
    
class Pilha: 
  def __init__(self):
    self.topo = None
    
  def estaVazia(self):
    return self.topo is None 
  
  def empilhar(self, valor):
    novo = No(valor) 
    
    novo.proximo = self.topo
    self.topo = novo 
    
    
  def desempilhar(self):
    if self.estaVazia():
      print("Pilha vazia")
      return None
    
    valor = self.topo.valor 
    
    self.topo = self.topo.proximo
    
    return valor
    
  def verTopo(self):
    if self.estaVazia():
        print("Pilha vazia")
        return None
    
    return self.topo.valor
    
    
  def exibir(self):
    atual = self.topo 
    
    print("TOPO")
    
    while atual is not None: 
      print(" ↓ ")
      print(atual.valor)
      atual = atual.proximo
    
    print("None")
    
  
pilha = Pilha() 

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)

pilha.exibir()

print(pilha.verTopo())
print(pilha.desempilhar())
pilha.exibir()

pilha.empilhar(40)
pilha.exibir()