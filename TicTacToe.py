import random
def drawBoard (board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter ():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print ('Do you want to be X or O?')
        letter = input().upper()
    # the first element is the players letter, the second is the computer's letter
    if letter == 'X' :
        return ['X', 'O']
    if letter == 'O':
        return ['O', 'X']



def whoGoesFirst (letter):
    #let's whoever is X go first
    if letter == 'X':
        return 'computer'
    else:
        return 'player'


def playAgain ():
    print ('do you want to play again?')
    return input().lower().startswith ('y')


def makeMove (board, letter, move):
    board[move] = letter    


def isWinner (bo, le):
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #across top
    (bo[4] == le and bo[5] == le and bo[6] == le) or #across middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or #across bottom
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down right
    (bo[8] == le and bo[5] == le and bo[2] == le) or #down middle
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down left
    (bo[9] == le and bo[5] == le and bo[1] == le) or #diagonal
    (bo[7] == le and bo[5] == le and bo[3] == le)) #diagonal


def getBoardCopy (board) :
    dupeboard = []

    for i in board:
        dupeboard.append (i)
    return dupeboard


def isSpaceFree (board, move):
    return board[move] == ' '


def getPlayerMove (board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split () or not isSpaceFree(board, int(move)):
        print ('What is your move? (1-9)')
        move = input ()
    return int(move)


def chooseRandomMoveFromList(board, movelist):
    possiblemoves = []
    for i in movelist:
        if isSpaceFree (board, i):
            possiblemoves.append(i)
    if len(possiblemoves) != 0:
        return random.choice(possiblemoves)
    else:
        return None


def getComputerMove (board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(1,10):
        copy = getBoardCopy (board)
        if isSpaceFree (copy, i):
            makeMove (copy, computerLetter, i)
            if isWinner (copy, computerLetter):
                return i
    for i in range(1,10):
        copy = getBoardCopy (board)
        if isSpaceFree (copy, i):
            makeMove (copy, playerLetter, i)
            if isWinner (copy, playerLetter):
                return i   
    move = chooseRandomMoveFromList (board, [1,3,7,9])
    if move != None:
        return move
    if isSpaceFree (board, 5):
         return 5
    return chooseRandomMoveFromList (board, [2,4,6,8])

    
def isBoardFull (board):
    for i in range(1,10):
        if isSpaceFree (board, i):
            return False
    return True

                                         
print('Welcome to Tic Tac Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst (computerLetter)
    print ('The ' + turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove (theBoard)
            makeMove (theBoard, playerLetter, move)
            if isWinner (theBoard, playerLetter):
                drawBoard (theBoard)
                print ('Hooray! You Won!')
                gameIsPlaying = False

                
            else:
                if isBoardFull(theBoard):
                    drawBoard (theBoard)                         
                    print ('the game is a tie')
                    break
                else:
                   turn = 'computer'
        else:
            move = getComputerMove (theBoard, computerLetter)
            makeMove (theBoard, computerLetter, move)
            if isWinner (theBoard, computerLetter):
                drawBoard (theBoard)
                print ('You Lost')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard (theBoard)                         
                    print ('The game is a tie')
                    break
                else:
                   turn = 'player'
    if not playAgain():
        break
