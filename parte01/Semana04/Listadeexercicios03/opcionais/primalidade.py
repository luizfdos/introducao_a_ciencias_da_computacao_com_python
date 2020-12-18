numero = int(input('Digite um número inteiro: '))
divisores = 0
divisor = numero 
verificaDivisibilidade = 0
while divisor >= 1:
    verificaDivisibilidade = numero % divisor
    if verificaDivisibilidade == 0:
        divisor -= 1
        divisores += 1
    else: 
        divisor -= 1

print('primo' if divisores == 2 else 'não primo' )
