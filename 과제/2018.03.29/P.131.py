# P. 131

import math

print("이차 방정식(aX^2 + bX + c = 0) 에 들어갈 a, b, c 값을 입력해 주십시오.")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
d = b * b - 4*a*c

if a == 0 :
    print("X =",-c/b)
    
elif d == 0 :
    print("X =", -b / (2.0 * a))
    
elif d < 0 :
    print("실근이 존재하지 않습니다.")
    
else :
    print("X =", (-b + math.sqrt(d)) / (2.0 * a))
    print("Or, X =",  (-b - math.sqrt(d)) / (2.0 * a))
    


#도전과제

print("이차 방정식(aX^2 + bX + c = 0) 에 들어갈 a, b, c 값을 입력해 주십시오.")
a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))

i = -10000
while i != 10000 :
    x = a*i*i + b*i + c
    if x == 0:
        print("X =",i)
        
        print("이차 방정식(aX^2 + bX + c = 0) 에 들어갈 a, b, c 값을 입력해 주십시오.")
        a = float(input("a:"))
        b = float(input("b:"))
        c = float(input("c:"))
        
    else :
        i += 1
print("실근이 존재하지 않습니다")