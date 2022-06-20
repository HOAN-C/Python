X = int(input("구입 금액을 입력하시오"))

if X >= 100000 :
    DIS = X*0.05
    SAL = X - DIS
    print("할인금액은 ",DIS, "원 이며, 지불금액은 ", SAL,"원 입니다. ")

else :
    MOR = 100000 - X
    print(MOR, "원 상당의 제품을 더 구입하시면 5% 할인 받습니다")
    
