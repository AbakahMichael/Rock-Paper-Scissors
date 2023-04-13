import random

rock = """
_______
---' ____)
(_____)
(_____)
(____)
---.__(___)
"""
paper = """
_______
---' ____)____
______)
_______)
_______)
---.__________)
"""
scissors = """
_______
---' ____)____
______)
__________)
(____)
---.__(___)
"""

# This function takes in a move as a parameter and returns the corresponding ASCII art based on the move.
def printMove(move):
    if move == 'rock':
        return rock
    if move == 'paper':
        return paper
    if move == 'scissors':
        return scissors

# This function takes in the player's name as a parameter and asks the player to input their move. It returns the player's move as a string.
def makePlayerMove(name):
    fPlayerMove = input("Choose rock, paper, or scissors: ").lower()        #takes input
    playerArt = printMove(fPlayerMove)                                       
    print(name + " chose: " + fPlayerMove)                                  #prints chosen name + their choice
    print(playerArt)                                                        #followed by the ascii art
    return fPlayerMove

# This function takes in the computerName as a parameter and generates a random number between 1 and 3 to determine the computer's move. It returns the computer's move as a string.
def makeComputerMove(cName):
    computerMoveNum = random.randint(1,3)                                   #inclusive
    if computerMoveNum == 1:
        fComputerMove = 'rock'
    elif computerMoveNum == 2:
        fComputerMove = 'paper'
    else:
        fComputerMove = 'scissors'
    computerArt = printMove(fComputerMove)                                   
    print(cName + " chose: " + fComputerMove)                               #same as in makePlayerMove,
    print(computerArt)                                                      #except computerName is always 'Computer'
    return fComputerMove

# This function takes in the playerMove and computerMove as parameters and returns the winner as a string.
def checkRoundWinner(pMove, cMove):
    if pMove == 'rock' and cMove == 'scissors':                             #hardcoding each way for the player to win
        return "player"                                                     #rock beats scissors, etc
    elif pMove == 'paper' and cMove == 'rock':
        return "player"
    elif pMove == 'scissors' and cMove == 'paper':
        return "player"
    elif pMove == cMove:
        return "tie"
    else:                                                                   #this covers all three ways the computer can win
        return "computer"                                                   #instead of rewriting the ways for the player to win

# The main function is the main driver for the game. It uses a while loop to keep playing until either the player or the computer wins the best out of three.
def main():
    # Inputs
    playerName = input("Enter player name: ")
    computerName = "Computer"
    # Score Variables
    playerScore = 0
    computerScore = 0
    # While loop
    while playerScore < 2 and computerScore < 2:                            #if a score is 2, that player wins
        print("---------------")                                            #clearly separates each round
        print("Round Start")
        playerMove = makePlayerMove(playerName)                             #makes each move
        computerMove = makeComputerMove(computerName)
        roundWinner = checkRoundWinner(playerMove, computerMove)            #determines winner with above conditionals
        if roundWinner == "player":                                         #roundWinner == 'player' iff they played rock vs scissors, etc
            playerScore += 1                                                #increment score
            print(playerName + " wins the round!")
        elif roundWinner == "computer":
            computerScore += 1
            print(computerName + " wins the round!")
        else:                                                               #nothing happens to the scores, and a new round starts
            print("It's a tie!")                                                
        print("Score: " + playerName + ": " + str(playerScore) + " - " + computerName + ": " + str(computerScore))
    # Who won at the end                                                    #example output: 'Score: hoontr: 1 - Computer: 0'
    if playerScore > computerScore:                                         #equivalent to: if playerScore == 2
        print(playerName + " wins the game!")                               #as one of the scores has to be 2 for the loop to stop
    else :
        print('Computer wins the game!')
main()                                                                      #actually runs the code since everything else is in functions