import csv

with open('vologist.csv', 'r') as csv_file:
    csv_reader = csv.reader( csv_file )
    suma_po = 0
    num_of_days = 0
    pogoda_dict = {}
    more_list = []
    
    for row in csv_reader:
        for el in row: 
            num_of_days += 1
            if suma_po == 0:
                suma_po = int(el)
                pogoda_dict[num_of_days] = int(el)
            else:
                suma_po = suma_po + int(el)
                pogoda_dict[num_of_days] = int(el)
    aver_po = round(suma_po/num_of_days, 2)
    
    print(suma_po)
    print(aver_po)
    
    for el in pogoda_dict:
        if pogoda_dict[el] > aver_po:
            more_list.append(el)
    more = str(more_list)
    more = more.replace(']', '')
    more = more.replace('[', '')
    print(f'Вологість була вище {more} жовтня')
    