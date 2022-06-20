s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = -1
total1 = 0
total2 = 0
while (i < 13):
    i += 1
    s[i] = int(input('신용카드의 숫자를 입력해주세요. : '))
print(s)
yn = int(input(' 등록한 카드의 번호가 맞습니까? 맞으면 1 아니면 0을 입력하세요. : '))
if (yn == 1):
    for n in range(0,14,2):
        s[n] = s[n]*2
        if(s[n] >= 10):
            s[n] = s[n] - 9
        else:
            s[n] = s[n]
        total1 += s[n]
    for m in range(1,14,2):
        total2 += s[m]
    if (total1 + total2) % 10 == 0:
        print('사용 가능한 신용카드입니다.')
    else:
        print('사용 불가능한 신용카드입니다.')
            
        

else:
    print('프로그램을 다시 실행시켜주십시오.')"""