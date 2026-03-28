'''
Ever wonder how many people live in New York City? What about London?

Create a favorite_cities.py program.

Let's make a City class that uses the __init__() method to define the following attributes:
    name (string)
    country (string)
    population (integer rounded to the nearest thousand people)
    landmarks (list of strings)

Next, create an object for your hometown and assign the attributes above.

Lastly, create another object for the city that you've always wanted to visit!

Bonus: Add 2-3 more attributes, like nickname, founding year, mayor, etc.
'''
# Write code below 💖

class City:
    def __init__(self,name,country,population,landmarks):
        self.name = name
        self.country = country
        self.population = population
        self.landmarks = landmarks


nyc = City("New York City", "USA", 8468000, ["Statue of Liberty", "Brooklyn Bridge", "Apollo Theatre"])
shanghai = City("Shanghai", "China", 26320000, ["The Bund", "Jin Mao Tower", "Tianzifang"])

print(vars(nyc))
print(vars(shanghai))
