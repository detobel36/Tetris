import random
import time
import turtle

"""""""""""""""""""""""""""""""""""""""""""""""""""
                   Paramètres
"""""""""""""""""""""""""""""""""""""""""""""""""""

SIZE_COL = 10
SIZE_LIGNE = 20
SIZE_CASE = 15
PRECISION = 5
WAIT_TIME = 0.5/PRECISION
COLOR = ["red", "green", "yellow", "purple", "orange", "blue", "gray"]


"""""""""""""""""""""""""""""""""""""""""""""""""""
                Piece du Tetrice
"""""""""""""""""""""""""""""""""""""""""""""""""""
def getAllPiece():
    return [
            [
                [0, 1, 0],
                [1, 1, 1]
            ],
            [
                [2, 2, 2, 2]
            ],
            [
                [3, 3, 0],
                [0, 3, 3]
            ],
            [
                [0, 4, 4],
                [4, 4, 0]
            ],
            [
                [5, 0, 0],
                [5, 5, 5]
            ],
            [
                [0, 0, 6],
                [6, 6, 6]
            ],
            [
                [7, 7],
                [7, 7]
            ]
        ]

def getRandomPiece():
    allPiece = getAllPiece()
    randInt = random.randint(0, len(allPiece)-1)
    return allPiece[randInt]

def inversePiece(piece):
    global currentColonne
    global SIZE_COL

    colPiece = len(piece[0])
    newColPiece = len(piece)
    if(currentColonne+newColPiece > SIZE_COL):
        currentColonne -= newColPiece - colPiece

    nouvellePiece = [[0 for i in range(len(piece))] for i in range(len(piece[0]))]
    for ligne in range(len(piece)):
        for col in range(len(piece[ligne])):
            nouvellePiece[col][len(piece)-1 - ligne] = piece[ligne][col]
    return nouvellePiece


"""""""""""""""""""""""""""""""""""""""""""""""""""
                 Piece ET Matrice
"""""""""""""""""""""""""""""""""""""""""""""""""""

def isFree(SIZE_COL, SIZE_LIGNE, piece, matTetrice, ligne, colonne):
    tailleLignePiece = len(piece)
    tailleColPiece = len(piece[0])

    if(ligne+tailleLignePiece > SIZE_LIGNE or ligne < 0):
        return False
    else:
        for lig in range(len(piece)):
            for col in range(len(piece[lig])):
                if(piece[lig][col] >= 1 and matTetrice[ligne+lig][colonne+col] >= 1):
                    return False
    return True

def placePieceTetrice(piece, matTetrice, ligne, colonne):
    for lig in range(len(piece)):
        for col in range(len(piece[lig])):
            if(piece[lig][col] >= 1):
                matTetrice[ligne+lig][colonne+col] = piece[lig][col]

def fullLine(matTetrice):
    for ligne in range(len(matTetrice)):
        allEqualsToOne = True
        for colonne in range(len(matTetrice[ligne])):
            if(matTetrice[ligne][colonne] == 0):
                allEqualsToOne = False
                break

        if(allEqualsToOne):
            return ligne

    return -1

def removeMatTetrice(numLigne, matTetrice):
    newMatrice = [[0 for i in range(len(matTetrice[0]))]]
    for ligne in range(len(matTetrice)):
        if(ligne != numLigne):
            newMatrice.append(matTetrice[ligne])
    return newMatrice


"""""""""""""""""""""""""""""""""""""""""""""""""""
                       Turtle
"""""""""""""""""""""""""""""""""""""""""""""""""""

def drawPiece(ligne, colonne, piece, SIZE_CASE):
    global COLOR
    for i in range(len(piece)):
        for j in range(len(piece[i])):
            if(piece[i][j] >= 1):
                couleur = COLOR[piece[i][j]-1]
                turtleDrawCarre(SIZE_CASE, ligne+i, colonne+j, couleur)

def drawNextPiece(SIZE_LIGNE, SIZE_CASE, piece):
    drawPiece(SIZE_LIGNE-5, -5, piece, SIZE_CASE)

    turtle.color("white")
    turtle.up()
    turtle.goto(-(SIZE_CASE*5), -SIZE_CASE*(SIZE_LIGNE-2))
    turtle.down()
    turtleDrawContenuCarre(4*SIZE_CASE)


