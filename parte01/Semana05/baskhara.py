import math


def delta(a, b,c):
    return b ** 2 - 4 * a * c


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)


def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d < 0:
            print("esta equação não possui raízes reais")
    else:
        if d == 0: 
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            print(f"a raiz desta equação é {raiz1}")
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            if raiz1 > raiz2:
                print(f"as raízes da equação são {raiz2} e {raiz1}")
            else: 
                print(f"as raízes da equação são {raiz1} e {raiz2}")
            
main()