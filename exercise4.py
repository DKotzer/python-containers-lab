# Exercise 4

#     Create a dictionary named home_town containing the keys of city, state and population.
#     Print a string with this format:
#     "I was born in city, state - population of population"



home_town = {
    "city": "city1",
    'state': 'state1',
    'population': '666'
}
print(home_town["city"])
print(home_town["state"])
print(home_town["population"])

print("I was born in ", home_town["city"], " ", home_town["state"]," - population of ",home_town["population"])
