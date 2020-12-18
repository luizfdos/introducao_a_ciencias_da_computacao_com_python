decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))
valor = 1
while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

print("A sequencia está em ordem decrescente!" if decrescente else "A sequência não está em ordem decrescente!")