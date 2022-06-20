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

