def fizzbuzz(x):
    if x % 5 == 0:
        if x % 3 == 0:
            return "FizzBuzz"
        else: 
            return "Buzz"
    else: 
        if x % 3 == 0:
            return "Fizz"
        else: 
            return x


for i in range(1, 100):
    if fizzbuzz(i):
        print(fizzbuzz(i))
    else: 
        print(i)