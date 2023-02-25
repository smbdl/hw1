countries = {'kg': {"red", "yellow"},
             "rus": {"white", 'blue', 'red'},
             'tur': {'white', 'red'},
             'usa': {'white', 'blue', 'red'},
             'kz': {'blue', 'yellow'}
             }

while True:
    color = input('write a color: '.lower()).split()
    if color == ['stop'.lower()]:
        print('program stopped.')
        break
    for i in countries:
        color = set(color)
        if not color.difference(countries[i]):
            print(i)
    else:
        print('no country with that color.')
