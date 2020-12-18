def soma_matrizes(m1, m2):
    dimensao1 = f"{len(m1)}X{len(m1[0])}"
    dimensao2 = f"{len(m2)}X{len(m2[0])}"
    if dimensao1 != dimensao2:
        return False
    linhas = len(m1)
    colunas = len(m1[0])
    soma_das_matrizes = []

    for j in range(linhas):
        linha = []
        for i in range(colunas):
            linha.append(0)
        soma_das_matrizes.append(linha)

    for coluna in range(colunas):
        for linha in range(linhas):
            soma_das_matrizes[linha][coluna] = m1[linha][coluna] + m2[linha][coluna]

    return soma_das_matrizes
