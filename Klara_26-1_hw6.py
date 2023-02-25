def odd_even(number: int):
    if type(number) == int:
        if number % 2 == 0:
            return True
        return False
    return None


def check(sentence: str):
    if sentence[0].istitle() and sentence.endswith('.'):
        print(sentence)
    else:
        print("Write correctly.")


def average(*args):
    return int((sum(args) / len(args)))


def nearest(values: list, num: int):
    difference = [abs(i - num) for i in values]
    return f'{values} {num} == {values[difference.index(min(difference))]}'


print(nearest([1, 20, 10, 30, 15, 45, 50], 5))