def turtleDrawCarre(SIZE_CASE, ligne, colonne, color):
    turtle.up()
    turtle.goto(SIZE_CASE*colonne, -SIZE_CASE*(ligne+1))
    turtle.down()

    turtle.begin_fill()
    turtle.color("white")
    turtleDrawContenuCarre(SIZE_CASE)
    turtle.end_fill()

    turtle.up()
    turtle.forward(1)
    turtle.right(90)
    turtle.forward(1)
    turtle.right(270)
    turtle.down()
    
    turtle.color(color)
    turtle.begin_fill()
    turtleDrawContenuCarre(SIZE_CASE-2)
    turtle.end_fill()

def turtleDrawContenuCarre(taille):
    turtle.forward(taille)
    turtle.right(90)
    turtle.forward(taille)
    turtle.right(90)
    turtle.forward(taille)
    turtle.right(90)
    turtle.forward(taille)
    turtle.right(90)


def drawMatrice(matTetrice, SIZE_CASE):
    global COLOR
    for ligne in range(len(matTetrice)):
        for col in range(len(matTetrice[ligne])):
            if(matTetrice[ligne][col] >= 1):
                couleur = COLOR[matTetrice[ligne][col]-1]
                turtleDrawCarre(SIZE_CASE, ligne, col, couleur)

def drawBorder(SIZE_CASE, SIZE_COL, SIZE_LIGNE):
    turtle.up()
    turtle.goto(0, 0)
    turtle.down()
    turtle.forward(SIZE_CASE*SIZE_COL)
    turtle.right(90)
    turtle.forward(SIZE_CASE*SIZE_LIGNE)
    turtle.right(90)
    turtle.forward(SIZE_CASE*SIZE_COL)
    turtle.right(90)
    turtle.forward(SIZE_CASE*SIZE_LIGNE)

def updateWaitAndReset(timeWait):
    turtle.update()
    if(timeWait > 0):
        time.sleep(timeWait)
    screen.reset()
    turtle.ht()
    turtle.color("white")


"""""""""""""""""""""""""""""""""""""""""""""""""""
                       Menu
"""""""""""""""""""""""""""""""""""""""""""""""""""

def drawMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score):
    global statut

    if(statut == 2):
        viewPauseMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score)
    elif(statut == 3):
        viewEndMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score)

def viewPauseMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score):
    viewPopupMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE)
    turtle.color("white")
    turtle.write("\tScore: " + str(score) + "\n" +
                 "<Esc> pour reprendre la\n" + \
                 "\tpartie", \
                 font=("Arial", 16, "normal"))

def viewEndMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score):
    viewPopupMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE)

    turtle.color("white")
    turtle.write("\tScore: " + str(score) + "\n" +
                 "<Espace> pour rejouer\n" + \
                 "   <Esc>    pour quitter", \
                 font=("Arial", 16, "normal"))

def viewPopupMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE):
    sizeLigne = SIZE_LIGNE*SIZE_CASE
    sizeColonne = SIZE_COL*SIZE_CASE
    sizeMenu = 10*SIZE_CASE
    padding = 10

    turtle.up()
    turtle.goto(-sizeColonne/2, -((sizeLigne/2)+sizeMenu/2))
    turtle.begin_fill()
    turtle.color("gray")
    turtle.down()
    turtle.forward(sizeMenu)
    turtle.right(90)
    turtle.forward(sizeColonne*2)
    turtle.right(90)
    turtle.forward(sizeMenu)
    turtle.right(90)
    turtle.forward(sizeColonne*2)
    turtle.up()
    turtle.end_fill()
    turtle.goto(-sizeColonne/2 + padding, -(sizeLigne/2)-padding)



"""""""""""""""""""""""""""""""""""""""""""""""""""
                       Event
"""""""""""""""""""""""""""""""""""""""""""""""""""

def eventKeyUp():
    global statut
    global currentPiece
    if(statut == 1):
        currentPiece = inversePiece(currentPiece)

def eventKeyDown():
    global statut
    global forceGoDown
    if(statut == 1):
        forceGoDown = True

