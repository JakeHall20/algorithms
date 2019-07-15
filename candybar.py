
'''
--------------------------------------------------------------------------------
You can do this in any language that runs on Linux.  You can again use two
teammates on the second part of this one.
--------------------------------------------------------------------------------
Part 1.  Each person does this on their own. Moldy Chocolate. Two players take
turns by breaking an m x n chocolate bar, which has one spoiled 1 x 1 square.
Each break must be a single straight line cutting all the way across the bar
along the boundaries between the squares. After each break, the player who broke
the bar last eats the piece that does not contain the spoiled square. The player
left with the spoiled square loses the game.  Is it better to go first or second
in this game?  Explain.

Part 2. The Program. Write an interactive program to play the game with the
computer. Your program should make a winning move in a winning position and a
random legitimate move in a losing position.
--------------------------------------------------------------------------------
Jacob Hall
--------------------------------------------------------------------------------
'''
# pip install numpy
import numpy as np, time
# pip install beautifultable
from beautifultable import BeautifulTable
import os, sys


class ChocolateBar(object):
    def __init__(self, m, n):
        self.chocBar = []
        self.m, self.n = m, n
        self.moldM, self.moldN = 0, 0
        self.createBar(self.m, self.n)
        self.table = self.createPrint()

        self.brokenRows = list()
        self.brokenCols = list()

    def createBar(self, m, n):
        self.chocBar = np.array([[x for x in range(0, n)] for y in range(0, m)])
        #np.copy = copy of an array
        #print(self.chocBar)
        #print('\n')
        #left = np.vsplit(self.chocBar, np.array([4,5]))
        #print(left[0], '\n', left[1])
        self.chooseMoldyPiece(m, n)

    def chooseMoldyPiece(self, m, n):
        self.moldM = np.random.randint(0, m)
        self.moldN = np.random.randint(0, n)

    def getMoldy(self):
        return self.moldM, self.moldN

    def printMoldy(self):
        print('**** MOLDY IS LOCATED AT ****')
        print('({}, {})'.format(self.moldM+1, self.moldN+1))

    def createPrint(self):
        table = BeautifulTable()
        table.set_style(BeautifulTable.STYLE_BOX_DOUBLED)

        for i in self.chocBar:
            k = 0
            while k<1:
                table.append_row([' ' for n in range(0, self.n)])
                k+=1

        # setting the moldy piece to this
        table[self.moldM][self.moldN] = '*'

        return table

    def printTable(self):
        print(self.table)

    def updateTable(self, type, loc):
        print(type, loc)
        # add a check for if the moldy piece is in that row / column
            # left = np.vsplit(self.chocBar, np.array([loc,self.n]))
            # print('breaking off:: ', left[0])
            # if the moldy piece is above, break down
            # if it is below, break up
            # print(loc in self.brokenRows)
        if type == 'row':
            if loc in self.brokenRows:                # if the location has been chosen
                raise ValueError
            else:
                self.brokenRows.append(loc)           # add location to list of chosen values
                if loc-1 < self.moldM:                # if the moldy piece is below
                    print('moldy is below, breaking up')
                    i, loop = 1, True
                    while (loop):                     # updating the board
                        self.brokenRows.append(loc-i)
                        self.table[loc-i] = ['#' for n in range(0, self.m)]
                        if (loc-i) == 0:
                            loop = False
                        i+=1
                elif loc-1 > self.moldM:
                    print('moldy is above, breaking down')
                    i, loop = 0, True
                    while (loop):
                        self.brokenRows.append(loc-i)
                        self.table[loc-1 + i] = ['#' for n in range(0, self.m)]
                        if (loc+i) == self.m:
                            loop = False
                        i+=1
                else:
                    print('moldy is on this row')


            time.sleep(1)
        elif type == 'column':
            # checking if location has been chosen before
            if loc in self.brokenCols:
                print('val error in cols')
                raise ValueError
            # not been chosen before
            else:
                # add to list of chosen values
                self.brokenCols.append(loc)
                # if moldy is to the right
                if loc-1 < self.moldN:
                    print('moldy to right, breaking left')
                    j, loop = 1, True
                    # updating the board from col[loc] to the first column
                    while (loop):
                        for i in range(0, self.m):
                            self.table[i][loc-j] = '#'
                        if (loc-j) == 0:
                            loop = False
                        j += 1
                # if moldy is to the left
                elif loc-1 > self.moldN:
                    print('moldy to left, breaking right')
                    j, loop = 0, True
                    # updating the board from col[loc-1] to the last column
                    while (loop):
                        for i in range(0, self.m):
                            self.table[i][loc-1 + j] = '#'
                        if (loc+j) == self.n:
                            loop = False
                        j += 1
                else:
                    print('moldy piece is on this column')
                    # ask if they are sure they want this moldy ass piece
                    # if yes, game is over, they lose.

                    # else, raise a value error to send them back to choose 1
                    # or 2 again.


        time.sleep(1)



