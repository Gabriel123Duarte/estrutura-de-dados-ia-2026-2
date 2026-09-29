def exibir_arvore(raiz):
  if raiz is None:
    print("Árvore vazia")
    return

  linhas, _, _, _ = _montar_arvore(raiz)

  for linha in linhas:
    print(linha.rstrip())


def _montar_arvore(no):
  valor = str(no.valor)
  largura_valor = len(valor)

  # Nó folha
  if no.esquerda is None and no.direita is None:
    return [valor], largura_valor, 1, largura_valor // 2

  # Apenas filho à esquerda
  if no.direita is None:
    linhas_esq, largura_esq, altura_esq, meio_esq = (
      _montar_arvore(no.esquerda)
    )

    primeira_linha = (
      " " * (meio_esq + 1)
      + "_" * (largura_esq - meio_esq - 1)
      + valor
    )

    segunda_linha = (
      " " * meio_esq
      + "/"
      + " " * (
        largura_esq
        - meio_esq
        - 1
        + largura_valor
      )
    )

    linhas_esq = [
      linha + " " * (largura_valor)
      for linha in linhas_esq
    ]

    return (
      [primeira_linha, segunda_linha] + linhas_esq,
      largura_esq + largura_valor,
      altura_esq + 2,
      largura_esq + largura_valor // 2
    )

  # Apenas filho à direita
  if no.esquerda is None:
    linhas_dir, largura_dir, altura_dir, meio_dir = (
      _montar_arvore(no.direita)
    )

    primeira_linha = (
      valor
      + "_" * meio_dir
      + " " * (largura_dir - meio_dir)
    )

    segunda_linha = (
      " " * largura_valor
      + "\\"
      + " " * (largura_dir - 1)
    )

    linhas_dir = [
      " " * largura_valor + linha
      for linha in linhas_dir
    ]

    return (
      [primeira_linha, segunda_linha] + linhas_dir,
      largura_valor + largura_dir,
      altura_dir + 2,
      largura_valor // 2
    )

  # Dois filhos
  linhas_esq, largura_esq, altura_esq, meio_esq = (
    _montar_arvore(no.esquerda)
  )

  linhas_dir, largura_dir, altura_dir, meio_dir = (
    _montar_arvore(no.direita)
  )

  primeira_linha = (
    " " * (meio_esq + 1)
    + "_" * (largura_esq - meio_esq - 1)
    + valor
    + "_" * meio_dir
    + " " * (largura_dir - meio_dir)
  )

  segunda_linha = (
    " " * meio_esq
    + "/"
    + " " * (
      largura_esq
      - meio_esq
      - 1
      + largura_valor
      + meio_dir
    )
    + "\\"
    + " " * (largura_dir - meio_dir - 1)
  )

  # Igualar alturas das duas subárvores
  if altura_esq < altura_dir:
    linhas_esq += [
      " " * largura_esq
    ] * (altura_dir - altura_esq)

  elif altura_dir < altura_esq:
    linhas_dir += [
      " " * largura_dir
    ] * (altura_esq - altura_dir)

  linhas = []

  for esquerda, direita in zip(
    linhas_esq,
    linhas_dir
  ):
    linhas.append(
      esquerda
      + " " * largura_valor
      + direita
    )

  return (
    [primeira_linha, segunda_linha] + linhas,
    largura_esq + largura_valor + largura_dir,
    max(altura_esq, altura_dir) + 2,
    largura_esq + largura_valor // 2
  )