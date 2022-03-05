#Advanced Programming Course Homework: 3, Page 2
#Programming questions , Question 1
while True:
    income = int(input('Please enter your monthly income : '))
    tax = 0
    if income<=1000:
        tax = 0
    elif income>1000 and income<=2500:
        tax = (income * 10) / 100 
    elif income>2500 and income<=4000:
        tax = (income * 15) / 100 
    elif income>4000 and income<=6000:
        tax = (income * 20) / 100 
    elif income>=8000:
        tax = (income * 30) / 100 
    netincome = income - tax
    print('Your net income in this month is : ',netincome)



