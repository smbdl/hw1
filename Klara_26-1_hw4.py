# data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
# data_tuple = list(data_tuple)
# letters, numbers = [], []
# for i in data_tuple:
#     letters.append(i) if type(i) == str else numbers.append(i)
# del numbers[0]
# letters.append(numbers.pop(0))
# numbers.insert(1, 2)
# numbers.sort()
# letters.reverse()
# letters[1] = "G"
# letters[7] = "c"
# numbers = [i*i for i in numbers]
# letters = tuple(letters)
# numbers = tuple(numbers)
# print(letters)
# print(numbers)


data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data_tuple = list(data_tuple)
letters, numbers = [i for i in data_tuple if type(i) == str], [i for i in data_tuple if type(i) != str]
del numbers[0]
letters.append(numbers.pop(0))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = "c"
numbers = [i * i for i in numbers]
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
