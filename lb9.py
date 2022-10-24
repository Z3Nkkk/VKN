import math as m
list_dot1 = []
list_dot2 = []
list_dot3 = []
dist_dot = []

def dot_coordinate(coord):
    n=1
    for i in range(3):
        coord_value = float(input(f'введіть {coord} для {n} точки: '))
        if n == 1 :
            list_dot1.append( coord_value )
        elif n == 2 :  
            list_dot2.append( coord_value )
        elif n == 3 :  
            list_dot3.append( coord_value )              
        n = n + 1
    return()

dot_coordinate("x")
dot_coordinate("y")
dot_coordinate("z")

(x1, y1, z1) = dot1 = tuple(list_dot1)
(x2, y2, z2) = dot2 = tuple(list_dot2)
(x3, y3, z3) = dot3 = tuple(list_dot3)

ab = round( m.sqrt( m.pow(x1, 2) + m.pow(y1, 2) + m.pow(z1, 2) ), 2)
dist_dot.append(ab)
bb = round( m.sqrt( m.pow(x2, 2) + m.pow(y2, 2) + m.pow(z2, 2) ), 2)
dist_dot.append(bb)
cb = round( m.sqrt( m.pow(x3, 2) + m.pow(y3, 2) + m.pow(z3, 2) ),2 )
dist_dot.append(cb)

(a, b, c) = dotname = tuple(dist_dot)
print(f'Відстань від точок до центра координат: {dotname}')

if a < b and a < c and b > c:
    print(f'Точка 1 найближча: {a} до початку координат')
    print(f'Точка 2 найвіддаленіша: {b} до початку координат')
elif a < b and a < c and c > b:
    print(f'Точка 1 найближча: {a} до початку координат')
    print(f'Точка 3 найвіддаленіша: {c} до початку координат')
    
elif b < a and b < c and a > c:
    print(f'Точка 2 найближча: {b} до початку координат')
    print(f'Точка 1 найвіддаленіша: {a} до початку координат')
elif b < a and b < c and c > a:
    print(f'Точка 2 найближча: {b} до початку координат')
    print(f'Точка 3 найвіддаленіша: {c} до початку координат')
    
elif c < a and c < b and a > b:
    print(f'Точка 3 найближча: {c} до початку координат')
    print(f'Точка 1 найвіддаленіша: {a} до початку координат')
elif c < a and c < b and b > a:
    print(f'Точка 3 найближча: {c} до початку координат')
    print(f'Точка 2 найвіддаленіша: {b} до початку координат')
else:
    print("Точки на однаковому віддаленні від початку координат")
