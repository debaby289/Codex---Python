'''
When you pull up to a drive-thru like McDonald's, you can order food by saying item numbers.

Create a drive_thru.py program with your favorite fast food chain's menu.

Define a get_item() function that takes in one parameter, the number of the item you want to order, and returns the name of that item!

For example, if you called the function with:
    Argument value 1, it could return '🍔 Cheeseburger'.
    Argument value 2, it could return '🍟 Fries'.
    Argument value 3, it could return '🥤 Soda'.
    Argument value 4, it could return '🍦 Ice Cream'.
    Argument value 5, it could return '🍪 Cookie'.
Make sure to call this function a few times to make sure that it works!

Lastly, let's do the following:
    Create a welcome menu and put that in a welcome() function.
    Create a main program that takes in user input with input().
'''
# Write code below 💖

def get_item(order_number):
    if order_number == 1:
        return ('🍔 Cheeseburger')
    elif order_number == 2:
        return ('🍟 Fries')
    elif order_number == 3:
        return ('🥤 Soda')
    elif order_number == 4:
        return ('🍦 Ice Cream')
    elif order_number == 5:
        return ('🍪 Cookie')
    
def welcome():
    print('🍔 Cheeseburger')
    print('🍟 Fries')
    print('🥤 Soda')
    print('🍦 Ice Cream')
    print('🍪 Cookie')

welcome()

option = int(input('What would you like to order? '))
print(get_item(option))