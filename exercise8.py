# Exercise 8

#     Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.


foods = ("Apple","Orange","Cherry","Melon","Apricot","Mango")
for food in foods:
    if "a" in food.lower():
        print("'a' food detected: ", food)