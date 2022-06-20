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
