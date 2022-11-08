file = open('story.txt', 'r')
file_reader = file.read()

golosni = 'AaEeIiOoUuYy'
prugolosni = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz'
nums = '1234567890'
gol_count = 0
prugol_count = 0
nums_count = 0


for el in file_reader:
    if el in golosni:
        gol_count += 1
    if el in prugolosni:
        prugol_count += 1
    if el in nums:
        nums_count += 1
print(f'Кількість букв що позначають голосні звуки: {gol_count}\n\
Кількість букв що позначають приголосні звуки: {prugol_count}\n\
Кількість цифр: { nums_count }')
 
file.close()
