# ALGORITHM FOR TIC TAC TOE
# Display function to display the game
    # Look at the exercise for idea on how to make it fancy
# User choice function for user input
    # Checking for choices to be digit and within range
    # Checking to see if the position is already filled then move on
# Calling user choice function in turn (X first then O)
# When there are 3 in the row, declare winner

# Assigned Tic-Tac-Toe Board as Matrix
matrix = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

# Board display 
def display():
    for row in range(3):
        for column in range(3):
            print(matrix[row][column], end = " ")
        print()

# Position on the board wheneever each player plays their hand
def position(row, column, player): #(row, column, player character)
    row = int(row)
    column = int(column)
    
    if matrix[row][column] == 'X' or matrix[row][column] == 'O': 
        print("Position already filled.")
        return ticTacToe()

    if matrix[row][column] == '-':
        matrix[row][column] = player

# Assigned 'X' or 'O' to the players after first player picked
def assignedMarks(player1):
    while player1 != 'X' and player1 != 'O':
        print('Wrong input')
        player1 = input('Please pick again to start: ') 
        
    if player1 == 'X': player2 = 'O' # Assigned players their marks
    else: player2 = 'X'

    return(player1, player2)

# Checking 
def checkBoard(player): # Checking to see if the game ended
    if matrix[0][0] == 'X' or matrix[0][0] == 'O':
        if (matrix[0][0] == matrix[0][1] == matrix[0][2]) or (matrix[0][0] == matrix[1][1] == matrix[2][2]) or (matrix[0][0] == matrix[1][0] == matrix[2][0]):
            print(f"Game End! {player} won!")
            return 9
    if (matrix[1][0] == 'X' or matrix[1][0] == 'O') and (matrix[1][0] == matrix[1][1] == matrix[1][2]):
        print(f"Game End! {player} won!")
        return 9
    if matrix[2][0] == 'X' or matrix[2][0] == 'O':
        if (matrix[2][0] == matrix[2][1] == matrix[2][2]) or (matrix[2][0] == matrix[1][1] == matrix[0][2]):
            print(f"Game End! {player} won!")
            return 9
    if (matrix[0][1] == 'X' or matrix[0][1] == 'O') and (matrix[0][1] == matrix[1][1] == matrix[2][1]):
        print(f"Game End! {player} won!")
        return 9
    if (matrix[0][2] == 'X' or matrix[0][2] == 'O') and (matrix[0][2] == matrix[1][2] == matrix[2][2]):
        print(f"Game End! {player} won!")
        return 9
    
    else: 
        count = 0
        for row in range(3): 
            for column in range(3):
                if matrix[row][column] != '-':
                    count += 1
        return count

def resetGame():
    for row in range(3):
        for column in range(3):
            matrix[row][column] = '-'
    

def playGame(gameOver): 
    while gameOver:
        continueGame = input('Would you like to restart the game? Select Y or N: ')
        if continueGame == 'Y' or continueGame =='y': 
            ticTacToe()
        else: 
            print("Have a good day!")
            return 


def ticTacToe():
    player1 = input("Please select either X or O to start: ")

    player = assignedMarks(player1.upper())
    display()

    count = 0
    row = 'x'
    column = 'y'
    withinRange = False 
    gameEnded = False
    
    while withinRange == False and gameEnded == False:
        if count%2 == 0:
            print("PLAYER 1")
            turn = player[0]
            row = input("Please select a row (0, 1, 2): ")
            column = input("Please select a column (0, 1, 2): ")

            if row.isdigit() == False or column.isdigit() == False: 
                print("Sorry that's not a digit!")
            
            if row.isdigit() == True and column.isdigit() == True: 
                if int(row) in range(3) and int(column) in range(3):
                    withinRange = True
                    position(row, column, turn)
                    count += 1
                    display()
                    if checkBoard(turn) == 9: 
                        gameEnded = True
                        resetGame()
                        break
                else: 
                    print("Sorry, you're out of range")
                    pass
    
                withinRange = False

        if count%2 == 1:
            print("PLAYER 2")
            turn = player[1]
            row = input("Please select a row (0, 1, 2): ")
            column = input("Please select a column (0, 1, 2): ")

            if row.isdigit() == False or column.isdigit() == False: 
                print("Sorry that's not a digit!")
            
            if row.isdigit() == True and column.isdigit() == True: 
                if int(row) in range(3) and int(column) in range(3):
                    if matrix[int(row)][int(column)] == 'X' or matrix[int(row)][int(column)] == 'O': 
                        print("Position already filled.")
                        display()
                        pass
                    else:
                        withinRange = True
                        position(row, column, turn)
                        count += 1
                        display()
                        if checkBoard(turn) == 9: 
                            gameEnded = True
                            resetGame()
                            break
                else: 
                    print("Sorry, you're out of range")
                    pass
    
                withinRange = False
        
    return gameEnded 

def start(): 
    gameEnded = ticTacToe()
    playGame(gameEnded)


start()

