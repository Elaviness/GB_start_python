n = input('Введите Ваше число: ')

while True:
    if n.isdigit():
        n = int(n)
        break
    else:
        n = input('Вы ввели не число, повторите попытку: ')

result = n + (n*10+n) + (n*100+n*10+n)
print('Расчет по формуле n+nn+nnn: {}+{}+{}={}'.format(n, n*10+n, n*100+n*10+n, result))
