def maior_elemento(lista):
  maior = menor = lista[0]
  for i in range(0, len(lista)):
    if lista[i] > maior:
      maior = lista[i]
  return maior
