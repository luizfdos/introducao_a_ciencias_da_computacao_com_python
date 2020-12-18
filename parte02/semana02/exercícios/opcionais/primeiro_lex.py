def primeiro_lex(lista):
  primeiro = lista[0]
  for i in range(len(lista)):
    if lista[i] < primeiro:
      primeiro = lista[i]
  return primeiro
