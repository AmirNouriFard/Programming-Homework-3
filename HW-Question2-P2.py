#Advanced Programming Course Homework: 3, Page 2
#Programming questions , Question 2
print('Please enter the sides of the triangle :')
side1 = int(input('side 1 : '))
side2 = int(input('side 2 : '))
side3 = int(input('side 3 : '))
if side1==side2 or side2==side3 or side1==side3 :
    print('Right triangle')
else :
    print('Not Right triangle')