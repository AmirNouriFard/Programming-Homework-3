#Advanced Programming Course Homework: 3, Page 2
#Programming questions , Question 3
print('Please enter 5 number :')
num1 = int(input('number 1 : '))
num2 = int(input('number 2 : '))
num3 = int(input('number 3 : '))
num4 = int(input('number 4 : '))
num5 = int(input('number 5 : '))
if num1==num2 or num1==num3 or num1==num4 or num1==num5 or num2==num3 or num2==num4 or num2==num5 or num3==num4 or num3==num5 or num4==num5 :
    print('DUPLICATES')
else:
    print('ALL UNIQUE')