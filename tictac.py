from random import randrange

board = "-" * 20
print(board)

def evaluate(board):
    if "xxx" in board:
        print ("Wow, 3 in a row, Congratulations!!!")
        return "x"
    elif "ooo" in board:
        print ("Wow, 3 in a row, Good news but not for you")
        return "o"
    elif "-" not in board:
        print ("Draaaaaaw")
        return "!"
    else:
        print ("The game is not finished")  
        return "-"      

#def move(board, mark, position):
#    board = board[:position- 1] + mark + board[position:]
#    return board

def player_move(board):
    while True:
        player_position = int(input("Choose your position in range 1-20 : "))
        if player_position < 1 or player_position > 20:
            print ("Something went wrong, choose the number in range 1-20 ")
            player_position = int(input("Choose your position in range 1-20 : "))
        elif board[player_position - 1] != "-":
            print ("Something went wrong, this position is already taken")
            player_position = int(input("Choose your position in range 1-20 : "))               
        else:
            board = board[:player_position- 1] + "x" + board[player_position:]
            print(board)
            return board

def pc_move(board):
    pc_position = randrange (21)
    while True:
        #if 3 in row we can not use randrange all the time but only for first move?
        if board[pc_position-1] != "-":
            pc_position = randrange (21) 
        else:
            board = board[:pc_position- 1] + "o" + board[pc_position:]
            print(board)
            return board

def game():
    global board  #UnboundLocalError: local variable 'board' referenced before assignment
    while True:
        board = player_move(board)
        check = evaluate(board)
        if check == "-":
            pass
        else:
            break
        board = pc_move(board)
        check = evaluate(board)
        if check == "-":
            pass
        else:
            break
             
game()

#File "C:\Users\roman\Desktop\test.py", line 80, in <module>
#   game()
#  File "C:\Users\roman\Desktop\test.py", line 55, in game
#    if "xxx" in board:
#TypeError: argument of type 'NoneType' is not iterable