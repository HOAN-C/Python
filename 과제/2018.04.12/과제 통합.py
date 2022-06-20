
#문제 1
def oddeven(x):
    if x % 2 == 0:
        print("짝수")
        
    else :
        print("홀수")
        
x = int(input())
oddeven(x)

#문제 2
def IsEven(T):
    if T % 2 == 0:
        print("짝수")
        return (T)
    
    else :
        print("홀수")

T = int(input())
IsEven(x)

#문제 3
def year(x):
    if (x % 4 == 0 and x % 10 != 0 and x % 400 == 0) :
        print("윤년")
        
    else :
        print("윤년이 아님")
        
x = int(input())
year(x)

#문제 4
def abs(x):
    if x < 0:
        x *= -1
        
    else :
        x = x
        
    return x

x = int(input())
abs(x)

#문제 5
def ave (x, y):
    A = (x+y) / 2
    
    return A

x = int(input())
y = int(input())
ave(x,y)

#문제 6
def Fac(n):
    a = 1
    while (n > 1) :
        a = a * n
        n = n - 1
    n = a
    return n

n = int(input())
Fac(n)

#문제 7
def Pita(a,b,c):
    if (a > b and a > c) :
        if (a*a == b*b + c*c):
            print("피타고라스 삼각형")
            
        else :
            print("피타고라스 삼각형이 아님")
        
    elif (b > a and b > c) :
        if (b*b == a*a + c*c):
            print("피타고라스 삼각형")
            
        else :
            print("피타고라스 삼각형이 아님")
    
    else :
         if (c*c == a*a + b*b):
            print("피타고라스 삼각형")
        
         else :
            print("피타고라스 삼각형이 아님")

a = int(input())
b = int(input())
c = int(input())
Pita(a,b,c)






