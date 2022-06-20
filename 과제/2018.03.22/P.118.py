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
