"""  Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие 
лекционных, практических и лабораторных занятий по этому 
предмету и их количество. Важно, чтобы для каждого 
предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и 
общее количество занятий по нему. Вывести словарь на 
экран. """ 
with open("lesson5_6.txt", 'r', encoding='utf-8') as file:
    str = file.readlines()

tmp = []
for itm in str:
    itm = itm.split(':')
    tmp.append(itm)

str = tmp
for elem in str: # получаю подсписок
    idx = 0
    tmp = ''
    for itm in elem: # строка из списка
        sum = 0
        if idx % 2 == 1:
            for char in itm: # симовол из строки
                if char.isdigit():
                    tmp += char
                elif char == '(':
                    tmp += ' '
            tmp = tmp.split(' ')
            for num in tmp:
                if num.isdigit():
                    sum += int(num)    
        idx +=1
    elem[1] = sum
result = dict(str)
print(result)
