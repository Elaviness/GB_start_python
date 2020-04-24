""" Создать текстовый файл (не программно), сохранить 
в нем несколько строк, выполнить подсчет количества 
строк, количества слов в каждой строке.
"""

#try:
with open("lesson5_2.txt", 'r+' , encoding="utf-8") as file:
    str_list = ['stroka_1\n','stroka_2\n','stroka_3333\n']
    file.writelines(str_list)
    lines_count = 0
    for line in file:
        lines_count += 1
        symbol_count = 0
        for symb in line:
            symbol_count += 1
        print(f'В {lines_count} строке {symbol_count} символов.')
#except 
