'''
Let’s go back to fruits! 🫐🍇🍌🍓🍒

Grocery shopping is great until you forget what was on your list. 😥

Before you head out, your best friend ask you to pick up some fruit for her too. Let's combine the lists!
    Create two sets representing your favorite fruits and your best friend's favorite fruits.
    Print the union of the two sets.
    Print the intersection of the two sets.

Have fun with it, check if the same fruit is in both sets or see the <difference> in both sets.

Remember: tomatoes are fruits! 🍅
'''
# Write code below 💖

my_favorite_fruits = {
  'purple grapes',
  'cherries',
  'strawbeerries'
}

my_friends_favorite_fruits = {
    'bananas',
    'cherries',
    'green grapes'
}

our_fruits = my_favorite_fruits.union(my_friends_favorite_fruits)
different_friends = my_favorite_fruits.intersection(my_friends_favorite_fruits)

print(our_fruits)
print(different_friends)