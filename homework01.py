"""
celsius = eval(raw_input('Please enter a temperature in Celsius:'))
fahrenheit = (9.0/5.0) * celsius + 32
print('The transformed Fahrenheit is:{}'.format(fahrenheit))"""


"""
radius,length = eval(raw_input('Please enter the radius and height of the cylinder:'))
area = radius * radius * 3.1415
volume = area * length
print('The area and volume of the output are: {} {}'.format(area,volume))"""


"""
feet = eval(raw_input('Please enter a vlaue for feet: '))
meters = feet * 0.305
print('{} feet is {} meters'.format(feet,meters)) """


"""
M = eval(raw_input('Please enter amount of water in kilograms: '))
initialTem = eval(raw_input('Please enter the initial temperature: '))
finalTem = eval(raw_input('Please enter the final temperature: '))
Q = M * (finalTem-initialTem) * 4184
print('The energy needed is: {}'.format(Q)) """


"""
balance,rate = eval(raw_input('Please enter balance and interest rate: '))
interest = balance * (rate/1200)
print('The interest is: {:.5f}'.format(interest)) """


"""
v0,v1,t = eval(raw_input('Please enter v0,v1 and t: '))
a = (v1-v0)/t
print('The average acceleration is: {:.4f}'.format(a)) """


"""
num = eval(raw_input('Please enter the monthly saving amount: '))
sum=0
for i in range (0,6):
    sum=(sum+num) * (1+0.00417)
print('After the sixth month, the account value is: {:.2f}'.format(sum)) """


"""
num = eval(raw_input('Please enter a number between 0 and 1000: '))
sum = num%10 + num//10%10 + num//100
print('The sum of the digits is: {}'.format(sum)) """

