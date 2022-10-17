# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Введите число: ")
s = 0 
res =  list(map(int, [ch for ch in number if ch.isdigit()]))
for el in res:
    s += el
print(s)    
