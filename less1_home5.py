viruchka = int(input('Введите значение выручки: '))
izderzhki = int(input('Введите значение издержек: '))

if viruchka > izderzhki:
     print('Финансовый результат - ПРИБЫЛЬ')
     rentab = (viruchka-izderzhki)/viruchka
     print(f'Рентабельность выручки: {rentab}')
     chislennost = int(input('Введите численность сотрудников: '))
     pribil_na_sotr = (viruchka - izderzhki)/chislennost
     print(f'Прибыль на одного сотрудника: {pribil_na_sotr}')
else:
    print('Финансовый результат - УБЫТОК или отсутствует')