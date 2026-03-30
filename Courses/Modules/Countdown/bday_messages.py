'''
Let's use the datetime and random modules to make a birthday card to determine how far your birthday is from today! 🎂
For this exercise, we are creating two .py files in a separate code editor.
Note: You can do this on VS Code! Check out this article to set up VS Code.

## bday_messages.py
Create a new file called bday_messages.py.

Import the random module.

Then, define a bday_messages list with the following items:
    'Hope you have a very Happy Birthday! 🎈',
    'It's your special day – get out there and celebrate! 🎉',
    'You were born and the world got better – everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'
Next, use the random.choice() method to get a single item from the list.

Save this item in a random_message variable.

Let's save bday_messages.py and move to the next part.
'''
# Write code below 💖

import random as rd

bday_mssages = [
    'Hope you have a very Happy Birthday! 🎈',
    'It\'s your special day - get out there and celebrate! 🎉',
    'You were born and the world got better - everybody wins! 🥳',
    'Have lots of fun on your special day! 🎂',
    'Another year of you going around the sun! 🌞'
]

random_message = rd.choice(bday_mssages)
