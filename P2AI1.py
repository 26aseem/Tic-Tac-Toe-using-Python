
# Tic-Tac-Toe Program using random number and numpy in Python 
#In this game, a human plays with the computer.
#There are two players: Player1 and Player2
#Player 1 is assigned 1 as its mark
#Player 2 is assigned 2 as its mark
#If 1 is returned as winner, it means Player 1 is the winner
#Else if 2 is returned as winner, it means Player 2 is the winner
#Else if -1 is returned as winner, it means the game is a tie
  
# importing all necessary libraries 
import numpy as np 
import random as rd
from time import sleep 

#User inputs
user = int(input('Welcome.\nThe mark of Player 1 is 1 and the mark of Player 2 is 2.\nChoose your Player.\nPress 1 for Player 1 or press 2 for Player 2\n'))
m = int(input('Enter the number of rows i.e. m\n'))
n = int(input('Enter the number of columns i.e. n\n'))
k = int(input('Enter the length of the sequence horizontally, vertically, or diagonally that constitutes a win\n'))
winner = 0
other = 0
if user == 1:
    other = 2
elif user == 2:
    other = 1


# Creates an empty board 
def create_board():
    mat = []
    for i in range(0,m*n):
        mat.append(0)

    final = np.array(mat)  #numpy library is used
    final = final.flatten()
    final = final.reshape(m,n)
    return final

    
  

# Check for empty places on board 
def possibilities(board): 
    l = []     
    for i in range(0,m): 
        for j in range(0,n):
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 


  
# Select a random place for the player 
def random_place(board): 
    selection = possibilities(board) 
    current_loc = rd.choice(selection) 
    board[current_loc] = other
    return(board) 


#mark
def mark(player,x,y,board):
    board[x,y] = player


  
# Checks whether the player has k of their marks in a horizontal row 
def row_win(board, player): 
    for x in range(0,m): 
        win = False
        for y in range(0,n-k+1):
            win_count = 0
            for z in range(y,y+k):
                if board[x,z] == player: 
                    win_count = win_count + 1
            if(win_count == k):
                win = True
                return(True)
        

    return(win) 

  
# Checks whether the player has k of their marks in a vertical row 
def col_win(board, player):
    for x in range(0,n): 
        win =False
        for y in range(0,m-k+1):
            win_count = 0
            for z in range(y,y+k):
                if board[z,x] == player:
                    win_count = win_count + 1
            if(win_count == k):
                win = True
                return(True)

    return(win) 

  
# Checks whether the player has k of their marks in a diagonal 

def diag_win(board, player): 
    win = False
    
    if m == n and m==k:
        win_count = 0
        for x in range(m): 
            if board[x, x] == player: 
                win_count = win_count + 1
        if(win_count == k):
                win = True
                return(win)

        win_count = 0
        for x in range(m): 
            if board[x, m-1-x] == player: 
                win_count = win_count + 1
        if(win_count == k):
                win = True
                return(win) 
        return win
            

    elif m != n:
        if k>min(m,n):
            win = False
            return(win)
        else:
            for x in range(0,m-k+1):
                for y in range(0,n-k+1):
                    win_count = 0
                    for z in (0,k):
                        if board[x+z,y+z] == player:
                            win_count = win_count + 1
                    if(win_count == k):
                        win = True
                        return(True)
            return(win)
                        
        








# Checks whether the player has k-1 of their marks in a horizontal row 
def row_mark(board, player): 
    for x in range(0,m): 
        for y in range(0,n-k+1):
            win = True
            step = 0
            pos = -1  #To store position where mark can be made
            for z in range(y,y+k):
                if board[x,z] == player: 
                    step = step + 1
                elif board[x,z] == 0:
                    pos = z
            if ((step + 1) != k) or (step + 1 == k and pos<0):
                win = False
            if win == True and board[x,pos] == 0 and pos>=0:
                mark(player,x,pos,board)
                return win
    return win

    
          
  
# Checks whether the player has k-1 of their marks in a vertical row 
def col_mark(board, player=other):
    for x in range(0,n): 
        for y in range(0,m-k+1):
            win = True
            step = 0
            pos = -1  #To store position where mark can be made
            for z in range(y,y+k):
                if board[z,x] == player: 
                    step = step + 1
                elif board[z,x] == 0:
                    pos = z
            if ((step + 1) != k) or (step + 1 == k and pos<0):
                win = False
            if win == True and board[pos,x] == 0 and pos>=0:
                mark(player,pos,x,board)
                return win
    return win
                

                           

    

  