class Computer(object):
    def __init__(self, m, n, cBar):
        self.m, self.n = m, n
        self.ChocolateBarRef = cBar
        self.moldM, self.moldN = self.ChocolateBarRef.getMoldy()

        # print('comp mold: {} {}'.format(self.moldM+1, self.moldN+1))

    def breakPiece(self):
        # depending on where the moldy piece is,
        # choose one to the right or left( if picking a column )
        # or choose one above or below ( if breaking by a row )
        # if neither of these, choose the next best option.
        r_or_c = np.random.randint(1, 3)
        # print('** r_or_c **', r_or_c)
        # try except for this -- check if it has been chosen before
        if r_or_c == 1:
            _type = 'row'
            _val = self.moldM + 2
            if _val == self.moldM and _val+1 <= self.m:     # checking if the piece to choose is the moldy piece
                _val += 1
            elif _val == self.moldM and _val+1 > self.m:
                _val -= 1
            else:
                _val = _val

        elif r_or_c == 2:
            _type = 'column'
            _val = self.moldN + 2
            if _val == self.moldN and _val+1 <= self.n:
                _val += 1
            elif _val == self.moldN and _val+1 > self.n:
                _val -= 1
            else:
                _val = _val

        else:
            raise ValueError

        print('breaking {} {}'.format(_type, _val))
        self.ChocolateBarRef.updateTable(_type, _val)

class Player(object):
    def __init__(self, m, n, cBar):
        self.m, self.n = m, n
        self.ChocolateBarRef = cBar


    def breakPiece(self):
        keepGoing = True
        while keepGoing:
            try:
                r_or_c = int(input())
                if r_or_c != 1 and r_or_c != 2:
                    raise ValueError
                else:
                    if r_or_c == 1:
                        _type = 'row'
                    elif r_or_c == 2:
                        _type = 'column'
                    else:
                        raise ValueError
                    ####################
                    _val = int(input('What {} would you like to break off?\n'.format(_type)))
                    time.sleep(1)
                    ####################
                    # print('rows: {} columns: {}'.format(self.m, self.n))
                    print('type: ', _type)
                    ####################
                    if _type == 'row':
                        if _val > self.m or _val < 0:
                            raise ValueError

                    elif _type == 'column':
                        if _val > self.n or _val < 0:
                            raise ValueError

                    else:
                        print('else val error')
                        raise ValueError
                    ####################
                    # print('breaking off: {} {}'.format(_type, _val))
                    self.ChocolateBarRef.updateTable(_type, _val)
                    time.sleep(1)
                    keepGoing = False

            except ValueError:
                print('Value Error Raised, re-enter correct input.')


class Game(object):
    def __init__(self):
        self.whoseTurn = 0
        self.isGameOver = False
        self.m, self.n = 10, 10
        self.bar = ChocolateBar(self.m, self.n)

        self.player = Player(self.m, self.n, self.bar)
        self.computer = Computer(self.m, self.n, self.bar)
        self.gameInfo()

    def gameInfo(self):
        print('{:*^40s}'.format('CHOCOLATE BAR GAME'))
        print('{:<20s}'.format('Breaking off a row or column will break off'))
        print('{:<20s}'.format('the entire row/column.\n'))
        self.bar.printMoldy()

        print('\n')
        print('{:^40s}'.format('Options for input are:\n'))
        print('{:<40s}'.format('Row:\t\tAn integer between {} and {}'.format(1, self.m)))
        print('{:<40s}'.format('Column:\t\tAn integer between {} and {}\n'.format(1, self.n)))
        print('{:^40s}'.format('Commands:\n'))
        print('{:<40s}'.format('{}\t\t{}').format('!help', 'Brings up this menu.'))
        print('{:<40s}'.format('{}\t\t{}').format('!quit', 'Closes the game.'))
        print('{:<40s}'.format('{}\t{}').format('!restart', 'Restarts the game.'))
        print('{:<40s}'.format('{}\t\t{}').format('!start', 'Starts the game.'))
        print('\n')

        # get input, start the game whatever
        userInput = input()
        if userInput == "!help":
            self.gameInfo()
        elif userInput == "!quit":
            raise ValueError
        elif userInput == "!restart":
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif userInput == "!start":
            self.bar.printTable()
            self.bar.printMoldy()
            self.choice()
            self.play()

    def choice(self):
        notValid = True
        while(notValid):
            try:
                print('Would you like to go first (1) or second (2)?')
                choice = int(input())

                if choice == 1:
                    print('you are first')
                    self.whoseTurn = 1
                elif choice == 2:
                    print('comp is first')
                    self.whoseTurn = 0
                else:
                    raise ValueError

                notValid = False

            except ValueError:
                print('Invalid Input...\nEnter a valid input. 1 for first; 2 for second.\n')


    def play(self):
        count = 0
        while self.isGameOver == False:
            count += 1
            if self.whoseTurn == 0:
                self.computer.breakPiece()
                self.bar.printTable()
            else:
                print('Would you like to:\n\t1.) break horizontally (by row)\n\t2.) break vertically (by column)')
                self.player.breakPiece()
                self.bar.printTable()

            self.switchTurn()
            # if for some reason it gets to this point, end the game
            maxNum = max(self.m, self.n)
            if count > maxNum:
                self.isGameOver = True


    def switchTurn(self):
        if self.whoseTurn == 0:
            self.whoseTurn = 1
            print('Your Turn..')
        else:
            self.whoseTurn = 0
            print("Computer's Turn..")



if __name__=="__main__":
    Game()
