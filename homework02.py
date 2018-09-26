#EP:1
"""
import math
r = eval(raw_input('Please enter the length from the center to a vertex: '))
s = 2 * r * math.sin(math.pi/5)
area = 5 * s * s / (4*math.tan(math.pi/5))
print('The area of the pentagon is: {:.2f}'.format(area))  """


#EP:2
"""
import math
x1,y1 = eval(raw_input('Please enter point 1 (latitude and longitude) in degrees: '))
x2,y2 = eval(raw_input('Please enter point 2 (latitude and longitude) in degrees: '))
d = 6371.01 * (math.acos(math.radians(math.sin(x1)*math.sin(x2)+math.cos(x1)*math.cos(x2)*math.cos(y1-y2))))
print('The distance between the two points is: {} km'.format(d))   
"""



#EP:3
"""
import math
s = eval(raw_input('Please enter the side: '))
area = (5*s*s)/4/(math.tan(math.pi/5))
print('The area of the pentagon is: {}'.format(area))  """



#EP:4
"""
import math
n = eval(raw_input('Please enter the number of sides: '))
s = eval(raw_input('Please enter the side: '))
area = n*s*s/(4*(math.tan(math.pi/n)))
print('The area of the polygon is: {}'.format(area))  """



#EP:5
"""
num = eval(raw_input('Please enter an ASCII code (0~127): '))
print('The character is: {}'.format(chr(num)))  """



#EP:6
"""
name = raw_input('Please enter employee is name: ')
num = eval(raw_input('Please enter number of hours worked in a week: '))
rate = eval(raw_input('Please enter hourly pay rate: '))
fed = eval(raw_input('Please enter federal tax withholding rate: '))
state = eval(raw_input('Please enter state tax withholding rate: '))
gr = rate * num
fe = gr * fed
st = gr * state
total = fe + st
net = gr - total
print('Employee Name: {}'.format(name))
print('Hours Worked: {}'.format(num))
print('Pay Rate: ${}'.format(rate))
print('Gross Pay: ${}'.format(gr))
print('Deductions\n Federal Withholding (20.0%): ${}\n State Withholding (9.0%): ${:.2f}\n Total Deduction: %{:.2f}'.format(fe,st,total))
print('Net Pay: ${:.2f}'.format(net))  """



#EP:7
"""
num = eval(raw_input('Please enter an integer: ')
q = num // 1000
b = (num%1000)//100
s = (num%100)//10
g = num%10
sum = g*1000 + s*100 + b*10 + q
print('The reversed number is: {}'.format(sum))
"""



#EP:8
"""
res = ''
for i in "2443048363@qq.com":
    res = res + chr(ord(i) + 1)
print(res)   """



#EP:1
"""
import math
a,b,c = eval(raw_input('Please enter a, b and c: '))
s = b*b - 4*a*c
if s>0:
    r1 = (-b + math.sqrt(s)) / (2*a)
    r2 = (-b - math.sqrt(s)) / (2*a)
    print('The roots are  {:.6f}  and  {:.5f}'.format(r1,r2))
elif s==0:    
    r1 = r2 = (-b + math.sqrt(s)) / (2*a)
    print('The root is  {:.0f}'.format(r1))
else:
    print('The equation has no real roots')  """ 



#EP:2
"""
import random
num1 = random.randint(0,100)
num2 = random.randint(0,100)
sum = eval(raw_input('Please enter sun: '))
if sum==num1+num2:
    print('True')
else:
    print('False')   """



#EP:3
"""
week = eval(raw_input('Please enter today is day: '))
day = eval(raw_input('Please enter the number of days elapsed since today: '))
f = (week+day)%7
if f==0:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==1:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==2:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==3:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==4:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==5:
    print('Today is  {}  and the future day is  {}'.format(week,f))
if f==6:
    print('Today is  {}  and the future day is  {}'.format(week,f))
"""



#EP:4
"""
a,b,c = eval(raw_input('Please enter a, b and c: '))
max1=max(a,b,c)
min1=min(a,b,c)
z=a+b+c-max1-min1
print('The number are: {}  {}  {}'.format(min1,z,max1))
"""



#EP:5
"""
wight1,num1 = eval(raw_input('Please enter wight and price for package 1: '))
wight2,num2 = eval(raw_input('Please enter wight and price for package 2: '))
Package1 = num1/wight1
Package2 = num2/wight2
if Package1<Package2:
    print('Package 1 has the better price')  
if Package1>Package2:
    print('Package 2 has the better price')  
"""



#EP:6
"""
m,y = eval(raw_input('Please enter month and year: '))
if m==2:
    if (y%4==0 or y%100!=0)and y%4==0:
        n=29
    else:
        n=28
else:
    if m==4 and m==6 and m==9 and m==11:
        n=30
    else:
        n=31
print('{}  day and  {}  month have  {}  day'.format(y,m,n))
"""



#EP:7
"""
import random
num = eval(raw_input('positive(1), negative(0): '))
com = random.randint(0,1)
if num==com:
    print(True)
else:
    print(False)  """



#EP:8
"""
import random
num = eval(raw_input('scissor(0), rock(1), paper(2): '))
com = random.randint(0,2)
if num==com:
    print('draw')
elif (num==0 and com==2) or (num==1 and com==0)or (num==2 and com==1):
    print('win')
else:
    print('lose')   
"""



#EP:10
"""
import random
pai = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
hua = ['mh','ht','fk','heit']
p =random.choice(pai)
h = random.choice(hua)
print('The card you picked is  {}  of  {}'.format(p,h))
"""



#EP:11
"""
num = eval(raw_input('Please enter a three-digit integer: '))
b = num//100
g = num%10
if b==g:
    print('{}  is a palindrome'.format(num))
if b!=g:
    print('{}  is not a palindrome'.format(num))  """



#EP:12
"""
a,b,c = eval(raw_input('Please enter edges: '))
if a+b<=c and a+c<=b and b+c<=a:
    print('This is illegal')
else:
    print('The perimeter is: {}'.format(a+b+c))
"""
