def éPrimo(k):
    divisores = 0
    divisor = k 
    verificaDivisibilidade = 0
    while divisor >= 1:
        verificaDivisibilidade = k % divisor
        if verificaDivisibilidade == 0:
            divisor -= 1
            divisores += 1
        else: 
            divisor -= 1

    return True if divisores == 2 else False

def maior_primo(x):
    while x >= 2: 
        if éPrimo(x):
            return x
        else: 
            x -= 1
