digitosAdjacentes = False
digito = anterior = 0
resto = repetição = 1
numero = int(input("Digite um número inteiro: "))
if numero > 10:
    while resto != 0:
        digito = numero % 10
        if digito == anterior and repetição > 1:
            digitosAdjacentes = True
            break
        else:
            anterior = digito
            repetição += 1
        resto = numero // 10
        numero = resto

print(f'sim' if digitosAdjacentes else f'não')



