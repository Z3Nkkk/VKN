#Варіант 6 
#1. Написати програму, яка обчислюватиме значення функції у залежності від значення аргументу
import math as m

x = float(input("Введіть x: "))
 
def func_el1 ( x1 ):
    a = -9 + m.log( x1, m.e) + m.sqrt(x1)
    return(a)
def func_el2 ( x2 ):
    b = m.cos(x2) + m.sin(2*x2)
    return(b)
def func_el3 ( x3 ):
    c = m.fabs( -m.pow( x3, 2) + 2*m.pow( x3, -x3) )
    return(c)

if x >= 5 :
    print ("Значення функції: ", round (func_el1(x), 2))
elif x > -0.5 :
    print ("Значення функції: ", round (func_el2(x), 2))
else:
    print ("Значення функції: ", round (func_el3(x), 2))
