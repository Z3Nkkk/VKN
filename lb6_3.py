#Варіант 6 
#3. Записати всі значення аргументу і функції у вкладений список (2 рядки). Вивести на екран вкладений список. Вивести на екран суму значень функції на проміжку. 
import math as m

x = float( input("введіть значення \033[1mx:\033[0m "))
a = float( input("\nвведіть \033[1ma:\033[0m "))
b = float( input("введіть \033[1mb:\033[0m "))
h = float( input("введіть значення кроку циклу: "))
y1 = 0
y = m.sin(x + m.pi) + m.cos(x + m.log( m.fabs(x), m.e ))

lst_x = []
lst_func = []
x1 = x

while x + a < x1 + b:
    
    y = m.sin(x + m.pi) + m.cos(x + m.log( m.fabs(x), m.e ))
    
    lst_x.append(x)
    lst_func.append(y)
    
    y1 = y1 + y
    x = x + h
        
lst = [ lst_x, lst_func ]
print (lst[0], "\n", lst[1], "\n") 
print ("Сума значень функції: ", round( y1, 2), "\n")
