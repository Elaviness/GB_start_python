""" Создать (программно) текстовый файл, записать 
в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и 
выводить ее на экран. """
with open("lesson5_5.txt", 'w') as num_file:
    num_file.write('1 6 7 8 2 9 3 4')

with open("lesson5_5.txt", 'r') as num_file:
    str = num_file.read()
    num_list = str.split(' ')
    summary = 0
    try:
        for itm in num_list:
            summary += int(itm)
    except ValueError:
        print("Неккоректно введены данные файл.")
    print(summary)
    