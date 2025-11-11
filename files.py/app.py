def solishtir_son(son):

    son_str = str(son)

    if len(son_str) != 6:
        return "Xatolik: son 6 xonali bo‘lishi kerak!"

    chap = sum(int(x) for x in son_str[:3])
    ong = sum(int(x) for x in son_str[3:])

    if chap == ong:
        return "Sizning biletingiz omadli!"
    else:
        return "Oddiy bilet."


try:
    son = int(input("6 xonali son kiriting: "))
    natija = solishtir_son(son)
    print(natija)

except ValueError:
    print("Xatolik: faqat raqam kiriting!")
finally:
    print("dastur ishlamoqda")
