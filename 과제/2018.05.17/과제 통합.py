###P.275
         I = 0000111223
     least = 00231222334
leastvalue = 77519559798
         K = 1234234344
       tmp = ???777999


### P.287

board = [['  ' for x in range (3)] for y in range(3)]


while True:
    #게임보드 그리기
    for r in range (3):
        print(" " + board[r][0] + "I " +  board[r][1] + "I " + board[r][2])
        
        if (r != 2):
            print("---I---I---")
            
            
            
    #사용자로부터 좌표 받기
    x = int(input("x좌표 입력"))
    y = int(input("y좌표 입력"))
    
    
    
    #사용자 입력 좌표 검사
    if board[x][y] != '  ':
        print("잘못된 좌표")
        continue
    
    else:
        board[x][y] = 'x '
        
        
    #컴퓨터가 놓을 위치 선정.
    done = False
    if x == y:
        if (x == 0):
            if board[1][1] == '  ' and not done :
                board[1][1] = '0 ';
                    
            elif board[2][2] == '  ' and not done :
                board[2][2] = '0 ';
                
        elif (x == 1):
            if board[0][0] == '  ' and not done :
                board[0][0] = '0 ';
                    
            elif board[2][2] == '  ' and not done :
                board[2][2] = '0 ';
                
        elif (x == 2):
            if board[1][1] == '  ' and not done :
                board[1][1] = '0 ';
                    
            elif board[0][0] == '  ' and not done :
                board[0][0] = '0 ';
                
        
    elif board[y][x] == '  ':
        board[y][x] = '0 ';
            
            
            
    else:
        for i in range (3):
            for j in range (3):
                if board[i][j] == '  ' and not done :
                    board[i][j] = '0 ';
                    done = True
                    break;
                    
                    
### P.289
                    
import random

A = 0
B = 0
C = 0
D = 0
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
                if (r == 0 and c == 0):
                    for A in range(r+1, r):
                        for B in range(c, c+2):
                            if board[A][B]:
                                M += 1
                M = '?'
                print(M, end =" ")
                M = 0
                
                    
            
    
    print()