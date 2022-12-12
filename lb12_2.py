import def_for_lb12_2
print("1 - Зашифрувати або Розшифрувати; 2 - Зашифрувати і одразу розшифрувати")
action = int(input("Введіть число яке відповідає бажаній дії: "))
txt_for_cipher = input('Введіть текст для шифрування/дешифрування: ')

cipher = def_for_lb12_2.cipher(txt_for_cipher)

print (f'\n{cipher}\n')
    
if action == 2:
    print(def_for_lb12_2.cipher(cipher), "\n")