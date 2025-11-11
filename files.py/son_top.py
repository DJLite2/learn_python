# kompyuter son uylaydi men uni topishim kk keyin men uylayman u topishi kk
import random


def son_top():
    kom_soni = random.randint(1, 100)
    topildi = False

    while not topildi:
        taxmin = int(input("uylagan soningizni kiriting: "))
        if taxmin == kom_soni:
            print("Topildi")
            topildi = True
        elif taxmin < kom_soni:
            print("sen uylagan son kichik")
        else:
            print("sen uylagan son katta")

    return True


def kompyuter_top():
    print("\n--- Kompyuter topadi ---")
    print("Siz 1 dan 100 gacha son o'ylang.")
    input("O'yladingizmi? Enter tugmasini bosing...")

    min_son = 1
    max_son = 100
    topildi = False
    urinishlar = 0

    while not topildi:
        urinishlar += 1

        taxmin = (min_son + max_son) // 2

        javob = input(
            f"Sizning soningiz {taxmin}mi? JAVOBINGIZNI kiriting (kichik/katta/to'g'ri): ").lower()

        if javob == "to'g'ri":
            print(
                f"Yes! Kompyuter {urinishlar} urinishda to'g'ri topdi: {taxmin}!")
            topildi = True
        elif javob == "katta":
            min_son = taxmin + 1
        elif javob == "kichik":
            max_son = taxmin - 1
        else:
            print("Nog'o'ri buyruq. Iltimos, 'kichik', 'katta' yoki 'to'g'ri' kiriting.")
        if min_son > max_son:
            print("Mantiqiy xatolik! Siz noto'g'ri javoblar berdingiz shekilli.")
            break


qayata_uynash = "ha"

while qayata_uynash.lower() == "ha":
    son_top()
    kompyuter_top()

    qayata_uynash = input("qayta uynaysizmi? (ha/yuq): ").strip()

print("Xayr,salomatbuling")
