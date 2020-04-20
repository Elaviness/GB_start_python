"""Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input(). """

print('Вводите элементы, нажимайте enter \nдля окончания ввода просто нажмите enter')
elem = input('')
elem_list = []
while elem:
        elem_list.append(elem)
        elem = input('')
print(elem_list)

for i in range(0, len(elem_list) -1,2):
    elem_list[i], elem_list[i+1] = elem_list[i+1], elem_list[i]


print(elem_list)
