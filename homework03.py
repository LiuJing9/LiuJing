#EP:1
"""
num = -1
s,n,sum1 = 0,0,0
while num!=0:
    num = eval(raw_input('Please enter an integer, the input ends if it is 0: '))
    if num>0:
        s += 1
    if num<0:
        n += 1
    sum1 += num
pin = float(sum1) / (s+n) 
print('The number of positive number is: {}'.format(s))
print('The number of negative number is: {}'.format(n))
print('The number of sum is: {}'.format(sum1))
print('The number of average value is: {}'.format(pin))
"""

#EP:2
"""
pay = 10000
sum = 10000
for i in range(10):
    pay = pay + pay*0.05
    sum += pay
print(pay)
print(sum)
"""

#EP:4
"""
num = 0
for i in range(100,1000):
    if i%6==0 and i%5==0:
        num+=1
        print(i,' ',end=' ')
        if num%10==0:
           print('\n')
"""

#EP:5
"""
m=12000
while m*m*m>12000:
    m -= 1
print(m)
n=1
while n*n<12000:
    n += 1
print(n)  
"""

#EP:6
"""
a = eval(raw_input('Loan Amount: '))
y = eval(raw_input('Number of Years: '))
i=0.05
n = a*pow(i+1,y)
m = n / (12*y)
print('{:.5f}   {:.2f}   {:.2f}'.format(i,m,n))
while i<=0.08:
    i += 0.00125
    n = a*pow(i+1,y)
    m = n / (12*y)
    print('{:.5f}   {:.2f}   {:.2f}'.format(i,m,n))
"""

#EP:7
"""
a = 50001
b,num = 0,0
for i in range(50001):
    num = 1/(a-i)
    b += num
print(b)
"""

#EP:8
"""
a,b = 1,3
s = 1/3
while a<97:
    a += 2
    b += 2
    s += a/b
print(s)
"""

#EP:9
"""
a = eval(input('>>'))
num = 0
for i in range(1,a+1):
    num += pow((-1),i+1) / (2*i-1)
pi = 4*num
print(pi)
"""

#EP:10
"""
for i in range(1,10001):
    num = 0
    for j in range(1,int(i/2+1)):
        if i%j==0:
            num += j
    if num==i:
        print(num)
"""

#EP:11
"""
num = 0
for i in range(1,8):
    for j in range(1+i,8):
        print(i,' ',j)
        num += 1
print(num)
"""
