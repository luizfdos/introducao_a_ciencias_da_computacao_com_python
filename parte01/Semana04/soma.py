i = soma = valor = 0
sumlength = int(input("Digite quantos números quer somar: "))
while i < sumlength:
    valor = int(input("Digite um valor a ser somado: "))
    soma += valor
    i += 1

print(f'A soma dos valores digitados é: {soma}')