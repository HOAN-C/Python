grade = int(input("취득한 총 학점 수는 몇 점 입니까?"))
while grade > 0 :
    if grade >= 140 :
        print("졸업가능")
    else :
        print("졸업불가")

    grade = int(input("취득한 총 학점 수는 몇 점 입니까?"))

print("이용해 주셔서 감사합니다")
