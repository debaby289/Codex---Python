'''
Create a new file called main.py.
Import both the datetime module as well as bday_messages (the last file).
    import datetime, bday_messages

Next, use the datetime module to create two date objects:
    today: Today's date, using the datetime.date.today() method.
    next_birthday: The date for your next birthday, using the year, month, and day arguments.

A really cool thing you can do with date objects is addition and subtraction!
    time_difference = date1 - date2

Use date subtraction to calculate how many days away today is from next_birthday. Then, assign the result to a new variable called days_away.

Then, create a control flow statement:
    If today is equal to next_birthday, print the random_message variable (imported from bday_messages).
    Else, print 'My next birthday is {days_away} days away!'.

The output should look something like this:
    My next birthday is 42 days away!

Got it working locally? Congrats! Click "Submit answer" to continue. ヾ( ˃ᴗ˂ )◞ • *✰

Bonus: Instead of using a date in the future, what if we tried to see how many days it's been since a past event, like the release date of your favorite movie or game, or the date you were born? What about how many years or months it's been?
'''
# Write code below 💖

import datetime,bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026,7,22)

days_away = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away.days} days away!')