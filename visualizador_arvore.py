def exibir_arvore(raiz):
  if raiz is None:
    print("Árvore vazia")
    return

  print(f"RAIZ: {raiz.valor}")

  pilha = []
  filhos = []

  if raiz.esquerda is not None:
    filhos.append(("E", raiz.esquerda))

  if raiz.direita is not None:
    filhos.append(("D", raiz.direita))

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

    print(
      prefixo
      + conector
      + lado
      + ": "
      + str(atual.valor)
    )

    filhos = []

    if atual.esquerda is not None:
      filhos.append(("E", atual.esquerda))

    if atual.direita is not None:
      filhos.append(("D", atual.direita))

    for i in range(len(filhos) - 1, -1, -1):
      lado_filho, filho = filhos[i]
      ultimo_filho = i == len(filhos) - 1

      pilha.append((
        filho,
        novo_prefixo,
        lado_filho,
        ultimo_filho
      ))