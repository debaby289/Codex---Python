'''
# Area Calculator
Create a calculator.py program that calculates the area of one of the following shapes:
    Square
    Rectangle
    Triangle
    Circle
The program should present a menu for the user to choose which shape to calculate, then ask them for the appropriate values (side, length, width, etc.).

Then, it should calculate the area and print it out.

Here are the area equations for each shape:
    Square_area = side^2
    Rectangle_area = length * width
    Triangle_area = (height * base) / 2
    Circle_area = π * radius^2
 
Note: For pi π in the area of a circle, feel free to either use 3.14 or import the math module to use the math.pi variable.

The output should look something like this:
    ==================
    Area Calculator 📐
    ==================

    1) Triangle
    2) Rectangle
    3) Square
    4) Circle
    5) Quit

    Which shape: 1

    Base: 5
    Height: 6

    The area is 15
'''
import math

print('==================')
print('Area Calculator 📐')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

choice = input('Which shape: ')

if choice == '1':  # Triangle
    base = float(input('Base: '))
    height = float(input('Height: '))
    area = (base * height) / 2

elif choice == '2':  # Rectangle
    length = float(input('Length: '))
    width = float(input('Width: '))
    area = length * width

elif choice == '3':  # Square
    side = float(input('Side: '))
    area = side ** 2

elif choice == '4':  # Circle
    radius = float(input('Radius: '))
    area = math.pi * radius ** 2

elif choice == '5':
    print('Goodbye!')
    exit()

else:
    print('Invalid choice')
    exit()

print(f'The area is {area}')
