'''def имя_функции():
    действие'''
    
'''def sleep():
    print("I'm sleeping...")
    
sleep()'''

'''def sleep():
    ls = "I'm sleeping..."
    print(ls)
    
sleep()'''


'''def say_world(Slovo):
    print(Slovo)
    
say_world('Cat')'''


'''def say_word(Slovo):
    return Slovo
    
new_word = say_word('Dog')

print(say_word('Cat'))
print(new_word)'''


'''def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))'''

'''fib1 = fib2 = 1

print(fib1, fib2, end=' ')

for i  in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end = ' ')'''


'''fib1 = fib2 = 1

n = int(input('Введите число: '))
n = n - 2

while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
    
    print(fib2)'''
    


a = int(input('Номер элемента ряда фибоначчи: '))

def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(a)))

























