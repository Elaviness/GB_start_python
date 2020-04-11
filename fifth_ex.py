revenue = input('Введите выручку: ')
while True:
    if revenue.isdigit():
        revenue = int(revenue)
        break
    else:
        revenue = input('Число введено некорректно, повторите попытку: ')

cost = input('Введите издержки: ')
while True:
    if str(cost).isdigit():
        cost = int(cost)
        break
    else:
        cost = input('Число введено некорректно, повторите попытку: ')

if revenue > cost:
    print('Финансовый результат компании: прибыль.')
    return_on_revenue = revenue - cost
    return_on_revenue_perc = return_on_revenue/revenue*100
    print(f'Рентабельность выручки составляет: {return_on_revenue_perc} %')
    number_of_employees = input('Введите количество сотрудников: ')
    while True:
        if str(number_of_employees).isdigit():
            number_of_employees = int(number_of_employees)
            break
        else:
            number_of_employees = input('Число введено некорректно, повторите попытку: ')
    return_per_emloy = return_on_revenue/number_of_employees
    print(f'Доход компании на сотрудника составляет {return_per_emloy}')
else: 
    print('Финансовый результат компании: убыток.')