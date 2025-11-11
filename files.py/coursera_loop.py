# for loop and while loop
fruits = ['apple', 'banana', 'oreng', 'gress']

for item in fruits:
    print("I like fruits is- ", item)

for i in range(10):
    print("loop__", i)

count = 0
while count < len(fruits):
    print("I like fruits is ", fruits[count])
    count += 1

for idx, item in enumerate(fruits):
    print(idx, item)


favorites = ['Creme Brulee', 'Apple Pie',
             'Churros', 'Tiramisú', 'Chocolate Cake']
# continue
for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

# pass
for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are', dessert)
