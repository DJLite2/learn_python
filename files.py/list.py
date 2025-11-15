list1 = [1, 2, 3, 1]
print(list1)
list1.append([8, 9, 10])  # bu listga bitta qiymat qilib qushadi
print(list1)
a = len(list1)
print(a)
x = list1.pop(len(list1) - 1)  # oxirgi indexdagi qiymatni uchiradi
# appenddan farqli bu elementlarni alohida qushadi yani har bir element bitta indexsga ega buladi
print(x)
list1.extend([1, 2, 3, 4, 5, 6, 7, 8])
print(list1)

del list1[1]
print(list1)

for i in list1:
    print('value: ', i)
