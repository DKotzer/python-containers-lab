# Exercise 5

#     Iterate over the key: value pairs in home_town and print a string for each item, for example:
#     "city = Arcadia"
#     "state = California"
#     "population = 58000"


home_town = {
    "city": "Toronto",
    'state': 'Ontario',
    'population': '666,000,000'
}


for entry in home_town:
    print(entry, home_town[entry])


# print("I was born in ", home_town["city"], " ", home_town["state"]," - population of ",home_town["population"])

# print("city = ", home_town["city"])
# print("state = ", home_town["state"])
# print("population = ",home_town["population"])


