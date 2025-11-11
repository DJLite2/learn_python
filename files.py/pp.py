def gpa(ball):
    umumiy = sum(ball)
    if umumiy >= 360:
        return "the best"
    elif umumiy >= 320:
        return "well"
    else:
        return "work hard"


def ortacha_baho(talaba_baholari):
    if not talaba_baholari:
        return "Baholar royxati bosh!"

    ortacha = sum(talaba_baholari) / len(talaba_baholari)
    return round(ortacha, 1)


talabalar_baholari = {
    "Alijon": [85, 90, 78, 92],
    "Lola": [95, 88, 90, 97],
    "Davron": [70, 75, 68, 80],
    "Nilufar": [91, 93, 89, 94]
}
the_best_talabalar_soni = 0


for ism, baholar in talabalar_baholari.items():
    ortacha = ortacha_baho(baholar)
    umumiy = gpa(baholar)
    print(f"{ism}: ortacha baho = {ortacha}, natija: {umumiy}")
    if umumiy == "the best":
        the_best_talabalar_soni += 1  # Hisoblagichni 1 ga oshirish

print(type(talabalar_baholari))
print(
    f"'the best' natijasiga erishgan talabalar soni: {the_best_talabalar_soni}")
