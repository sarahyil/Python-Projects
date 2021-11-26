'''
Sarah Yildirim
10/15/2020
My code is for the minesweeper game. This game took me a long look time to code. I actually had
to restart a few times because it kept crashing and the coding wasn't working. I was finally able to get it
to work.  My table group and I worked together a lot on this and it was very helpful. Overall, I enjoyed this project but it was also 
very very stressful at times. Also, I had to use a lot of functions I wasn't previously familiar with and I found them
from the python website. I do wish I had met with Ms. Healey beforehand to work on this, but I had started
too late because I had to restart and it has been a very stressful week (Midterms!). But, I think that I
have everything I need. I was able to fix my code and fix all the errors I found. I changed my code a bit
because I wanted to make the code more easier to read and also I changed how the board printed. I am happy
with the results and this project definitely took a very very long time!
OMH
'''

import os
import random
import math

#this function will clear and exit
def clear():
    os.system('clear')

#this function is for the instructions of the minesweeper game for the user
def instructions(): 
   
    print("\nThis is the minesweeper game!")
    print("\nFor this game, you want to flag all of the bombs with out uncovering them beforehand.")
    print("\nEnter two numbers with a space between them to uncover a cell. Include an 'F' if you want to flag the cell.")

#this function is setting up the size of the board by asking user what they want the side of the board length to be
def size_board():
    global side
    print("\nWhat would you like the side of your board to be?")
    try: 
        side = int(input())
        if side < 3:
            print("\nToo small! Please enter a number greater than 2.")
            size_board()
        elif side > 10:
            print("\nToo large! Please enter a number less than 11.")
            size_board()
    except ValueError:
        print("That is incorrect. Please enter a side length for the board.")
        size_board()

#this function is setting up the display for the user board
def display():
    global flagnumber
    flagnumber = 0
    global display
    display = [["*" for x in range(side)] for y in range(side)]

#this function is setting up the solution board which the user can not see
def solution_board():
    global solution
    solution = [[0 for x in range(side+2)] for y in range(side+2)] #I am making the solution board 2 cells larger

instructions()
size_board()
display()
solution_board()

#this function is the display that the user is going to see
def player_board():
    global space
    space = ' '
    for x in range(side):
        print("\n")
        for y in range(side):
            print(space*10+str(display[x][y]), end="") #this is the viewer board and this is just setting up the board for them

#this function is assigning each bomb a spot on the board
def bombs():
    global differentplace
    global bomb_place
    
    bomb_place = []
    differentplace = []
    for x in range(math.ceil(side*side*0.10)): # I only want 10 percent of the whole board to be bombs
        bomb_place.append([random.randint(1, side), random.randint(1, side)])
    for x in bomb_place:
        if x not in differentplace: #each bomb must be in different cells
            differentplace.append(x) 
    if not len(differentplace) == math.ceil(side*side*0.10):
        bombs()

#this function is filling the board with bombs
def board_fill():
    global solution

    for x in range(len(differentplace)):
        solution[differentplace[x][0]][differentplace[x][1]] = '⦿' 
        #bombs around a cell
    for x in range(side+2): 
        for y in range(side+2):
            if solution[x][y] == '⦿':
                for a in range(x-1, x+2):
                    for b in range(y-1, y+2):
                        if solution[a][b] != '⦿':
                             solution[a][b] += 1
                
    print("\n")            

