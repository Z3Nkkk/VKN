import random

inp = input("ВВедіть значення для множини через кому: ")
x = inp.split(",")
user = list(x)
countable = []

for el in user:
    countable.append(round(float(el),1))
D = set(countable)

C = set()
edge = random.randint(1, 30)
for i in range (edge):
    elem = round( random.uniform(0.7, 150), 1 )
    C.add( elem )

sum = C|D
dif = D - C

print(C)
print(sum)
print(dif)