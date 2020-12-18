i = valor = 0
produto = 1
length = int(input("Digite quantos números quer multiplicar: "))
while i < length:
    valor = int(input("Digite um valor a ser somado: "))
    produto *= valor
    i += 1

print(f'O produto dos valores digitados é: {produto}')