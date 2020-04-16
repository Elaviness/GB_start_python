
press_key = input('Введите любой символ для старта: ')
i = 0
goods = []
goods_tmp = []
goods_analytic = {}

while press_key:
    i +=1
    tmp = input('Введите через пробел название, стоимость, количество и единицу измерения товара: ')
    tmp = tmp.split(' ')
    goods.append((i, {"название": tmp[0], "цена": tmp[1], "количество": tmp[2], "ед": tmp[3]}))
    press_key = input('Для завершения ввода нажмите Enter. Для продолжения любой другой символ: ')
    goods_tmp.append(tmp)

print(goods)
names = []
prices = []
counts = []
units = []
for itm in goods_tmp:
    names.append(itm[0])
    prices.append(itm[1])
    counts.append(itm[2])
    units.append(itm[3])

goods_analytic.update({"название": names, "цена": prices, "количество": counts, "ед": units})
print(goods_analytic)

