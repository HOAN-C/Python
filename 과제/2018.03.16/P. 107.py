x = int(input("첫 번째 정수"))
y = int(input("두 번째 정수"))

while x != y :
    if (x > y) :
        max = y
    else :
        max = x

    print("더 작은 수는",max)

    print("\n ============ \n")

    x = int(input("첫 번째 정수"))
    y = int(input("두 번째 정수"))

print("두 수는 같습니다. 감사합니다.")
