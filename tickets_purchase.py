# запрос на ввод количества билетов
N = int(input("Введите количество билетов: "))
S = 0 # общая стоимость билетов

# запрос возраста и рассчет стоимости для каждого билета
for i in range(1, N + 1):
    age = int(input("Введите возраст для билета №" + str(i) + ": "))
    if 18 <= age < 25:
        S += 990
    elif age >= 25:
        S += 1390
    else:
        S += 0  # меньше 18 лет
print("--------------------------")

# Общая стоимость
print("Общая стоимость билетов: {0} руб.".format(S))

# Рассчитаем доп.скидку от 3х человек
if N >= 3:
    print("Сумма скидки 10%: {0} руб.".format(S * 0.1))
    print("Общая стоимость билетов с учетом скидки 10%: {0} руб.".format(S - (S * 0.1)))