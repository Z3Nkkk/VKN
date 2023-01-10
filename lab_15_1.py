import json
import tkinter as tk

dict = {}

with open("dict.json", "r",  encoding = 'utf8') as jsonfile:
    dict = json.load(jsonfile) 

def translate ():
    text_for_translate = entry1.get()
    for el in range(len(text_for_translate)):
        entry1.delete(0)
    entry1.insert(0, dict[text_for_translate])
    print(text_for_translate)



root = tk.Tk ()
label1 = tk.Label(root, text = "Введіть текст для перекладу", width="30", height = "2", font = "ubuntu 30")
entry1 = tk.Entry(root,  bd = "1", width = "30")
button1 = tk.Button(root, text = "Перевести", font = "ubuntu 10" , command = translate )
label1.grid(row=1, column=1, padx=10, pady=10)
entry1.grid(row=2,column=1, padx=0, pady=10)
button1.grid(row=3, column=1, padx=10, pady=20)

root.mainloop()

print()