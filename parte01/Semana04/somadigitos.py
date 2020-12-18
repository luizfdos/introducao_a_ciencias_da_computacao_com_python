soma = contador = digito = 0
resto = 1
numero = int(input("Digite o número que deseja saber a soma dos digitos: "))

while resto != 0: 
     digito = numero % 10
     resto = numero // 10 
     soma += digito
     numero = resto

print(f'A soma dos digitos é {soma}')

     