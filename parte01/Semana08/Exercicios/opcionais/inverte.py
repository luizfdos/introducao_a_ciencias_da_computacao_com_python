n = int(input('Digite um número: '))
array = []
while n != 0:
    array.append(n)
    n = int(input('Digite um número: '))
lenght = len(array)-1
while lenght >= 0: 
    print(array[lenght])
    lenght -= 1