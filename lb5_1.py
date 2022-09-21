#Варіант 6 
#1. Написати програму, яка обчислюватиме значення функції у залежності від значення аргументу
import math as m

x = float(input("Введіть x: "))
 
def func_el1 ( x ):
    a = -9 + m.log( x, m.e) + m.sqrt(x)
    return(a)
def func_el2 ( x ):
    b = m.cos(x) + m.sin(2*x)
    return(b)
def func_el3 ( x ):
    c = m.fabs( -m.pow( x, 2) + 2*m.pow( x, -x) )
    return(c)

if x >= 5 :
    print ("Значення функції: ", round (func_el1(x), 2))
elif x > -0.5 and x < 5 :
    print ("Значення функції: ", round (func_el2(x), 2))
else:
    print ("Значення функції: ", round (func_el3(x), 2))
