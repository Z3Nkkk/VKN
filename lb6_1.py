#Варіант 6 
#1. Протабулювати  функцію  в  діапазоні  [a;b]  з  кроком  h  за  допомогою циклу з параметром. Значення a, b, h вводяться з клавіатури.
import math as m

x = float( input("введіть значення \033[1mx:\033[0m "))
a = float( input("\nвведіть \033[1ma:\033[0m "))
b = float( input("введіть \033[1mb:\033[0m "))
h = float( input("введіть значення кроку циклу: "))

b = x + b

for i in range(100):
    
    y = m.sin(x + m.pi) + m.cos(x + m.log( m.fabs(x), m.e ))
    print ( y, "\n")
    x = x + h
    
    if a + x > b:
        break

