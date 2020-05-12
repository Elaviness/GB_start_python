""" Создать (не программно) текстовый файл со 
следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл 
на чтение и считывающую построчно данные. При этом 
английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый 
файл. """
tmp = []

with open("lesson5_4_1.txt", 'r', encoding='utf-8') as file:
    for line in file:
        tmp.append(line)

translate = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре' }

with open("lesson5_4_2.txt", 'a', encoding='utf-8') as file:
    for itm in tmp:
        line = itm.split(' ')
        num_from_line = int(line[2][:1])
        new_str = translate.get(num_from_line)   
        file.write(str(new_str + ' ' + line[1] + ' ' + line[2]))
