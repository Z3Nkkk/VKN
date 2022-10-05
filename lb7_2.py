filepath = input("Введіть шлях до файла  ")
elem = filepath.split("/")
path_elem = elem[:-1]

for x in path_elem:
    print( x )

print(f"\n\033[1m{elem[-1]}\033[0m")







