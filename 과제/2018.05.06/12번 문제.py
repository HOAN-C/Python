INPUT = int(input("금액을 입력하여 주십시오"))

A = 3 #500원 짜리 동전의 갯수
B = 5 #100원 짜리 동전의 갯수
C = 4 #50원 짜리 동전의 갯수
D = 10 #10원 짜리 동전의 갯수

Coins = [500, 100, 50, 10]
Counts = [A, B, C, D]

if INPUT < (500*A + 100*B + 50*C + 10*D):
    
    
    #동전 처리 함수
    def COIN(COIN, Count): 
        global INPUT
        
        if (INPUT > COIN) or (INPUT == COIN):
            SOL = INPUT//COIN
            
            if (SOL < Count) or (SOL == Count):
                print(COIN,"원 짜리",SOL,"개") 
                
            else :
                SOL = Count
                print(COIN,"원 짜리",SOL,"개")
                
            INPUT = INPUT - COIN*Count
        
        else :
            print(COIN,"원 짜리 0개")
            
    Q = 0
    while Q != 4:
        COIN(Coins[Q], Counts[Q])
        Q += 1


else :
    print(INPUT - (500*A + 100*B + 50*C + 10*D), "원이 부족하여 동작 할 수 없음.")