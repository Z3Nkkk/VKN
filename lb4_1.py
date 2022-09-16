#Варіант 6 
#1.Написати  програму  для  обчислення  значення  функції
import math

x = float( input("Введіть х  "))

a = math.sin( math.pow(x,2)) - math.tan(x-8)
b = math.log( math.fabs( math.pow( x, 3) - math.sin(x)), math.e)

y = a/b

print(y)
 