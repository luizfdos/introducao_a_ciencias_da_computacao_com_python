def éPrimo(x):
    fator = 2
    while x % fator != 0 and fator < x-1:
        fator += 1 
    if x % fator == 0 and x != 2:
        return False
    else: 
        return True

def n_primos(n):
    inicial = 2
    contador = 0
    while inicial <= n:
        if(éPrimo(inicial)):
            contador +=1
            inicial += 1
        else:
            inicial +=1
    return contador

print(n_primos(1))

