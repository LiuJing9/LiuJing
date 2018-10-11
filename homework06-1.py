# _*_coding:utf8-

#1
"""
def sn(n):
    a = "232-22-3333"
    if n==a:
        print '[+] Valid SSN'
    else:
        print '[-] Invalid SSN'
m=raw_input('Please enter a social security: ')
sn(m)
"""
#2
"""
def ch(ch1,ch2):
        print ch2.find(ch1)
c1=raw_input('Please enter a string of strings: ')
c2=raw_input('Please enter a string of strings: ')
ch(c1,c2)
"""
#3
"""
def pwd(m):
    if len(m)>=8:
        if m.isalnum()==True:
            for i in m:
               s=0
               if i>='0' and i<='9':
                  s += 1
            if s>=2:
                print '[+] valid password'
            else:
                print '[-] invalid password'
        else:
            print '[-] invalid password'           
    else:
        print '[-] invalid password'
n=raw_input('Please enter the password: ')
pwd(n)
"""
#4
"""
def countLetters(s):
    n=0
    for i in range(len(s)):
        if (s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z'):
           n += 1
    print(n)
s1=raw_input('Please enter a string: ')
countLetters(s1)
"""
#5:
"""
def getNumber(u):
    for i in range(len(u)):
        if u[i]>='0' and u[i]<='9':
            print u[i],
        elif (u[i]>='a' and u[i]<='c') or (u[i]>='A' and u[i]<='C') :
            print 2,
        elif (u[i]>='d' and u[i]<='f') or (u[i]>='D' and u[i]<='F'):
            print 3,
        elif (u[i]>='g' and u[i]<='i') or (u[i]>='G' and u[i]<='I'):
            print 4,
        elif (u[i]>='j' and u[i]<='l') or (u[i]>='J' and u[i]<='L'):
            print 5,
        elif (u[i]>='m' and u[i]<='o') or (u[i]>='M' and u[i]<='O'):
            print 6,
        elif (u[i]>='p' and u[i]<='s') or (u[i]>='P' and u[i]<='S'):
            print 7,
        elif (u[i]>='t' and u[i]<='v') or (u[i]>='T' and u[i]<='V'):
            print 8,
        elif (u[i]>='w' and u[i]<='z') or (u[i]>='W' and u[i]<='Z'):
            print 9,
u=raw_input('Please enter a string: ')
getNumber(u)
"""
#6:
"""
def reverse(s):
    s1=list(s)
    s1.reverse()
    print ''.join(s1)
a=raw_input('Please enter a string: ')
reverse(a)
"""
#7
"""
def checkCard(card_num):
    card_list = list(card_num) # 将字符串转为列表方便计算
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2  # 将所有位数*2
        if res >= 10:
            res_1 = res % 10  # 拿到的个位
            res_2 = res // 10# 拿到的十位
            res_3 = res_2 + res_1
            Res += res_3
        else:
            Res += res

        if i % 2 !=0: # 加和所有奇数位置
            Res_2 += int(card_list[i])

    RES = Res + Res_2
    if RES % 10 == 0:
        print('合法')
    else:
        print('不合法')
card_num = '438857601840707'
checkCard(card_num)
"""
#8:woring
"""
def string(s): 
    n=10-len(((s[0]+s[2]+s[4]+s[6]+s[8]+s[10])+(s[1]+s[3]+s[5]+s[7]+s[9]+s[11])*3))%10
    m=list(s)
    m.append(n)
    print m
a=raw_input('Please enter the first 12 digits of an ISBN-13 as a string: ')
string(a)
"""    
#8:zhengque
"""
def checkISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        SUM += res

    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print(RES)

str_ = input('Please enter the first 12 digits of an ISBN-13 as a string: ')
checkISBN(str_)
"""



