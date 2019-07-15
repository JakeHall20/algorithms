'''
Write a program based on a version of brute-force pattern matching for playing
the game Battleship on the computer.

The rules of the game are as follows:
-There are two opponents in the game (in this case a human player and the
 computer).
-The game is played on two identical 10 x 10 square boards on which each
 opponent places his or her ships, not seen by the opponent.

-Each player has five ships, each of which occupies a certain number of squares
 on the board:
    a destroyer (two squares)
    a submarine (three squares)
    a cruiser (three squares)
    an aircraft carrier (five squares).
-Each ship is placed either horizontally or vertically, with no two ships
 touching each other.
-The game is played by the opponents taking turns “shooting” at each other’s
 ships.

-The result of each shot is displayed as either a hit or a miss. In case of a
 hit, the player gets to go again and keeps playing until missing.
-The goal is to sink the opponent’s ships before the opponent succeeds in doing
 it first. To sink a ship, all squares occupied by the ship must be hit.

-You can program in any language that I can run on Linux (so anything except
 C#).  You can work with one other person if you want.  You have a full week on
 this one.

'''

'''
# creating a dictionary out of two lists
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
'''

'''

Jacob Hall

'''


# importing modules
import pprint
import numpy as np
from beautifultable import BeautifulTable
import random

# Player Class
class Player(object):
    def __init__(self):
        self.board=[]
        self.shotsTaken = ['0,0']
        self.otherShots = list()
        self.isGameOver = False
        self.pieces = Pieces()

    def shoot(self, shotsTaken):
        self.otherShots = shotsTaken
        correct = False
        while correct == False:
            try:
                self.i, self.j = input('Enter a coordinate seperated by a space: ').split()
                correct = True
            except ValueError:
                print('not a valid input')
            except AttributeError:
                print('not a valid input')


        # check if it's not in the range of the board
        # transfer the a to ascii
        self.otherShots.append(str(str(self.i)+','+str(self.j)))
        self.shotsTaken.append(str(str(self.i)+','+str(self.j)))
        return (self.otherShots)



# Computer Class - Class for the computer opponent.
class Computer(object):
    # overloading the init method
    def __init__(self):
        self.board = []
        self.shotsTaken = ['0,0']        # a list of previous shots that have been taken
        self.otherShots = list()
        self.i = 0
        self.j = 0

        self.isGameOver = False
        self.pieces = Pieces()

    # Brute-Force Method for guessing where a ship might be
    # ** need to add in checks for -- if hit, then --
    # ** add in a shoot method in the Game class, that will return if it is a hit or miss
    def shoot(self, shotsTaken):
        # print('\n')
        self.otherShots = shotsTaken
        # setting the current last shot to be the last element in the shotsTaken list array.
        cur = self.shotsTaken[-1]
        othercur = self.otherShots[-1]
        # print(cur, othercur)

        # cur is formatted as (row, col)
        # this changes them into integers for the following if/else checks.
        self.i = int(cur[0])        # row
        self.j = int(cur[-1])       # col

        # print('last shot taken: ', self.i, self.j)
        # if the game is over
        if(self.i == 9 and self.j == 9):
            print('game over: {},{}'.format(self.i, self.j))
            self.isGameOver == True
        # if the game is not over
        else:

            # if the previous shot was column 9, then reset to the next row and column 0.
            if(self.j == 9):    # if the last j location was 9; the next will be the next row
                self.i += 1     # go one row down
                self.j = 0      # reset j to the first element
                print('Shooting at Space: ', end='')
                print(self.i, self.j)
            # if it is not the end of the board (column-9)
            else:
                self.j += 1
                print('Shooting at Space: ', end='')
                print(self.i, self.j)
        # adding the shot taken to the list.
        self.otherShots.append(str(str(self.i)+','+str(self.j)))
        self.shotsTaken.append(str(str(self.i)+','+str(self.j)))
        return (self.otherShots)
        #print(self.shotsTaken)


# Pieces Class - Stores the game pieces along with the information regarding the pieces
# - Stores length, as well as the status of each ship (sunken or not)
# - Can return information about each location within the length of each ship (if it has been hit or not yet.)
class Pieces(object):
    def __init__(self):
        self.destroyer = list()
        self.submarine = list()
        self.cruiser = list()
        self.aircraft = list()
        self.types = ['destroyer', 'submarine', 'cruiser', 'aircraft']
        self.ships = [self.destroyer, self.submarine, self.cruiser, self.aircraft]
        self.shipDict = dict()

        self.initShips()
        self.shipLocations()

    # checking type , returning the information associated
    # with that type of ship
    def getInfo(self, type):
        if type == "destroyer":
            return 2
        elif type == "submarine":
            return 3
        elif type == "cruiser":
            return 3
        else:
            return 5
    # initialzing the ships, to their respective lenghts
    # only executed at the beginning of the game
    def initShips(self):
        # generating each ship; identified by a '-' for now
        for t in self.types:
            self.shipDict[str(t)] = ['-' for j in range(0, self.getInfo(t))]

    def shipLocations(self):
        locD = [random.randint(0, 10), random.randint(0, 10)]

        print(locD, ':::::')





# game class
# - stores the board
# - handles all game actions
# - checks to see who wins
class Game(object):
    def __init__(self):
        self.c = Computer()
        self.p = Player()

        self.boardMain = [ [i for i in range(0,10)] for j in range(0,10)]        # creating the board
        self.gameOver = False
        self.whoseTurn = 0
        self.shotsTaken = ['0,0']        # a list of previous shots that have been taken

        self.table = self.createBoard()
        self.play()

    def createBoard(self):
        # table for printing
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)
        table.column_headers = [str(chr(i)) for i in range(97, 107)]
        for i in self.boardMain:
            k = 1
            while k <= 1:
                j = i[0]
                table.append_row([' ' for n in range(1, 11)])
                k += 1
        # print(table)
        return table

    def printBoard(self, i, j):
        print(i, j)
        self.table[i][j-1] = 'X'

        ## if hit -- place something, update the list of pieces for whoever got hit
        ## else -- miss
        ## update the board
        ## print it out (the line below does this)
        print(self.table)



    # where the game is being played
    def play(self):
        # if self.c.isGameOver == True or self.p.isGameOver == True:
        while(self.gameOver == False):
            print(self.shotsTaken)
            if(self.whoseTurn == 0):
                self.shotsTaken = (self.c.shoot(self.shotsTaken))
                self.whoseTurn = 1
                #self.updateBoard
                self.printBoard(int(self.shotsTaken[-1][0]), int(self.shotsTaken[-1][-1]))
            else:
                self.shotsTaken = (self.p.shoot(self.shotsTaken))
                self.whoseTurn = 0
                #self.updateBoard
                self.printBoard(int(self.shotsTaken[-1][0]), int(self.shotsTaken[-1][-1]))

if __name__=="__main__":
    g = Game()      # initialzing the game
