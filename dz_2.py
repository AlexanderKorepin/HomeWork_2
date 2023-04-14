# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def zadacha_1():
  number = abs(int(input('Введите число: ')))
  print(f"Список факториалов числа {number}:")
  for i in range(1, number+1):
    print(f"{factorial(i)}", end = "\t")

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
#Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
def zadacha_2():
    print("X | Y | Z | ¬(X ∧ Y) ∨ Z")
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f"{x} | {y} | {z} | {int(not(x and y) or z)}")
# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
def zadacha_3():
    str1 = input("Введите первую строку: ")
    str2 = input("Введите вторую строку: ")
    for i in str1:
        print(f"'{i}' = {count_characters(i, str2)}")
def count_characters(j, text):
    count = 0
    for i in text:
        if i == j:
            count += 1
    return count
# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
def zadacha_4():
    number = abs(int(input("Введите число N: ")))
    positions = 2
    first = list(range(-number, number + 1))
    first = shiftElementsRight(first,positions )
    print(first)

def shiftElementsRight(first, positions):
    return first[-positions:] + first[:-positions]
