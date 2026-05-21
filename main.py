from colorama import Fore, Back, Style
import pygame

boardWidth = 7
boardHeight = 6
tileSize = 50
paddingBetween = 5
paddingOutside = 50

RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)


screenHeight = boardHeight*(tileSize+paddingBetween)-paddingBetween+(2*paddingOutside)
screenWidth = boardWidth*(tileSize+paddingBetween)-paddingBetween+(2*paddingOutside)

playerColors = [RED, BLUE]

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

def drawTile(x, y, color):
    xPos = paddingOutside+(y*tileSize+paddingBetween)
    yPos = (x*tileSize)
    pygame.draw.circle(screen, color, (xPos, yPos), tileSize/2)


def drawBoard():
    for i in range(boardHeight):
        for j in range(boardWidth):
            if board[i][j] != "-":
                drawTile(i, j, playerColors[board[i][j]-1])


board = []
currentTurn = 1

bgColor = Back.BLACK
p1Color = Fore.RED
p2Color = Fore.BLUE
textColor = Fore.BLACK
moveSymbol = "@"


def makeBoard():
    for i in range(boardHeight):
        board.append([])
        for j in range(boardWidth):
            board[i].append("-")

def showBoard():
    for i in range(boardWidth):
        print(bgColor+str(i+1), end=" ")
    print("")
    for i in range(boardHeight):
        for j in range(boardWidth):
            if board[i][j]==1:
                print(p1Color+moveSymbol,end=" ")
            elif board[i][j]==2:
                print(p2Color+moveSymbol,end=" ")
            else:
                print(textColor+"-",end=" ")
        print("")



def placePiece(row, col):
    if row<0 or row>boardHeight-1:
        return
    global currentTurn
    if currentTurn==1:
        board[row][col] =  1
        currentTurn = 2
    else:
        board[row][col] =  2
        currentTurn = 1
    

def takeTurn(col):
    for i in range(boardHeight):
        if board[i][col]!="-":
            #print(board[i][col],i,col)
            placePiece(i-1,col)
            return
        elif i==boardHeight-1:
            placePiece(i,col)
            return

def checkWin():
    if checkDiagonal():
        return True
    if checkHorizontal():
        return True
    if checkVertical():
        return True
    return False

def checkVertical():
    for col in range(boardWidth):
        for row in range(boardHeight-3):
            initial = board[row][col]
            if board[row+1][col]==initial and board[row+2][col]==initial and board[row+3][col]==initial and initial!="-":
                #print("V "+str(initial))
                return True
    return False

def checkHorizontal():
    for row in range(boardHeight):
        for col in range(boardWidth-3):
            initial = board[row][col]
            if board[row][col+1]==initial and board[row][col+2]==initial and board[row][col+3]==initial and initial!="-":
                #print("H "+str(initial))
                return True
    return False

def checkDiagonal():
    return False

makeBoard()

running = True
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    showBoard()
    move = int(input(textColor+"Move: "))
    takeTurn(move-1)
    # if checkWin()==True:
    #     print("Winner!")
    #     break
    # print("")
    drawBoard()
    pygame.display.flip()