def conta_letras(frase, contar="vogais"):
  total = 0
  if contar == "vogais":
    for i in range(len(frase)):
      if frase[i].lower() in ("aeiou"):
        total += 1
    return total
  if contar == "consoantes":
    for i in range(len(frase)):
      if frase[i].lower() in ("bcdfghjklmnprstvwxyz"):
        total += 1
    return total
