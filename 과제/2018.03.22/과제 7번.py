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
