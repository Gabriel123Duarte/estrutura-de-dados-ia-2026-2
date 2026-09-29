from visualizador_arvore import exibir_arvore

class NoArvore:
  def __init__(self, valor):
    self.valor = valor
    self.esquerda = None
    self.direita = None

    # NOVO — altura do nó para o balanceamento AVL
    self.altura = 1


class ArvoreBusca:
  def __init__(self):
    self.raiz = None


  # NOVO — retorna a altura de um nó
  def altura(self, no):
    if no is None:
      return 0

    return no.altura


  # NOVO — recalcula a altura de um nó
  def atualizar_altura(self, no):
    if no is None:
      return

    altura_esquerda = self.altura(no.esquerda)
    altura_direita = self.altura(no.direita)

    no.altura = 1 + max(
      altura_esquerda,
      altura_direita
    )


  # NOVO — calcula o fator de balanceamento
  def fator_balanceamento(self, no):
    if no is None:
      return 0

    return (
      self.altura(no.esquerda)
      - self.altura(no.direita)
    )


  # NOVO — rotação à direita
  def rotacao_direita(self, no):
    if no is None or no.esquerda is None:
      return no

    nova_raiz = no.esquerda
    subarvore = nova_raiz.direita

    nova_raiz.direita = no
    no.esquerda = subarvore

    # NOVO — atualizar as alturas
    self.atualizar_altura(no)
    self.atualizar_altura(nova_raiz)

    return nova_raiz


  # NOVO — rotação à esquerda
  def rotacao_esquerda(self, no):
    if no is None or no.direita is None:
      return no

    nova_raiz = no.direita
    subarvore = nova_raiz.esquerda

    nova_raiz.esquerda = no
    no.direita = subarvore

    # NOVO — atualizar as alturas
    self.atualizar_altura(no)
    self.atualizar_altura(nova_raiz)

    return nova_raiz


  # NOVO — rotação esquerda-direita
  def rotacao_esquerda_direita(self, no):
    if no is None or no.esquerda is None:
      return no

    no.esquerda = self.rotacao_esquerda(
      no.esquerda
    )

    return self.rotacao_direita(no)


  # NOVO — rotação direita-esquerda
  def rotacao_direita_esquerda(self, no):
    if no is None or no.direita is None:
      return no

    no.direita = self.rotacao_direita(
      no.direita
    )

    return self.rotacao_esquerda(no)


  # NOVO — identifica o tipo de desequilíbrio
  # e realiza a rotação necessária
  def balancear(self, no):
    if no is None:
      return None

    self.atualizar_altura(no)

    fator = self.fator_balanceamento(no)

    # Desbalanceamento para a esquerda
    if fator > 1:

      # Caso LL
      if self.fator_balanceamento(no.esquerda) >= 0:
        print("Caso LL no nó", no.valor)

        return self.rotacao_direita(no)

      # Caso LR
      else:
        print("Caso LR no nó", no.valor)

        return self.rotacao_esquerda_direita(no)


    # Desbalanceamento para a direita
    if fator < -1:

      # Caso RR
      if self.fator_balanceamento(no.direita) <= 0:
        print("Caso RR no nó", no.valor)

        return self.rotacao_esquerda(no)

      # Caso RL
      else:
        print("Caso RL no nó", no.valor)

        return self.rotacao_direita_esquerda(no)


    return no


  # NOVO — percorre o caminho de baixo para cima
  # atualizando alturas e corrigindo desequilíbrios
  def rebalancear_caminho(self, caminho):

    for i in range(len(caminho) - 1, -1, -1):

      no = caminho[i]

      nova_raiz = self.balancear(no)

      if i == 0:
        self.raiz = nova_raiz

      else:
        pai = caminho[i - 1]

        if pai.esquerda is no:
          pai.esquerda = nova_raiz

        elif pai.direita is no:
          pai.direita = nova_raiz


  # INSERÇÃO
  def inserir(self, valor):
    novo = NoArvore(valor)

    if self.raiz is None:
      self.raiz = novo
      return

    atual = self.raiz

    # NOVO — guardar o caminho percorrido
    # para balancear depois da inserção
    caminho = []

    while True:

      # NOVO
      caminho.append(atual)

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

    # NOVO — verificar o balanceamento
    # de baixo para cima
    self.rebalancear_caminho(caminho)


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

    # NOVO — guardar o caminho percorrido
    # para balancear depois da remoção
    caminho = []

    # 1. Procurar o nó que será removido
    while atual is not None and atual.valor != valor:

      # NOVO
      caminho.append(atual)

      pai = atual

      if valor < atual.valor:
        atual = atual.esquerda
      else:
        atual = atual.direita

    if atual is None:
      print("Valor não encontrado:", valor)
      return

    # 2. Caso o nó tenha no máximo um filho
    filho = None

    if atual.esquerda is None:
      filho = atual.direita

    elif atual.direita is None:
      filho = atual.esquerda

    # 3. Caso o nó tenha dois filhos
    else:

      # NOVO — este nó também pode ter
      # sua altura alterada
      caminho.append(atual)

      # Encontrar o sucessor:
      # menor nó da subárvore direita
      pai_sucessor = atual
      sucessor = atual.direita

      while sucessor.esquerda is not None:

        # NOVO — guardar também o caminho
        # percorrido até o sucessor
        caminho.append(sucessor)

        pai_sucessor = sucessor
        sucessor = sucessor.esquerda

      # Copiar o valor do sucessor
      atual.valor = sucessor.valor

      # Agora removeremos o sucessor original
      atual = sucessor
      pai = pai_sucessor

      # O sucessor não tem filho à esquerda,
      # mas pode ter filho à direita
      filho = sucessor.direita

    # 4. Atualizar a referência do pai
    if pai is None:
      # O nó removido era a raiz
      self.raiz = filho

    elif pai.esquerda is atual:
      pai.esquerda = filho

    else:
      pai.direita = filho

    # NOVO — após a remoção, verificar
    # o balanceamento de baixo para cima
    if caminho:
      self.rebalancear_caminho(caminho)

    elif self.raiz is not None:
      self.atualizar_altura(self.raiz)


    if self.raiz is None:
      print("Árvore vazia")
      return

    print(f"RAIZ: {self.raiz.valor}")

    # Cada item guarda: nó, prefixo e se é o último filho
    pilha = []

    filhos = []

    if self.raiz.esquerda is not None:
      filhos.append(("E", self.raiz.esquerda))

    if self.raiz.direita is not None:
      filhos.append(("D", self.raiz.direita))

    # Empilhar da direita para a esquerda
    for i in range(len(filhos) - 1, -1, -1):
      lado, filho = filhos[i]
      ultimo = i == len(filhos) - 1
      pilha.append((filho, "", lado, ultimo))

    while pilha:
      atual, prefixo, lado, ultimo = pilha.pop()

      if ultimo:
        conector = "└── "
        novo_prefixo = prefixo + "    "
      else:
        conector = "├── "
        novo_prefixo = prefixo + "│   "

      print(prefixo + conector + lado + ": " + str(atual.valor))

      filhos = []

      if atual.esquerda is not None:
        filhos.append(("E", atual.esquerda))

      if atual.direita is not None:
        filhos.append(("D", atual.direita))

      # A pilha é LIFO, então empilhamos
      # em ordem inversa para imprimir E antes de D
      for i in range(len(filhos) - 1, -1, -1):
        lado_filho, filho = filhos[i]
        ultimo_filho = i == len(filhos) - 1

        pilha.append((
          filho,
          novo_prefixo,
          lado_filho,
          ultimo_filho
        ))


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