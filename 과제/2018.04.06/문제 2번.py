Card_Code = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
i = 0
Check = 0

while Check == 0:
    while (i < 14):
        Card_Code[i] = int(input("카드의 숫자를 입력해주십시오."))
        i += 1

    print("\n 입력하신 코드는",Card_Code,"입니다. 맞으면 1 틀리면 0을 눌러 다시 입력해 주십시오.")
    Check = int(input())

    if Check == 0:
        i = 0

    else :
        i = 14

#1단계 보안 인증
T = 0

for A in range(0,14,2):
    Card_Code[A] = Card_Code[A] * 2
    if Card_Code[A] >= 10:
        Card_Code[A] = Card_Code[A] - 9
        T += Card_Code[A]

    else:
        T += Card_Code[A]

if T == 25:
    print("\n1단계 보안인증 성공.")

else:
    print("\n1단계 보안인증 실패.")


#2단계 보안 인증
T2 = 0

for B in range(1,14,2):
    T2 += Card_Code[B]

if T2 == 35:
    print("\n2단계 보안인증 성공.")

else:
    print("\n2단계 보안인증 실패.")



#보안인증 결과 출력
if ((T + T2) % 10 == 0 and (T + T2) == 60) :
    print("\n보안인증에 성공한 카드 입니다.")

else :
    print("\n보안인증에 실패하셨습니다.")
