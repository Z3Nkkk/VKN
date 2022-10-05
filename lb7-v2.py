list = sorted(input("Веведіть: "))

i = 0
j = 1
count = 1 

for x in list:

    if(list[i]==list[j]):
        count += 1
    else:
        print(f'"{x}" - частота {round(count/len(list), 2)}')
        count = 1
        
    if (j == len(list)-1): 
        print(f'"{list[j]}" - частота {round(count/len(list), 2)}')
        break
    i += 1
    j += 1