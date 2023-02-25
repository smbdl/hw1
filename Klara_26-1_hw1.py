# тут програма запрашивает пользователя ввести данные
print(f"Введите температуру в данной области:")
chyu = int(input("Чуй - "))
tls = int(input("Талас - "))
ik = int(input("Иссык-Куль - "))
nrn = int(input("Нарын - "))
osh = int(input("Ош - "))
jl = int(input("Джалал-Абад - "))
btkn = int(input("Баткен - "))

# далее вычисляет среднее арефметическое
sum_temperatures = chyu + tls + ik + nrn + osh + jl + btkn
amount_regions = 7
average_temperature = sum_temperatures / amount_regions
# и результат
print(f"Средний показатель температуры воздуха по КР на сегодня {round(average_temperature, 1)} °C.")


# это альтернатива спустя месяц обучения
# regions = ['chui', 'talas', 'naryn', 'batken', 'osh', 'ik', 'jlbd']
# answer = [int(input(f'temperature in {i} is ')) for i in regions]
# print(f'temperature in kg is {round(sum(answer) / len(regions), 2)}')
