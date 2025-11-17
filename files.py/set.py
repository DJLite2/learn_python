set = {1, 2, 3, 4, 5, 6}
set_a = {2, 3, 6, 7, 8}
set.add(9)
set.discard(3)
set.difference(set_a)
print(set | set_a)  # = print(set.union(set_a))
print(set.intersection(set_a))  # = print(set & set_a)
print(set.symmetric_difference(set_a))  # = print(set ^ set_a)


# dictionary
dict = {1: 'car', 2: 'bmw', 3: 'spark'}
print(dict)
print(type(dict))
print(dict[1])
print(dict)
dict[2] = 'BMW'
dict = {1: 'car', 2: 'bmw', 3: 'spark', 2: 'Bmw'}
print(dict)
# del dict[2] delite funcsion

for x in dict:
    print(x)

for key, value in dict.items():
    print(str(key) + " : " + value)


# simple sum (args)
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print(sum_of(1, 2, 3, 4, 5, 8))
# args is all argument input

# kwargs


def sum_of(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return round(sum, 2)


print(sum_of(coffe=3.99, cake=5.99, juice=2.99))
