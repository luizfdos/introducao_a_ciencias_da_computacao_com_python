def éHipotenusa(n):
    n_squared = n * n
    a = 1  
    b = 1
    while a < n:
        while b < n:
            if n_squared == (a*a)+(b*b):
                return True
            b += 1
        a += 1
        b = a

def soma_hipotenusas(n):
    soma = 0
    inicial = 1
    while inicial <= n:
        if éHipotenusa((inicial*inicial)):
            soma += inicial
            inicial += 1
        else:
            inicial += 1
    return soma


