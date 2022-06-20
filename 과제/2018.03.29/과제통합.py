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
    
    
# P. 138

X = 7

print("Game start!\n\n게임을 종료하고싶으시면 0을 입력하세요.")

Guess = int(input("예상 수 입력(범위: 1 ~ 100) :"))

while Guess != 7 :
    
    if Guess == X :
        print("WIN!")
        
    elif X < Guess and Guess <= 100 :
        print ("고정 수 보다 큽니다")
        
    elif 1 <= Guess and Guess < X :
        print("\n고정 수 보다 작습니다")
        
    else :
        print("범위를 넘어갔습니다!")
    
    Guess = int(input("예상 수 입력(범위: 1 ~ 100) :"))
    
print("WIN!")