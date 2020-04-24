""" Создать текстовый файл (не программно), 
построчно записать фамилии сотрудников и величину 
их окладов. Определить, кто из сотрудников имеет 
оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
""" 
with open("lesson5_3.txt", 'r+' , encoding="utf-8") as file:
    str_list = ['Гончаров 15000\n','Акопов 25000\n','Иланова 19900\n']
    file.writelines(str_list)
    salary_sum = 0
    lines_count = 0
    for line in file:
        tmp = line.split(' ')
        lines_count += 1
        try:
            salary_sum += float(tmp[1])
            if float(tmp[1]) < 20000:
                print(tmp[0])
        except ValueError:
            print("В поле 'оклад' не число")
    print(f'Среднее значение оклада составляет {salary_sum/lines_count}')
 