#this function is for each time the user picks a cell on the board and the game then goes back to these functions
def user_move():
    global display
    global xmove
    global ymove
    global list_move
    global repeat_zeroes

    clear()
    repeat_zeroes = []

    player_board()
    print("\n\nPlease enter a row and column number. There must be a space seperating the two. You may also enter an f at the end inorder to flag/unflag a cell.")
    list_move = input().split() #the list
    ymove = int(list_move[1])
    xmove = int(list_move[0])
    
 #this is when the user wants to uncover a certain cell
    if len(list_move) == 2: 
        try:
            val = list(map(int, list_move)) #there can only be two int
            otherway()
        except ValueError:
            print("Wrong input!")
            user_move() #error check
    elif len(list_move) == 3: #3 inputs meaning the user flags a space
        if list_move[2] != 'F' and list_move[2] != 'f': #make sure the last input isn't a different number/character and is just f
            print("Wrong input!")
            user_move()
        try:
            val = list(map(int, list_move[:2]))
            otherway()
        except ValueError:
            print("Wrong input!")
            user_move()
    else: #this is when the input is more than 3 points or is something else
        print("That won't work. Try again please!!")
        user_move

    if xmove < 1 or xmove > side or ymove < 1 or ymove > side: #input must be within grid limits
        print("Wrong input!")
        user_move()

#this function is for the situation where the user wins and then can play again
def winsituation():
    print("You win!")
    print("Do you want to play again? y/n")
    playagain = str(input())
    if playagain == 'y':
        instructions()
        size_board()
        display()
        user_move()
        player_board()
        solution_board()
        bombs()
        board_fill()
        
    else:
        print("Goodbye!")

#this function is for the situation where the user loses and can play again
def losesituation():
    print("Do you want to play again? y/n")
    playagain = str(input())
    if playagain == 'y':
        instructions()
        size_board()
        display()
        user_move()
        player_board()
        solution_board()
        bombs()
        board_fill()
        
    else:
        print("Goodbye!")

#this function is for when there are two scenarios
def otherway():
    if len(list_move) == 3:
        winning_flags()
    elif len(list_move) == 2:
        show_board()

#this function shows the board when the game ends
def show_board():
    if solution[xmove][ymove] == '⦿': #game ends
        print("Game over!")
        losesituation()
    elif solution[xmove][ymove] == 0: #showing all zeroes
        display[xmove-1][ymove-1] = 0
        touching(xmove, ymove)
    else: 
        display[xmove-1][ymove-1] = solution[xmove][ymove]
        user_move()


#this function is for winning from having had flagged all spaces that don't have bombs
def winning_flags(): #winning from flags
    global flagnumber
    if display[xmove-1][ymove-1] == '⚐':
        display[xmove-1][ymove-1] = '*'
        flagnumber -= 1
        user_move()
    else:
        display[xmove-1][ymove-1] = '⚐'
        flagnumber += 1
        check_win() #checks for wins after flag is placed
        if checkforwin == True:
            winsituation()
        else:
            print("Keep going!")
            user_move()

#this function is calling the show function
def touching(xmove, ymove):
    global display
    global vis
    global solution
    #function call
    if solution[xmove][ymove] == 0: 
        show(xmove, ymove)
    user_move()

#this function is revealing around based on the zeroes and bombs
def show(xmove, ymove):
    global display
    global solution
    global repeat_zeroes

    if [xmove, ymove] not in repeat_zeroes: #this is stopping after no new zeroes are found
        repeat_zeroes.append([xmove, ymove])
        for x in range(xmove-1, xmove+2):
            for y in range(ymove-1, ymove+2):
                if x >= 2 and y >= 2 and x < side+1 and y < side+1:
                    display[x-1][y-1] = solution[x][y]
        

#this function is just checking to see if the user won or not
def check_win():
    global checkforwin
    checkforwin = False
    win_number = 0
    for x in range(side):
        for y in range(side):
            if display[x][y] == '⚐' and solution[x+1][y+1] == '⦿': #checking
                win_number += 1

    if win_number == flagnumber and win_number == math.ceil(side*side*0.10): #checking
        checkforwin = True
    else:
        checkforwin = False


bombs()
board_fill()
user_move()


'''   
Michael: Try and make the board look more aesthetically pleasing. Other than that, your code looks organized and is easy to read.   
What I did: I included the user board function. 

Zoey: Add some more comments to make it more clear what's going on in the game.  
What I did: I added more comments to include what each part is doing.   

Ahmed: Maybe add a board so that it's easier for the player.  
What I did: I made a board for the player.  

'''
