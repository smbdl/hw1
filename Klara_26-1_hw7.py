def nearest(values: list, num: int):
    lst = sorted(values, key=lambda i: (abs(num - i)))
    tuple = (num, lst)
    return tuple


def ind(lst):
    while True:
        try:
            indx = input('Index: ')
            if indx == 'stop':
                break
            print(lst[int(indx)])
        except:
            print(f'Numbers only from 0 to {len(lst) - 1}')


values = [1, 5, 10]
power = list(map(lambda x: x * x, values))
print(power)

values = list(range(1, 11))
new = list(filter(lambda x: x % 5 == 0, values))
print(new)
