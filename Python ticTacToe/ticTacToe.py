#Tic Tac Toe
#Benji Duke

from graphics import *
from math import *

def buildBoard():
    
    boardList = []
    for i in range(1, 10):
        boardList.append(str(i))
    return boardList

def displayBoard(win, numList):
    width = win.getWidth()
    height = win.getHeight()
    
    line1 = Line(Point(width/3, 0), Point(width/3, height))
    line1.draw(win)
    line2 = Line(Point(width*2/3, 0), Point(width*2/3, height))
    line2.draw(win)
    line3 = Line(Point(0, height/3), Point(width, height/3))
    line3.draw(win)
    line4 = Line(Point(0, height*2/3), Point(width, height*2/3))
    line4.draw(win)

    spot1 = Point(width/6, height/6)
    spot2 = Point(width/2, height/6)
    spot3 = Point(width*5/6, height/6)
    spot4 = Point(width/6, height/2)
    spot5 = Point(width/2, height/2)
    spot6 = Point(width*5/6, height/2)
    spot7 = Point(width/6, height*5/6)
    spot8 = Point(width/2, height*5/6)
    spot9 = Point(width*5/6, height*5/6)

    spotList = [spot1, spot2, spot3, spot4, spot5, spot6, spot7, spot8, spot9]

    message1 = Text(spot1, "")
    message2 = Text(spot2, "")
    message3 = Text(spot3, "")
    message4 = Text(spot4, "")
    message5 = Text(spot5, "")
    message6 = Text(spot6, "")
    message7 = Text(spot7, "")
    message8 = Text(spot8, "")
    message9 = Text(spot9, "")

    messageList = [message1, message2, message3, message4, message5, message6, message7, message8, message9]
    
    for i in range(9):

        messageList[i].setText(numList[i])
        messageList[i].draw(win)
        messageList[i].setSize(32)
        
    return messageList

def refreshBoard(messageList, boardList):
    for i in range(9):
        messageList[i].setText(boardList[i])
                               
        
def fillSpot(click, boardList, squareList, turn):

    for i in range(len(squareList)):
        
        if isClicked(squareList[i], click) == True and turn == 0:            
            boardList[i] = "X"
        elif isClicked(squareList[i], click) == True and turn == 1:
            boardList[i] = "O"

    return boardList
        
def isClicked(square, click):
    clicked = False
    x = click.getX()
    y = click.getY()
    
    squareP1 = square.getP1()
    squareP2 = square.getP2()
    
    squareP1X = squareP1.getX()
    squareP1Y = squareP1.getY()
    squareP2X = squareP2.getX()
    squareP2Y = squareP2.getY()

    if x > squareP1X and x < squareP2X and y > squareP1Y and y < squareP2Y:
        clicked = True

    return clicked    

def isLegit(click, boardList, squareList):
    result = False  

    for i in range(len(squareList)):
        if isClicked(squareList[i], click) == True and boardList[i] != "X" and boardList[i] != "O":
            result = True
    #if spot is legit return true
    return result

def gameWon(boardList):
    won = False
    
    if boardList[0] == boardList[1] and boardList[1] == boardList[2]:
        won = True
    elif boardList[3] == boardList[4] and boardList[4] == boardList[5]:
        won = True
    elif boardList[6] == boardList[7] and boardList[7] == boardList[8]:
        won = True
    elif boardList[0] == boardList[3] and boardList[3] == boardList[6]:
        won = True
    elif boardList[1] == boardList[4] and boardList[4] == boardList[7]:
        won = True
    elif boardList[2] == boardList[5] and boardList[5] == boardList[8]:
        won = True
    elif boardList[0] == boardList[4] and boardList[4] == boardList[8]:
        won = True
    elif boardList[2] == boardList[4] and boardList[4] == boardList[6]:
        won = True

    return won
    
def gameOver(turnCount):
    gameOver = False
    if turnCount == 9:
        gameOver = True
    return gameOver

def playGame():
    width = 400
    height = 400
    win = GraphWin("Tic Tac Toe", width, height)
    boardList = buildBoard()
    messageList = displayBoard(win, boardList)

    square1 = Rectangle(Point(0, 0), Point(width/3, height/3))
    square2 = Rectangle(Point(width/3, 0), Point(width*2/3, height/3))
    square3 = Rectangle(Point(width*2/3, 0), Point(width, height/3))
    square4 = Rectangle(Point(0, height/3), Point(width/3, height*2/3))
    square5 = Rectangle(Point(width/3, height/3), Point(width*2/3, height*2/3))
    square6 = Rectangle(Point(width*2/3, height/3), Point(width, height*2/3))
    square7 = Rectangle(Point(0, height*2/3), Point(width/3, height))
    square8 = Rectangle(Point(width/3, height*2/3), Point(width*2/3, height))
    square9 = Rectangle(Point(width*2/3, height*2/3), Point(width, height))

    squareList = [square1, square2, square3, square4, square5, square6, square7, square8, square9]
    
    turnCount = 0
    message = Text(Point(width/2, 20), "")
    message.draw(win)
    
    while gameWon(boardList) == False and gameOver(turnCount) == False:
        if turnCount % 2 == 0:
            message.setText("Player 1 Click")
        elif turnCount % 2 == 1:
            message.setText("Player 2 Click")

        turn = turnCount % 2
        click = win.getMouse()
        while isLegit(click, boardList, squareList) == False:
            message.setText("Invalid. Click again Player " + str(turn + 1))
            click = win.getMouse()
    
        fillSpot(click, boardList, squareList, turn)
        refreshBoard(messageList, boardList)
           
        turnCount += 1

    if gameWon(boardList) == True and turn == 0:
        message.setText("PLAYER 1 WINS!!!")
        message.setSize(32)
    elif gameWon(boardList) == True and turn == 1:
        message.setText("PLAYER 2 WINS!!!")
        message.setSize(32)
    else:
        message.setText("TIE GAME\nGO HOME NOW")
        message.move(0,30)
        message.setSize(32)

def main():
    playGame()

main()
