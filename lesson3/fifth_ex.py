"""  Программа запрашивает у пользователя строку чисел, 
разделенных пробелом. При нажатии Enter должна 
выводиться сумма чисел. Пользователь может продолжить 
ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже 
подсчитанной сумме. Но если вместо числа вводится 
специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной 
ранее сумме и после этого завершить программу. """

def adder(numbers, result):
    for i in numbers:
        try:
            if i == '/':
                print('Был получен конечный символ.')
                break
            else:
                result += int(i)
        except ValueError:
            print('Некоректное число или конечный символ')
            return
    return result        

result = 0        
while True:
    numbers = input('Введите строку чисел через пробел: ').split(' ')
    result = adder(numbers, result)
    print(result)