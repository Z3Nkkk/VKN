import def_for_lb12_1

NUM_1 = int(input("Введіть перше ціле число: "))
NUM_2 = int(input("Введіть друге ціле число: "))
NUM_for_multiple = int(input("Введіть число для якого бажаєте дізнатись кратні: "))

if NUM_1 > 0 and NUM_2 > 0:
    divisors = def_for_lb12_1.divisor(NUM_1, NUM_2)
    print(f'Числа {divisors} спільні дільники для {NUM_1} і {NUM_2}')
else:
    print("Для заданих чисел неможливо знайти спільні дільники")
if NUM_for_multiple > 0 and def_for_lb12_1.multiple(NUM_for_multiple) != "":
    multiples = def_for_lb12_1.multiple(NUM_for_multiple)
    print(f'Числа {multiples} кратні числу {NUM_for_multiple}') 
else: 
    print("Для заданого числа не існує кратних")

    
    