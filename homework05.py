# _*_conding:utf8-

#EP:1
"""
class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def getArea(self):
        area=self.width*self.height
        print area
    def getPerimeter(self):
        perimeter=(self.width+self.height)*2
        print perimeter
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()
Rectangle(3.5,35.7).getArea()
Rectangle(3.5,35.7).getPerimeter()
"""
#EP:2
"""
class Account:
    def __init__(self,id=0,balance=100,annualInterestRate=0,wit=0,de=0):
        self.__id=id
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
        self.__wit=wit
        self.__de=de
    def getMonthlyInterestRate(self):
        monthIntRate=self.__annualInterestRate/100/12
        print monthIntRate
    def getMonthlyInterest(self):
        monthInt=self.__balance*(self.__annualInterestRate/100/12)
        print monthInt
    def withdraw(self):
        w=self.__balance-self.__wit
        print w
        wir=self.__annualInterestRate/100/12
        print wir
        wi=w*wir
        print wi
    def deposit(self):
        d=self.__balance-self.__wit+self.__de
        print d
        dir=self.__annualInterestRate/100/12
        print dir
        di=d*dir
        print di        
a=Account(1122,20000,4.5,2500,3000)
a.getMonthlyInterestRate()
a.getMonthlyInterest()
a.withdraw()
a.deposit()
"""
#EP:3
"""
import math
class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n=n
        self.__side=side
        self.__x=x
        self.__y=y
    def getPerimeter(self):
        print self.__n*self.__side
    def getArea(self):
        area=self.__n*math.pow(self.__side,2)/(4*math.tan(math.pi/self.__n))
        print area
r1=RegularPolygon()
r1.getPerimeter()
r1.getArea()
r2=RegularPolygon(6,4)
r2.getPerimeter()
r2.getArea()
r3=RegularPolygon(10,4,5.6,7.8)
r3.getPerimeter()
r3.getArea()
"""
#EP:4
"""
class Fan:
    def __init__(self,speed,on=False,radius=5,color='blue'):
        self.__speed=speed
        self.__on=on
        self.__radius=radius
        self.__color=color
    def speed(self,SLOW=1,MEDIUM=2,FAST=3):
        print self.__speed
    def fuc(self):
        print self.__on
        print self.__radius
        print self.__color
f1=Fan(3,True,10,'yellow')
f1.speed()
f1.fuc()
f2=Fan(2,False,5,'blue')
f2.speed()
f2.fuc()
"""
#EP:5
"""
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def isSolvable(self,x=0,y=0):
        if self.__a*self.__d-self.__b*self.__c!=0:
            print True
            self.__x=float((self.__e*self.__d-self.__b*self.__f))/(self.__a*self.__d-self.__b*self.__c)
            print self.__x
            self.__y=float((self.__a*self.__f-self.__e*self.__c))/(self.__a*self.__d-self.__b*self.__c)
            print self.__y
        else:
            print '[+] There is no solution to this equation'
a,b,c,d,e,f=eval(raw_input('Please enter six number: '))
l=LinearEquation(a,b,c,d,e,f)
l.isSolvable()
"""
#EP:6
"""
class LinearEquation:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.__x1=x1
        self.__y1=y1
        self.__x2=x2
        self.__y2=y2
        self.__x3=x3
        self.__y3=y3
        self.__x4=x4
        self.__y4=y4
    def isSolvable(self,k1=0,b1=0,k2=0,b2=0,x=0,y=0):
        k1=(self.__y1-self.__y2)/(self.__x1-self.__x2)
        b1=self.__y1-self.__x1*k1
        k2=(self.__y3-self.__y4)/(self.__x3-self.__x4)
        b2=self.__y3-self.__x3*k2
        y=(b2-b1)/(k1-k2)*k1+b1
        x=(b2-b1)/(k1-k2)
        print('The intersecting point is: ({},{})'.format(x,y))
x1,y1,x2,y2=eval(raw_input('Please enter endpoints of the first line segment: '))
x3,y3,x4,y4=eval(raw_input('Please enter endpoints of the second line segment: '))
l=LinearEquation(x1,y1,x2,y2,x3,y3,x4,y4)
l.isSolvable()
"""




