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
