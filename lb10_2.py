import os

file = input("Введіть назву файла який бажаєте знайти: ")
disk = input("Введіть диск на якому бажаєте шукати файл: ")
check = 0

folder_list = os.listdir(f'{disk}:\\')
folder_list.append('Users\\JaT\\Desktop')

for el in folder_list:
    file_path = f'{disk}:\\{el}\\{file}'
    file_alt_path = f'{disk}:\\{file}'
    
    if os.path.exists(file_path):
        print(f'Файл знайдено {file_path}')
        check = 1
    elif el == file:
        print(f'Файл знайдено {file_alt_path}')
        folder_list.remove(el)
        check = 1
        
if check == 0:
    print(f'Файл не знайдено!')
    
    
    

