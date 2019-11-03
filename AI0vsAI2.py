
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
games = int(input('Enter the number of matches you want\n'))
m = int(input('Enter the number of rows i.e. m\n'))
n = int(input('Enter the number of columns i.e. n\n'))
k = int(input('Enter the length of the sequence horizontally, vertically, or diagonally that constitutes a win\n'))
winner = 0
user = 1
other = 2


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
def random_place(board,player): 
    selection = possibilities(board) 
    current_loc = rd.choice(selection) 
    board[current_loc] = player
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
            

    elif m != n or k!=m or k!=n:
        if k>min(m,n):
            win = False
            return(win)
        else:
            for x in range(0,m-k+1):
                for y in range(0,n-k+1):
                    win_count = 0
                    for z in range(0,k):
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
        pos = -1
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

        

    elif m != n or k!=m or k!=n:
        if k>min(m,n):
            win = False
            return(win)
        else:
            for x in range(0,m-k+1):
                for y in range(0,n-k+1):
                    step = 0
                    win = True
                    pos = -1
                    for z in range(0,k):
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
                    pos = -1
                    for z in range(0,k):
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





# Checks whether the user has k-1 of their marks in a horizontal row 
def row_check(board, player): 
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
                mark(other,x,pos,board)
                return win
    return win

    
          
  
# Checks whether the player has k-1 of their marks in a vertical row 
def col_check(board, player):
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
            if (step + 1 != k) or (step + 1 == k and pos<0):
                win = False
            if win == True and board[pos,x] == 0 and pos>=0:
                mark(other,pos,x,board)
                return win

    return win
                

                           

    

  
# Checks whether the player has k-1 of their marks in a diagonal 

def diag_check(board, player): 
    win = True
    step = 0
    pos = -1  #To store position where mark can be made
    
    if m == n and m==k:
        for x in range(0,m): 
            if board[x,x] == int(user):
                step = step + 1
                
            elif board[x,x] == 0:
                pos = x
        if ((step + 1) != k) or (step + 1 == k and pos<0):
            win = False
        if win == True and board[pos,pos] == 0 and pos>=0:
            mark(other,pos,pos,board)
            return win


        step = 0
        win = True
        pos = -1
        for x in [0,m-1]: 
            if board[x,m-1-x] == player:
                step = step + 1
            elif board[x,m-1-x] == 0:
                pos = x
        if ((step + 1) != k) or (step + 1 == k and pos<0):
            win = False
        if win == True and board[pos,m-1-pos] == 0 and pos>=0:
            mark(other,pos,m-1-pos,board)
            return win
        return win




    

    elif m != n or k!=m or k!=n:
        if k>min(m,n):
            win = False
            return(win)
        else:
            for x in range(0,m-k+1):
                for y in range(0,n-k+1):
                    step = 0
                    win = True
                    pos = -1
                    for z in range(0,k):
                        if board[x+z,y+z] == player:
                            step = step + 1
                        elif board[x+z,y+z] == 0:
                            pos = z
                    if ((step + 1) != k) or (step + 1 == k and pos<0):
                        win = False
                    if win == True and board[x+pos,y+pos] == 0 and pos>=0:
                        mark(other,x+pos,y+pos,board)
                        return win

          
            for x in range(0,m-k+1):
                for y in range(n-1,k-1):
                    step = 0
                    win = True
                    pos = -1
                    for z in range(0,k):
                        if board[x+z,y+z] == player:
                            step = step + 1
                        elif board[x+z,y+z] == 0:
                            pos = z
                    if ((step + 1) != k) or (step + 1 == k and pos<0):
                        win = False
                    if win == True and board[x+pos,y+pos] == 0 and pos>=0:
                        mark(other,x+pos,y+pos,board)
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
            if player == user:
                board = random_place(board,user)

            elif player == other:
                check = row_mark(board,other)
                if check == True:
                    print("Board after " + str(counter) + " move")
                    print("rm")
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
                    print("cm")
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
                    print("dm")
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue

                    
                check = row_check(board,user)
                if check == True:
                    print("Board after " + str(counter) + " move")
                    print("rc")
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue

                    
                check = col_check(board,user)
                if check == True:
                    print("Board after " + str(counter) + " move")
                    print("cc")
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue

                    
                check = diag_check(board,user)
                if check == True:
                    print("Board after " + str(counter) + " move")
                    print("dc")
                    print(board) 
                    sleep(0.1) 
                    counter += 1
                    winner = int(evaluate(board))
                    if winner != 0:
                        return(winner)
                    continue

                    
                board = random_place(board,other)
                
                
                
            print("Board after " + str(counter) + " move") 
            print(board) 
            sleep(0.1) 
            counter += 1

            winner = int(evaluate(board)) 

            if winner != 0:
                return(winner)
                
                
    

  
# Driver Code
pl1 = 0
pl2 = 0
p1 = 0
p2 = 0
draw = 0
for i in range(0,games):
    how_winner = play_game()

    if how_winner == 1 or how_winner == 2:
        print("Winner is: Player " + str(how_winner))

    elif how_winner == -1:
        print("Game is tie")


    if how_winner == 1:
        pl1 += 1

    elif how_winner == 2:
        pl2 += 1
p1 = pl1/games
p2 = pl2/games
draw = 1 - (p1 + p2)
small = p1
if(p1>p2):
    small = p2
if(small>draw):
    small = draw

print('\n\n\n')
print('Probability of Player 1 winning the game = ' + str(p1) + '\n')
print('Probability of Player 2 winning the game = ' + str(p2) + '\n')
print('Probability of drawing the game = ' + str(draw) + '\n')
print('The smallest probabilities from each game : ')
print(small)
