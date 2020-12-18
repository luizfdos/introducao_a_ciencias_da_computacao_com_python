from math import floor

def fatorial(x):
    multiplicação = 1
    while x > 0:
        multiplicação *= x
        x -= 1
    return multiplicação

def coeficienteBinomial (n, k):
    return fatorial(n) / (fatorial(n-k) * fatorial(k))

numerador = int(input("Digite o numerador: "))
denominador = int(input("Digite o denominador: "))

print(floor(coeficienteBinomial(numerador, denominador)))
