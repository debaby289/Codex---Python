'''
In the last exercise, we created a Restaurant class.

In a new file called bobs_burgers.py, create an instance of the Restaurant class called bobs_burgers with the following attributes:
    'Bob\'s Burgers'
    'American Diner'
    4.7
    False

Once you do that, create two more instances of the Restaurant class with your favorite dinner spots nearby.

Then, use print(vars()) to output each of the three restaurants!
'''
# Write code below 💖

class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = False

bob = Restaurant()
bob.name = 'Bob\'s Burgers'
bob.category = 'American Diner'
bob.rating = 4.7
bob.delivery = False
print(vars(bob))

burgerheaven = Restaurant()
burgerheaven.name = 'Burger Heaven'
burgerheaven.category = 'American Diner'
burgerheaven.rating = 4.7
burgerheaven.delivery = True
print(vars(burgerheaven))

burgerville = Restaurant()
burgerville.name = 'Burger Ville'
burgerville.category = 'American Diner'
burgerville.rating = 3.2
burgerville.delivery = False
print(vars(burgerville))