def eventKeyRight():
    global statut
    global currentColonne
    global currentPiece
    global SIZE_COL

    if(statut == 1 and currentColonne + len(currentPiece[0]) < SIZE_COL):
        currentColonne += 1

def eventKeyLeft():
    global statut
    global currentColonne

    if(statut == 1 and currentColonne > 0):
        currentColonne -= 1

def eventKeyEsc():
    global statut

    if(statut == 1): # Si jeu en cours -> Mettre le jeu en pause
        statut = 2
        
    elif(statut == 2): # Si jeu en pause -> Reprendre la partie
        statut = 1
        
    elif(statut == 3): # Si fin de partie -> Quitter le jeu
        global playAgain
        statut = None
        playAgain = False


def eventKeySpace():
    global statut

    if(statut == 3):
        statut = None
    print("Space")

def addListener(screen):
    screen.onkey(eventKeyUp, "Up")
    screen.onkey(eventKeyDown, "Down")
    screen.onkey(eventKeyLeft, "Left")
    screen.onkey(eventKeyRight, "Right")
    screen.onkey(eventKeyEsc, "Escape")
    screen.onkey(eventKeySpace, "space")
    screen.listen()


"""""""""""""""""""""""""""""""""""""""""""""""""""
                  Partie de Tetrice
"""""""""""""""""""""""""""""""""""""""""""""""""""

# Global variable
currentColonne = None
currentPiece = None
forceGoDown = None
statut = None          # None = non définit, 1 = en cours, 2 = en pause, 3 = fini

def lancerPartie(SIZE_CASE, SIZE_COL, SIZE_LIGNE, WAIT_TIME, PRECISION):
    global currentColonne
    global currentPiece
    global forceGoDown
    global statut

    statut = 1
    score = 0

    # Init matrice
    matTetrice = [[0 for x in range(SIZE_COL)] for x in range(SIZE_LIGNE)]

    # Init variable
    forceGoDown = False
    currentColonne = int(SIZE_COL/2)
    currentPiece = [[]]
    nextPiece = getRandomPiece()

    first = True
    while first or currentLigne > 0:
        first = False

        # Reset for new piece
        currentColonne = int(SIZE_COL/2)
        currentLigne = 0
        currentPiece = nextPiece
        nextPiece = getRandomPiece()
        turtle.ht()
        
        i = 1
        while isFree(SIZE_COL, SIZE_LIGNE, currentPiece, matTetrice, currentLigne, currentColonne):
            if(not forceGoDown):
                drawBorder(SIZE_CASE, SIZE_COL, SIZE_LIGNE);
                drawMatrice(matTetrice, SIZE_CASE)
                drawPiece(currentLigne, currentColonne, currentPiece, SIZE_CASE)
                drawNextPiece(SIZE_LIGNE, SIZE_CASE, nextPiece)
                drawMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score)
                updateWaitAndReset(WAIT_TIME)
                if(statut == 1):
                    if i % PRECISION == 0:
                        currentLigne += 1
                    i = (i+1)%PRECISION
            else:
                currentLigne += 1
        currentLigne -= 1
        forceGoDown = False

        placePieceTetrice(currentPiece, matTetrice, currentLigne, currentColonne)

        numFullLine = fullLine(matTetrice)
        while(numFullLine >= 0):
            matTetrice = removeMatTetrice(numFullLine, matTetrice)
            score += 1
            numFullLine = fullLine(matTetrice)

    statut = 3
    while(statut == 3):
        drawBorder(SIZE_CASE, SIZE_COL, SIZE_LIGNE);
        drawMatrice(matTetrice, SIZE_CASE)
        drawPiece(currentLigne, currentColonne, currentPiece, SIZE_CASE)
        drawMenu(SIZE_LIGNE, SIZE_COL, SIZE_CASE, score)
        updateWaitAndReset(WAIT_TIME)




"""""""""""""""""""""""""""""""""""""""""""""""""""
                    Execution
"""""""""""""""""""""""""""""""""""""""""""""""""""

# Init turtle
screen = turtle.Screen()
screen.bgcolor("black")
turtle.tracer(0, 0)
addListener(screen)

playAgain = True
while(playAgain):
    lancerPartie(SIZE_CASE, SIZE_COL, SIZE_LIGNE, WAIT_TIME, PRECISION)



screen.mainloop()
