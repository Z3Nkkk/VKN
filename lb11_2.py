import json
import math as m
sum = 0

el_1 = 0
el_2 = 0
el_3 = 0

def check (a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return(True)
def check_right (a, b, c):
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        return(True)
def check_equilateral (a, b, c):
    if a == b == c:
        return(True)
def check_isosceles (a, b, c):
    if a == b != c or a == c != b or c == b != a:
        return(True)

with open("tr.json", 'r') as json_file:
    tr = json.load(json_file) 
    
for len in tr['information']:
    
    if sum == 0:
        el_1 = len
        sum += 1
        
    elif sum == 1:
        el_2 = len
        sum += 1    
        
    elif sum == 2:
        el_3 = len
        sum += 1
        
        length_1 = el_1['length']
        length_2 = el_2['length']
        length_3 = el_3['length']
        
    elif sum == 3:
        el_1 = el_2
        el_2 = el_3
        el_3 = len
        
        length_1 = el_1['length']
        length_2 = el_2['length']
        length_3 = el_3['length']
        
    if sum == 3 and check(length_1, length_2, length_3) == True:
        
        name_1 = el_1['name']
        name_2 = el_2['name']
        name_3 = el_3['name']
        
        if check_right(length_1, length_2, length_3) == True:
            print(f'Трикутник {name_1}{name_2}{name_3} прямокутний')
        elif check_equilateral(length_1, length_2, length_3) == True:
            print(f'Трикутник {name_1}{name_2}{name_3} рівносторонній')
        elif check_isosceles(length_1, length_2, length_3) == True:
            print(f'Трикутник {name_1}{name_2}{name_3} рівнобедрений')
        else: 
            print(f'Трикутник {name_1}{name_2}{name_3} РІЗНОсторонній')
            
    elif sum == 3 and check(length_1, length_2, length_3) != True:
        name_1 = el_1['name']
        name_2 = el_2['name']
        name_3 = el_3['name']
        print(f'Трикутник {name_1}{name_2}{name_3} НЕ існує!')
