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
