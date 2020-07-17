# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.



chislo = int(input('Введите целое положительное число: '))
max_cifra = chislo%10
chislo = chislo//10
while chislo > 0:
    if chislo%10 > max_cifra:
        max_cifra = chislo%10
    chislo = chislo//10
print(max_cifra)
