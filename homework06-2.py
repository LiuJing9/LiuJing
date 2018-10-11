# _*_coding:utf8-

#1
"""
def score(s1):
    for i in range(len(s1)):
        if int(s1[i])>=int(max(s1))-10:
           print('Student {} score is {} and grade is A'.format(i,s1[i]))
        elif int(s1[i])>=int(max(s1))-20:
           print('Student {} score is {} and grade is B'.format(i,s1[i]))
        elif int(s1[i])>=int(max(s1))-30:
           print('Student {} score is {} and grade is C'.format(i,s1[i]))       
        elif int(s1[i])>=int(max(s1))-40:
           print('Student {} score is {} and grade is D'.format(i,s1[i]))
        else:
           print('Student {} score is {} and grade is F'.format(i,s1[i]))    
g=raw_input('Please enter scores: ')
q=g.split(' ')
score(q)
"""
#2
"""
def List(l):
    l.reverse()
    print l
n=raw_input('Please enter list number: ')
m=n.split(' ')
List(m)
"""
#3
"""
def Inte(n):
    n1=set(n)
    for i in n1:
        print('{} occurs {} times'.format(i,n.count(i)))
m=raw_input('Please enter integers between 1 and 100: ')
q=m.split(' ')
Inte(q)
"""
#4
"""
def score(s):
    a,b,c,d,e=0,0,0,0,0
    for i in s:
        a+=float(i)
        c+=1
    b=a/c
    print('Average score is: {}'.format(b))
    for j in range(len(s)):
        if float(s[j])>=b:
            d+=1
        elif float(s[j])<b:
            e+=1
    print('A score greater than or equal to the average score: {}'.format(d))
    print('Less than average score: {}'.format(e))   
n=raw_input('Please enter scores: ')
m=n.split(' ')
score(m)
"""
#5
"""
import random
def ran(n):
    m=set(n)
    for j in m:
        print('{} occurs {} times'.format(j,n.count(j)))
n=[random.randint(0,9) for i in range(1000)]
ran(n)
"""
#6
"""
def indexOfSmallestElement(lst):
    l=min(lst)
    a=''.join(lst)
    print a.find(l)
lst=raw_input('Please enter number: ')
ls=lst.split(',')
indexOfSmallestElement(ls)
"""
#7
"""
import random
def shuffle(lst):
    random.shuffle(lst)
    print lst
lst=raw_input('Please enter number: ')
ls=lst.split(' ')
shuffle(ls)
"""
#8
"""
def eliminateDuplicates(lst):
    ls=set(lst)
    print('The distinct numbers are: {}'.format(list(ls)))
lst=raw_input('Please enter ten numbers: ')
l=lst.split(' ')
eliminateDuplicates(l)
"""
#9
"""
def isSorted(lst):
    if lst==sorted(lst):
       print '[+] The list is already sorted'
    else:
       print '[-] The list is not sorted'
lst=raw_input('Please enter list: ')
ls=lst.split(' ')
isSorted(ls)
"""
#10
"""
def List(l):
    t=0
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
               t=l[j]
               l[j]=l[i]
               l[i]=t
    print l
l=raw_input('Please enter ten  numbers: ')
ls=l.split(' ')
List(ls)
"""
#11


#12
"""
def isConsecutiveFour(values):
    s=0
    for i in range(1,len(values)):
        if values[0]==values[i]:
            s+=1
        if s>=4:
            print('True')
        else:
            print('Flase')
            
        if values[0]!=values[i]:
            s=0
            values[0]=values[i]
        return values[0]
v=raw_input('Please enter a sequence of integers: ')
va=v.split(' ')
isConsecutiveFour(va)
"""
