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