# Checks whether the player has k-1 of their marks in a diagonal 

def diag_mark(board, player): 
    win = True
    step = 0
    pos = -1  #To store position where mark can be made
    
    if m == n and m==k:
        for x in range(m): 
            if board[x,x] == player:
                step = step + 1
                
            elif board[x,x] == 0:
                pos = x
        if ((step + 1) != k) or (step + 1 == k and pos<0):
            win = False
        if win == True and board[pos,pos] == 0 and pos>=0:
            mark(player,pos,pos,board)
            return win

        step = 0
        win = True
        for x in [0,m-1]: 
            if board[x,m-1-x] == player:
                step = step + 1
            elif board[x,m-1-x] == 0:
                pos = x
        if ((step + 1) != k) or (step + 1 == k and pos<0):
            win = False
        if win == True and board[pos,m-1-pos] == 0 and pos>=0:
            mark(player,pos,m-1-pos,board)
            return win
        return win

        

    elif m != n:
        if k>min(m,n):
            win = False
            return(win)
        else:
            for x in range(0,m-k+1):
                for y in range(0,n-k+1):
                    step = 0
                    win = True
                    for z in (0,k):
                        if board[x+z,y+z] == player:
                            step = step + 1
                        elif board[x+z,y+z] == 0:
                            pos = z
                    if ((step + 1) != k) or (step + 1 == k and pos<0):
                        win = False
                    if win == True and board[x+pos,y+pos] == 0 and pos>=0:
                        mark(player,x+pos,y+pos,board)
                        return win


                        
            for x in range(0,m-k+1):
                for y in range(n-1,k-1):
                    step = 0
                    win = True
                    for z in (0,k):
                        if board[x+z,y+z] == player:
                            step = step + 1
                        elif board[x+z,y+z] == 0:
                            pos = z
                    if ((step + 1) != k) or (step + 1 == k and pos<0):
                        win = False
                    if win == True and board[x+pos,y+pos] == 0 and pos>=0:
                        mark(player,x+pos,y+pos,board)
                        return win 
            
            return win






  
# Evaluates whether there is a winner or a tie  
def evaluate(board):
    Winner = 0
    for player in [1, 2]: 
        if (row_win(board, player) or col_win(board,player) or diag_win(board,player)):
            Winner = player
            return Winner

    if np.all(board != 0) and Winner == 0: 
        Winner = -1

    return Winner 

def check_cd(board,g,h):
    if board[g,h] == 1 or board[g,h] == 2:
        print("You tried to mark already marked place.\nKindly enter the values again.\n")
        c = int(input('Enter the row which you want to mark \n'))
        d = int(input('Enter the column which you want to mark \n'))
        check_cd(board,c,d)

  





#All required functions are completed and these functions will be further used to run the game  
# Main function to start the game
def play_game(): 
    board, winner, counter = create_board(), 0, 1
    print(board) 
    sleep(0.1) 

    while winner == 0: 
        for player in [1,2]:
            if player == other and counter == 1:
                board = random_place(board)
            elif player == user:
                c = int(input('Enter the row which you want to mark \n'))
                d = int(input('Enter the column which you want to mark \n'))
                check_cd(board,c,d)
                    
                mark(user,c,d,board)

            elif player == other:
                check = row_mark(board,other)
                if check == True:
                    print("Board after " + str(counter) + " move") 
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue
                
                check = col_mark(board,other)
                if check == True:
                    print("Board after " + str(counter) + " move") 
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue
                
                check = diag_mark(board,other)
                if check == True:
                    print("Board after " + str(counter) + " move") 
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue


                    
                board = random_place(board)
                
                
                
            print("Board after " + str(counter) + " move") 
            print(board) 
            sleep(0.1) 
            counter += 1

            winner = int(evaluate(board)) 

            if winner != 0:
                return(winner)
                
                
    

  
# Driver Code
play_again = 1
while(play_again > 0):
    how_winner = play_game()

    if how_winner == 1 or how_winner == 2:
        print("Winner is: Player " + str(how_winner))

    elif how_winner == -1:
        print("Game is tie")


    print("\n\n")
    again = int(input('Do you want to play again?\nPress 1 for Yes and 0 for No.\n'))
    if again == 1:
        play_again = 1
    elif again == 0:
        play_again = 0
