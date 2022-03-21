# Exercise 7

#     Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
#     ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
    # Iterate over awesome_students printing out each string.



names = ["Dylan", "Jon", "Camiel", "Lila", "Basheer", "Nicole"]

awesome_names = []
def awesome(names):
    for name in names:
        awesome_names.append(name + "is awesome!")
        # print(name) # same as below 
        
awesome(names)
for name in awesome_names:
    print(name)
