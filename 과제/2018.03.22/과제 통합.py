##1. P.118

x = int(input("학점을 입력 하십시오.\n"))

while x != 0 :
    if x >= 95 :
        print("A+ 학점")
    elif x >= 90 :
        print("A0 학점")

    elif x >= 85 :
        print("B+ 학점")
    elif x >= 80 :
        print("B0 학점")

    elif x >= 75 :
        print("C+ 학점")
    elif x >= 70 :
        print("C0 학점")

    elif x >= 65 :
        print("D+ 학점")
    elif x >= 60 :
        print("D0 학점")

    else :
        print("F 학점")

    x = int(input("\n학점을 입력 하십시오.\n"))

print("n\재수강을 축하합니다.")

##2. P.119

age = int(input("나이을 입력해 주십시오.\n"))

while age != 0 :

    if age >= 51 :
        print("노년 입니다.\n")

    elif 50 >= age >= 31 :
        print("정년 입니다.\n")

    elif 30 >= age >= 19 :
        print("청년 입니다.\n")

    elif 18 >= age >= 13 :
        print("청소년 입니다.\n")

    elif 12 >= age :
        print("어린이 입니다.\n")

    age = int(input("나이을 입력해 주십시오.\n"))

print("아직 안태어났군요!")

##3.

x = int(input("첫번째로 계산할 숫자를 입력하세요."))
y = int(input("두번째로 계산할 숫자를 입력하세요."))
a = int(input("연산자를 입력하세요. (덧셈: 1 / 빼기: 2 / 곱하기: 3 / 나누기: 4)"))

while x != 0 :
    if a == 1 :
        print("\n답은",x + y,'\n')

    elif a == 2 :
        print("\n답은",x - y,'\n')

    elif a == 3 :
        print("\n답은",x * y,'\n')

    elif a == 4 :
        print("\n답은",x / y,'\n')

    x = int(input("첫번째로 계산할 숫자를 입력하세요."))
    y = int(input("두번째로 계산할 숫자를 입력하세요."))
    a = int(input("연산자를 입력하세요. (덧셈: 1 / 빼기: 2 / 곱하기: 3 / 나누기: 4)"))

print("이용해 주셔서 감사합니다")

##4.

x = int(input("신장을 입력해 주십시오.(단위: CM)"))

while x != 0:
    if x >= 180 :
        print("\n180CM 이상인 분들은 탑승이 제한됩니다.")

    elif 180 > x >= 120 :
        print("\n탑승 가능하십니다.")

    elif 120 >= x :
        print("\n120CM 이하인 분들은 탑승이 제한됩니다.")

    print("\n ===================== ")
    x = int(input("\n신장을 입력해 주십시오.(단위: CM)"))
    
print("\n이용해 주셔서 감사합니다.")

##5.

x = int(input("\n가고자 하는 층을 입력해 주십시오."))

while x != 0 :
    if x >= 21 :
        print("\n 1. 1호기 탑승 후 10층에서 하차. \n\n 2. 계단으로 11층 까지 올라간 후 2호기 탑승. \n\n 3. 2호기 탑승 후 20층에서 하차. \n\n 4. 계단으로 21층까지 올라간 후 3호기 탑승.\n\n 5. 3호기 탑승 후 원하시는 층인",x,"층 까지 올라가시면 됩니다.")

    elif x >= 11 :
        print("\n 1. 1호기 탑승 후 10층에서 하차. \n\n 2. 계단으로 11층 까지 올라간 후 2호기 탑승. \n\n 3. 2호기 탑승 후 원하시는 층인",x,"층 까지 올라가시면 됩니다")

    elif x >= 1 :
        print("\n 1. 1호기 탑승 후 원하시는 층인",x,"층 까지 올라가시면 됩니다")



    print("\n ===================================")
    x = int(input("\n가고자 하는 층을 입력해 주십시오."))

print("이용해주셔서 감사합니다")

##6.

x = int(input(" 짜장면 몇그릇 원하시나요?"))
print("\n",x,"그릇 주문 받았습니다")

PRI = 3000 * x

y = int(input("\n 몇 층 이신가요?"))

while x != 0 :
    DIL = 3000
    if y >= 21 :
        print("\n 21층 이상은 배달을 하지 않습니다")

    elif y >= 16 :
        ADD = 3000 * 0.3
        print("\n 총 금액은",DIL + ADD + PRI,"원 입니다.")

    elif y >= 11 :
        ADD = 3000 * 0.2
        print("\n 총 금액은",DIL + ADD + PRI,"원 입니다.")

    elif y >= 6 :
        ADD = 3000 * 0.1
        print("\n 총 금액은",DIL + ADD + PRI,"원 입니다.")

    elif y >= 1 :
        ADD = 0
        print("\n 총 금액은",DIL + ADD + PRI,"원 입니다.")

    else :
        print("잘 못 입력하셨습니다.")


    x = int(input("\n 짜장면 몇 그릇 원하시나요?"))
    print("\n",x,"그릇 주문 받았습니다.\n")

    PRI = 3000 * x

    y = int(input("\n 몇 층 이신가요?"))


print("감사합니다")

##7.

x = int(input("\n포인트 점수를 입력하세요"))

while x != 0 :
    if x >= 900 :
        G = str('세제')

    elif x >= 800 :
        G = str('샴푸')

    elif x >= 700 :
        G = str('크리넥스')

    else :
        G = str('물티슈')

    print("\n축하합니다! 귀하의 선물은 \'"+ G +"\'입니다!")

    x = int(input("\n포인트 점수를 입력하세요"))

print("감사합니다")

##8.

age = int(input("\n 나이을 입력하십시오."))
pay = int(input("\n 지불금액을 입력하십시오.(단위: 원)"))

while pay != 0 :
    if age >= 20 :
        pri = 1300

    elif age >= 13 :
        pri = 750

    elif age >= 8 :
        pri = 500

    else :
        pri = 0

    if pay - pri >= 0 :
        print("\n 만",age,"세는 요금이",pri,"원 입니다. 거스름돈은",pay - pri,"원 입니다.")

    else :
        print("\n 만",age,"세는 요금이",pri,"원 입니다. 금액이",pri - pay,"원 부족합니다.")

    age = int(input("\n 나이을 입력하십시오."))

    pay = int(input("\n 지불금액을 입력하십시오.(단위: 원)"))
    

print("감사합니다.")

##9.

x = int(input("\n첫번째 수를 입력해주십시오,\n"))
y = int(input("두번째 수를 입력해주십시오.\n"))
z = int(input("세번째 수를 입력해주십시오.\n"))

while x != 0:
    if x > z and y > z :
        print("큰 두 수의 평균은",(x + y) / 2,"입니다.\n")

    if x > y and z > y :
        print("큰 두 수의 평균은",(x + z) / 2,"입니다.\n")

    if z > x and y > x :
        print("큰 두 수의 평균은",(y + z) / 2,"입니다.\n")

        

    x = int(input("첫번째 수를 입력해주십시오.\n"))
    y = int(input("두번째 수를 입력해주십시오.\n"))
    z = int(input("세번째 수를 입력해주십시오.\n"))

print("감사합니다.")

##10. 카운트 프로그램. 입력한 수를 더한다.

total = 0
print("종료하려면 -1을 입력하세요.")
num = 0
while num != -1:
    num = eval(input("정수를 입력하십시오.: "))
    total += num
    print("Total:", total)

print("종료합니다")



