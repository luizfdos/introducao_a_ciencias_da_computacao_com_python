# Verificar se número tem dois digitos adjacentes iguais 
# 1239921 digitos adjacentes iguais '99'
digitosAdjacentes = False
digito = anterior = 0
resto = 1
numero = int(input("Digite um número para verificar se ele possui digitos adjacentes: "))
numerooriginal = numero
while resto != 0:
    digito = numero % 10
    if digito == anterior :
        digitosAdjacentes = True
        break
    else:
        anterior = digito
    resto = numero // 10
    numero = resto

print(f'O numero {numerooriginal} possui digitos adjacentes' if digitosAdjacentes else f'O numero não {numerooriginal} possui digitos adjacentes')



