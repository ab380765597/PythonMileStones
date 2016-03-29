from IPython.display import clear_output


boardTable = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
def display_board(board):
    return '\n\n'.join(format_row(row) for row in board)
    
def format_row(row):
    return '|' + '|'.join('{0:^3s}'.format(x) for x in row) + '|'


def play_Symble(x,y,sign):
    
    if sign=='X' and boardTable[x][y]==' ':
        boardTable[x][y] = 'X'
        return "OK"
    elif sign=='O' and boardTable[x][y]==' ':
        boardTable[x][y] = 'O'
        return "OK"
    else:
        print 'Wrong place! Please reType the rock...'
        return "WRONG"
    


def win_Test(board, sign):
    win = False
    full = True
    for i in range(0,3):
        if board[0][i]==board[1][i]==board[2][i]==sign or board[i][0]==board[i][1]==board[i][2]==sign:
            win = True
    if board[0][0]==board[1][1]==board[2][2]==sign or board[0][2]==board[1][1]==board[2][0]==sign:
        win = True
    if win == True:
        return sign
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j]==' ':
                    full = False
                    break
    if full==True:
        return "F"
    else:
        return "C"
    
def run_Game():
    print display_board(boardTable)
    countTime = 0
    hand1 = 'X'
    hand2 = 'O'
    res = 'C'
    curTurn = hand1
    while (res=='C'):
        if countTime%2==0:
            curTurn = hand1
        else:
            curTurn = hand2
        print "Please enter the location of rock in the board\n"
        x = raw_input("x= ")
        y = raw_input("y= ")
        combined = play_Symble(int(x),int(y),curTurn)
        print display_board(boardTable)
        res = win_Test(boardTable, curTurn)
        if combined != "WRONG":
            countTime+=1
        
    if res=='F':
        print "Tire Game! WOW~"
    else:
        print res+" has win the game!"
        
if __name__ == "__main__":
    print "===Tic Toc Game Start==="
    
    run_Game()
    
    print"===Game Over==="
