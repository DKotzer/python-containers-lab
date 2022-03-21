foods = ("Apple","Orange","Cherry","Melon","Apricot","Mango")


# Exercise 3

#     Using a for loop, print just the last two food strings from foods.

for food in enumerate(foods):
    # if food == -1 or food == -2:
    # print(foods.index)
    print(foods[-1], foods[-2])

# for food in foods.reverse():
