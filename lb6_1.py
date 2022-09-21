#Варіант 6 
#1. Протабулювати  функцію  в  діапазоні  [a;b]  з  кроком  h  за  допомогою циклу з параметром. Значення a, b, h вводяться з клавіатури.
import math as m

x = float( input("введіть значення \033[1mx:\033[0m "))
a = int( input("\nвведіть \033[1ma:\033[0m "))
b = int( input("введіть \033[1mb:\033[0m "))
h = int( input("введіть значення кроку циклу: "))
 

for i in range(a, b, h):
    y = m.sin(x + m.pi) + m.cos(x + m.log( m.fabs(x), m.e ))
    print ( y, "\n")
    x = x + h

