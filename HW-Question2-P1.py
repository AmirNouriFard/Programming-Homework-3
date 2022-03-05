#Advanced Programming Course Homework: 3 Page 1 Question 2
val = int(input('please enter a number : '))
if val<10:
    if val !=5:
        print('wow',end='')
    else:
        val+=1
else:
    if val==17:
        val+=10
    else:
        print('whoa',end='')
print(val)
#What will the program print if the user provides the following input?
#(a) 3 (b) 21 (c) 5 (d) 17 (e) -5
#If user enter 3 , the program will print : wow3
#If user enter 21 , the program will print : whoa21
#If user enter 5 , the program will print : 6
#If user enter 17 , the program will print : 27
#If user enter -5 , the program will print : wow-5