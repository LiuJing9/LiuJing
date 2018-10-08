#_*_conding:utf8-

#EP:1
"""
def getPentagonalNumber(N):
    for n in range(1,N):
        w = n*(3*n-1)/2
        n += 1
        print(w,' ',end='')
        if n%10==0:
            print('\n')
getPentagonalNumber(101)
"""

#EP:2
"""
def sumDigits(n):
    s = 0
    while (n%10!=0):
        g=n%10
        s += g
        n=n//10
    print(s)
m=eval(raw_input('Please enter a number: '))
sumDigits(m)
"""

#EP:3
"""
def displaySortedNumbers(num1,num2,num3):
    num = [num1,num2,num3]
    num.sort()
    print(num)
n1,n2,n3 = eval(raw_input('Please enter three numbers: '))
displaySortedNumbers(n1,n2,n3)
"""

#EP:4
"""
investmentAmount = eval(input('The amount invested: '))
monthlyInterestRate = eval(input('Annual interest rate: '))
def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
    return investmentAmount*pow((1+monthlyInterestRate/100/12),years*12)
for years in range(1,31):
    num = futureInvestmentValue(investmentAmount,monthlyInterestRate,years)
    print("%d\t%.2f"%(years,num),end=" ")
    print()
"""

#EP:5
"""
def printChars(ch1,ch2,numberPerLine):
    c1 = ord(ch1)
    c2 = ord(ch2)+1
    s = 0
    for i in range(c1,c2):
        print(chr(i),end=" ")
        s += 1
        if s%numberPerLine==0:
           print(" ")
printChars('1','Z',10)
"""

#EP:6
"""
def numberOfDaysInAYear(year):
    if (year%4==0) and (year%100!=0):
       print('366 days in {}'.format(i))
    else:
       print('365 days in {}'.format(i))
for i in range(2010,2021):
    numberOfDaysInAYear(i)
"""

#EP:7
"""
x1,y1 = eval(raw_input('Please enter x1 and y1 for point1: '))
x2,y2 = eval(raw_input('Please enter x2 and y2 for point2: '))
def distance(x1,y1,x2,y2):
    sum = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))**0.5
    print(sum)
distance(x1,y1,x2,y2)
"""

#EP:8
"""
import math
def n(a):
    s = 0
    for j in range(2,int(math.sqrt(a)+1)):
            if a%j==0:
               s = 0
            else:
               s = 1
    return s
for i in range(1,32):
    s = pow(2,i)-1
    if n(s):
       print("%d\t%d"%(i,s))
"""

#EP:9
"""
import time
print(time.asctime(time.localtime(time.time())))
"""

#EP:10
"""
n,m = eval(raw_input('Throw two dice,please: '))
if n+m==2 or n+m==3 or n+m==12:
    print('You rolled {} + {} = {}'.format(n,m,n+m))
    print('You lose')
elif n+m==7 or n+m==11:
    print('You rolled {} + {} = {}'.format(n,m,n+m))
    print('You win')
else:
    while(1):
      print('You rolled {} + {} = {}'.format(n,m,n+m))
      print('point is {}'.format(n+m))
      sum = n+m
      n,m = eval(raw_input('Throw two dice,please: '))
      if n+m==7:
         print('You rolled {} + {} = {}'.format(n,m,n+m))
         print('You lose')
         break
      elif n+m==sum:
         print('You rolled {} + {} = {}'.format(n,m,n+m))
         print('You win')
         break
      else:
         continue
"""
