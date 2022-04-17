def display_board(board):
        print( "", "+---+---+---+", "\n", 
                "|", board[0][0], "|", board[0][1], "|",  board[0][2], "|", "\n",
                "+---+---+---+", "\n",
                "|", board[1][0], "|", board[1][1], "|",  board[1][2], "|", "\n",   
                "+---+---+---+", "\n",
                "|", board[2][0], "|", board[2][1], "|",  board[2][2], "|", "\n",
                "+---+---+---+", "\n",
)

board=[[ 1 , 2 , 3],
       [4, "X", 6],
       [7, 8, 9]]


def enter_move_O():
    move=int(input("what is your move?  "))

    if move <0 or move>9:
        print("please pick a number from 1-9...")
        return enter_move_O()
    
    if move==1:
        if board[0][0]==1:
            board[0][0]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==2:
        if board[0][1]==2 :
            board[0][1]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==3:
        if board[0][2]==3:
            board[0][2]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==4:
        if board[1][0]==4:
            board[1][0]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==5:
        print("please pick another spot...")
        return enter_move_O()
    if move==6:
        if board[1][2]==6:
            board[1][2]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==7:
        if board[2][0]==7:
            board[2][0]="O"   
        else:
            print("please pick another spot...")
            return enter_move_O()   
    if move==8:
        if board[2][1]==8:
            board[2][1]="O" 
        else:
            print("please pick another spot...")
            return enter_move_O()
    if move==9:
        if board[2][2]==9:
            board[2][2]="O"
        else:
            print("please pick another spot...")
            return enter_move_O()

def victory_for_O(board):
    if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
        print("O is the winner!")
        return False
    if board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
        print("O is the winner!")
        return False
    if board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
        print("O is the winner!")
        return False
    if board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
        print("O is the winner!")
        return False
    else:
        return True


def enter_move_X():
    from random import randrange

    move=randrange(1,10)
    print(move)

    
    if move==1:
        if board[0][0]==1:
            board[0][0]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==2:
        if board[0][1]==2:
            board[0][1]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==3:
        if board[0][2]==3:
            board[0][2]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==4:
        if board[1][0]==4:
            board[1][0]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==5:
        if board[1][1]==5:
            board[1][1]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==6:
        if board[1][2]==6:
            board[1][2]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==7:
        if board[2][0]==7:
            board[2][0]="X"   
        else:
            print("please pick another spot...")
            return enter_move_X()   
    elif move==8:
        if board[2][1]==8:
            board[2][1]="X" 
        else:
            print("please pick another spot...")
            return enter_move_X()
    elif move==9:
        if board[2][2]==9:
            board[2][2]="X"
        else:
            print("please pick another spot...")
            return enter_move_X()
    else:
        print("????")

def victory_for_X(board):
    if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
        print("X is the winner!")
        return False
    if board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
        print("X is the winner!")
        return False
    if board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
        print("X is the winner!")
        return False
    if board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
        print("X is the winner!")
        return False
    if board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
        print("X is the winner!")
        return False
    if board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
        print("X is the winner!")
        return False
    if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
        print("X is the winner!")
        return False
    if board[2][0]=="X" and board[1][1]=="X" and board[0][2]=="X":
        print("X is the winner!")
        return False
    else:
        return True
    

display_board(board)

while True:
    enter_move_O()
    display_board(board)
    if victory_for_O(board) == False:
        break
    enter_move_X()
    display_board(board)
    if victory_for_X(board) == False:
        break
    





