import random

M = 0

board = [[False for x in range (10)] for y in range (10)]

for r in range(10):
    for c in range(10):
        if( random.random() < 0.3 ):
            board[r][c] = True
            
            
for r in range(10):
    for c in range(10):
        if board[r][c]:
            print("# ", end ="")
                  
                  
        else :
            #중앙 일괄처리
            if (r >= 1 and c >= 1 and 9 > r and 9 > c):
                for A in range(r-1, r+2):
                    for B in range(c-1, c+2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0
                       
            #좌측 상단
            elif (r == 0 and c == 0):
                for A in range(0, 2):
                    for B in range(0, 2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0                 
                
            #우측 상단
            elif (r == 0 and c == 9):
                for A in range(0, 2):
                    for B in range(8, 10):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0         
                
            #좌측 하단
            elif (r == 9 and c == 0):
                for A in range(8, 10):
                    for B in range(0, 2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0
                
            #우측 하단
            elif (r == 9 and c == 9):
                for A in range(8, 10):
                    for B in range(8, 10):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0

            #상단 가장자리
            elif (r == 0 and c > 0 and 9 > c):
                for A in range(r, r+2):
                    for B in range(c-1, c+2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0

            #좌측 가장자리
            elif (r > 0 and 9 > r and c == 0):
                for A in range(r-1, r+2):
                    for B in range(c, c+2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0

            #하단 가장자리
            elif (r == 9 and c > 0 and 9 > c):
                for A in range(r-1, r+1):
                    for B in range(c-1, c+2):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0

            #우측 가장자리
            elif (r > 0 and 9 > r and c == 9):
                for A in range(r-1, r+2):
                    for B in range(c-1, c+1):
                        if board[A][B]:
                            M += 1
                print(M, end =" ")
                M = 0
                   
            else :
                continue;
                
                
                    
            
    
    print()
    
    
