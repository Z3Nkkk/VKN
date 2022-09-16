#Варіант 6 
#2.Написати  програму,  яка  обчислює  значення  виразу
import math as m

t = float( input("Введіть t:  "))
n = float( input("Введіть n:  "))
k = float( input("Введіть k:  "))

s = 4.17*m.sqrt(t) - m.sin( m.pi*n + m.pi/7) + m.pow( m.e, k/t + n)

print(round(s,2))
 