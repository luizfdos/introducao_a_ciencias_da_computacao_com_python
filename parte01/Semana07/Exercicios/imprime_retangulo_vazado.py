largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
larguraInicial = largura
alturaInicial = altura
inicial = 0
while altura > 0:
    if inicial == 0:
        while largura > 0:
            print('#',end='')
            largura -= 1
    else: 
        if inicial > 0 and inicial < alturaInicial-1:
            vazio = larguraInicial - 2
            print('#', ((vazio-2) * ' '), '#', end='')
        else: 
            while largura > 0:
                print('#',end='')
                largura -= 1
    print()
    inicial += 1
    largura = larguraInicial
    altura -=1
