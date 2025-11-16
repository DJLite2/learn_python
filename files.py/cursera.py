# funksiyalar
'''def bolinma(bulivchi, bolinma):
    return round((bulivchi * bolinma) / 100.00, 2)


print(bolinma(134.00, 12))
print(bolinma(123.89, 12))'''


# 2 variable scope

'''from threading import local


my_global = 10


def f1():
    fvalue = 7

    def f2():
        local = 5
        print('my global value is: ', my_global)
        print(fvalue)
    f2()


f1()'''


special = 5


def get_total(a, b):
    # enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        # local variable
        double = total * 2
        print(special)

    double_it()


get_total(2, 4)
