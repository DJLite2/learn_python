import numpy as np
import matplotlib.pyplot as plt

Ib = np.array([25, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400])

Ube_Uce0 = np.array([475, 495, 507, 516, 523, 529,
                    538, 545, 551, 557, 562])

Ube_Uce10 = np.array([686, 716, 733, 745, 754, 761,
                     773, 781, 789, 795, 800])

plt.figure(figsize=(8, 5))
plt.plot(Ube_Uce0, Ib, 'o-', label='Uce=0V')
plt.plot(Ube_Uce10, Ib, 's-', label='Uce=10V')
plt.xlabel("Ube (мВ)")
plt.ylabel("Ib (мкА)")
plt.title("2N2369A Кириш характеристикаси")
plt.legend()
plt.grid()
plt.show()

Uce = np.linspace(0, 20, 21)  # V

Ik_Ib25 = np.array([0.0, 2.3, 2.31, 2.33, 2.34, 2.36, 2.38, 2.39, 2.40,
                   2.42, 2.43, 2.45, 2.50, 2.59, 2.60, 2.61, 2.62, 2.63, 2.64, 2.65, 2.66])
Ik_Ib50 = Ik_Ib25 * 2.3
Ik_Ib75 = Ik_Ib25 * 3.5
Ik_Ib100 = Ik_Ib25 * 4.6
Ik_Ib125 = Ik_Ib25 * 5.7
Ik_Ib150 = Ik_Ib25 * 6.8

plt.figure(figsize=(8, 5))
plt.plot(Uce, Ik_Ib25, 'o-', label='Ib=25 мкА')
plt.plot(Uce, Ik_Ib50, 's-', label='Ib=50 мкА')
plt.plot(Uce, Ik_Ib75, '^-', label='Ib=75 мкА')
plt.plot(Uce, Ik_Ib100, 'd-', label='Ib=100 мкА')
plt.plot(Uce, Ik_Ib125, 'p-', label='Ib=125 мкА')
plt.plot(Uce, Ik_Ib150, '*-', label='Ib=150 мкА')
plt.xlabel("Uce (В)")
plt.ylabel("Ik (мА)")
plt.title("2N2369A Чиқиш характеристикаси")
plt.legend()
plt.grid()
plt.show()


delta_Ube = 733 - 686
delta_Ib = 75 - 25
h11e = delta_Ube / delta_Ib
print(f"h11э (Кириш каршилиги) = {h11e:.2f} кОм")

delta_Ube = 716 - 495
delta_Uce = 10 - 0
h12e = delta_Ube / delta_Uce
print(f"h12э (Кириш-чиқиш ўтказувчанлиги) = {h12e:.4f}")

delta_Ik = 8.4 - 2.4
delta_Ib = 75 - 25
h21e = delta_Ik / delta_Ib
print(f"h21э (Ток бўйича узатиш коэффициенти β) = {h21e:.2f}")


delta_Ik = 0.05
delta_Uce = 2
h22e = delta_Ik / delta_Uce
print(f"h22э (Чиқиш каршилиги) = {h22e:.4f} мА/В")

r_vx = h11e
r_vy = 1/h22e
print(f"Кириш каршилиги rвх = {r_vx:.2f} кОм")
print(f"Чиқиш каршилиги rвых = {r_vy:.2f} кОм")
