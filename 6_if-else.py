#if-else

'''age = int(input("Enter your age: "))
if age < 18:
    print("SORRY! you are a minor, you cannot drive")
else:
    print("you are an adult, you can drive")'''


#if_elif_else

percent = int(input("Enter your percentage: "))
if (percent >= 90 and percent <= 100):
    print("Congratulations! you got an A+ grade")
elif(percent >= 80 and percent < 90):
    print("Congratulations! you got an A grade")
elif(percent >= 70 and percent < 80):
    print("Good! you got a B grade")
elif(percent >= 60 and percent < 70):
    print("Not bad! you got a C grade")
elif(percent >= 50 and percent < 60):
    print("Keep trying! you got a D grade")
elif(percent >= 40 and percent < 50):
    print("just pass! you have to work hard")
elif(percent > 100 or percent < 0):
    print("its incorrect input, please enter a valid percentage between 0 to 100")
elif(percent >= 33 and percent < 40):
    print("just passed!")
else:
    print("You failed, better luck next time")

#number check

    
    
    
    
num=int(input("Enter the value of num:"))
if(num<0):
    print("Your number is \"Negative\"")
elif(num==0):
    print("number is \"zero\"")
else:
    print("Your number is \"Positive\"")   


#clock

import time
name = input('Enter your name: ')
Recenttime = int(time.strftime('%H'))
recenttime = time.strftime('%H:%M:%S')
c= name.capitalize()
if(4<=Recenttime<12):
    print('GOOD MORNING',c,'its time to wake up and do some exercise because the time is',recenttime)
elif(12<=Recenttime<17):
    print('GOOD AFTERNOON',c,'its',recenttime)
elif(17<=Recenttime<21):
    print('GOOD EVENING',c,'its',recenttime)
else:
    print('GOOD NIGHT',c,'its',recenttime)
# print('Hii',name,'its',recenttime)
# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59