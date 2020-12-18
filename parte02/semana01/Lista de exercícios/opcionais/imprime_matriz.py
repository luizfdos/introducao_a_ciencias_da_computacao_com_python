def imprime_matriz(matriz):
  rows = len(matriz)
  columns = len(matriz[0])

  for row in range(rows):
    for column in range(columns):
      if column + 1 < columns:
        print(matriz[row][column], end=" ")
      else: 
        print(matriz[row][column])
  return 


minha_matriz = [[1, 2, 3], [4, 5, 6]]
imprime_matriz(minha_matriz)