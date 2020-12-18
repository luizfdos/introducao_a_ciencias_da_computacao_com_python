n = int(input('Digite um numero inteiro: (digite 0 para parar)'))
array = []
while n != 0:
    array.append(n)
    n = int(input('Digite um numero inteiro: (digite 0 para parar)'))
lenght = len(array)-1
while lenght >= 0: 
    print(array[lenght], end=", ")
    lenght -= 1

# reverse_array = []
# initial = len(array)-1
# while initial >=0: 
#     reverse_array.append(array[initial])
#     initial -= 1

# print(reverse_array)


