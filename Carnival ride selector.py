# Ride Selector start
import time
print ('''Welcome These are the rides we have 
1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgigator''')



ride_number_text = input('Please enter the ride number here: ')
ride_number = int(ride_number_text)

while ride_number <1 or ride_number>5:
    print("Invalid number")
    ride_number_text =  input("Please, enter the ride number you want")
    ride_number = ride_number_text

    print('You have selectedc ride number: ', ride_number)

if ride_number == 1:
    print('You have picked Scenic River Cruise')
    print('There are no age limits on this ride')


else:
 age_text = input('Please enter your age: ')
 age = int(age_text)

 while age<1 or age>95:
    # Repeat this code while age is invalid
     print('Invalid age')
     age_text = input('Please enter your age')
     age = age_text
# When we get here. the age is valid
print("Thank you for entering your age: ")

if ride_number == 2:
    print('You have picked Carnival Carousel')
    print('The age limits for this ride is 3 - 5years')
if age>= 3:
    print('Congratulations you can go on the ride')
else:
    print('Sorry, you cant go on this ride')

if ride_number == 3:
    print('You have picked Jungle Adventure Water Splash ')
    print('The age limits for this ride is 6 - 8years')

if age>= 6:
        print('Congratulations you can go on the ride')
else:
    print('Sorry, you cant go on this ride')

if ride_number == 4:
      print('You have picked Downhill Mountain Run')
      print('The age limits for this ride is 9 - 15years')
      if age>= 9:
        print('Congratulations you can go on the ride')
    
else: 
    print('Sorry, you cant go on this ride')
    

if ride_number == 5:
    print('You have picked the regurgitator!!!')
    print('The age limits is 16 - 25years')

if age>= 16:
    # Age is not too low
    if age > 70:
        # Age is too high
        print('Sorry, you are too old')

    else:
        # Age is in correct range
        print('You can go on the ride')

else:
    print('Sorry, you cant go on this ride')



 

