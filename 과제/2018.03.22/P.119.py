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
