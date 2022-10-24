auto = {}
auto['BMW 5'] = '18000$'
auto['KIA RIO '] = '7500$'
auto['Lexus ES'] = '60000$'
auto['Honda Civic'] = '16000$'
auto['Toyota Camry'] = '30000$'
auto['Audi A6'] = '40000$'
auto['Volvo s80'] = '13000$'
n = 1

del (auto['Volvo s80'])
while n == 1:
     
    el = input ('Введіть назву авто ціну якого бажаєте дізнатись: ')

    if el in auto.keys():
        print (f'Ціна {el}: {auto[el]}')
        
        w = input(f'Бажаєте дізнатись ціну ще одного авто? ')
        if w =='так' or w == 'Так' or w == 'ТАК':
            n = 1
        else:
            n = 0
    else:
        print (f'Даних про {el} немає')
        bool = input (f'Бажаєте ввести дані для {el}? ')
        if bool == 'так' or bool == 'Так' or bool == 'ТАК':
            price = str(input(f'Введіть ціну для {el}: '))+'$'
            auto[el] = price
        else:
            n = 0
