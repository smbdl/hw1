a = 1
b = 100
attempts = 0
list_attempts = []
while True:
    current = (a + b) // 2
    is_right = input(f'Ваше число {current}').lower()
    attempts += 1
    list_attempts.append(current)
    print(list_attempts)
    print(f'Количество попыток: {attempts}')
    if is_right == "да":
        print('Конец')
        break
    elif is_right == "больше":
        a = current
    elif is_right == "меньше":
        b = current
    elif is_right != "больше" or is_right != 'меньше':
        print("Отвечайте только да, больше или меньше.")
    with open('results.txt', 'w', encoding='UTF-8') as file:
        file.write(f'Количество попыток: {attempts}\nСписок попыток:'
                   f' {list_attempts}\nЗагаданное число: {current}')