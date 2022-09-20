#Варіант 6 
#2.Написати  програму,  яка  обчислює  значення  виразу
import math as m

t = float( input("Введіть t:  "))
n = float( input("Введіть n:  "))
k = float( input("Введіть k:  "))

def func1 (n):
    x = m.pi*n + m.pi/7
    return (x)

def func2 (k, n):
    pow = k/t + n
    return (pow)    
 
s = 4.17*m.sqrt(t) - m.sin(func1 (n)) + m.pow( m.e, func2 (k, n))

print(round(s,2))
 
