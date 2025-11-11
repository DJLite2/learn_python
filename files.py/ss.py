def son_taqqoslash(a, b):
    if a > b:
        return "a son katta "
    elif a == b:
        return "sonlar teng"
    else:
        return "b son katta "


try:
    a = int(input("1-sonni kirit: "))
    b = int(input("2-sonni kirit: "))
    natija = son_taqqoslash(a, b)
    print(natija)
except ValueError:
    print("iltimos faqat son kiriting")
finally:
    print("well done!!!")
