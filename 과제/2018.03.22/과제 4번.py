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
