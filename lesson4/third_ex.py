""" Для чисел в пределах от 20 до 240 найти числа, 
кратные 20 или 21. Необходимо решить задание в одну строку. """

result = [itm for itm in range(20,240) if itm % 20 == 0 or itm % 21 == 0]

print(result)
