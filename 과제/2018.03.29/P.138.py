# P. 138

X = 7

print("Game start!\n\n게임을 종료하고싶으시면 0을 입력하세요.")

Guess = int(input("예상 수 입력(범위: 1 ~ 100) :"))

while Guess != 7 :
    
    if Guess == X :
        print("WIN!")
        
    elif X < Guess and Guess <= 100 :
        print ("고정 수 보다 큽니다")
        
    elif 1 <= Guess and Guess < X :
        print("\n고정 수 보다 작습니다")
        
    else :
        print("범위를 넘어갔습니다!")
    
    Guess = int(input("예상 수 입력(범위: 1 ~ 100) :"))
    
print("WIN!")