soma = contador = digito = 0
resto = 1
numero = int(input("Digite um número inteiro: "))

while resto != 0: 
     digito = numero % 10
     resto = numero // 10 
     soma += digito
     numero = resto

print(soma)