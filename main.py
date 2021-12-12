print('Отрезок\n')

# Программа считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.

MULTIPLE = 5

number_first = int(input('Введите начало отрезка: '))
number_last = int(input('Введите конец отрезка: '))

counter_summa = 0
counter_range = 0

for number in range(number_first - number_first // MULTIPLE + 1, number_last + 1, MULTIPLE):
  counter_summa += number
  counter_range += 1

medium = counter_summa / counter_range

print(medium)
