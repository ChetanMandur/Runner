from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=800, height=800, background="sky blue")


#SETS GLOBAL VARIABLES NEEDED IN THE REST OF THE PROGRAM
def setInitialValues():
    global lastStep , ComboPressed , Qpressed, ComboFailed, stepList
    global playerX, playerY, playerXSize, playerYSize, player, playerSpeed
    global endgoalX, endgoalY, endgoalYSize,endgoalXSize, endgoal , Distance, endgoalSprite
    global playerMult,CurrentAnimationStep, CurrentSprite
    global speedMarks, speedMeter, NoMoveYet, speedMarksImage
    global timeStart, currentTime, Stopwatch, IngameTime
    global backgroundX, backgrondY, background
    
    CurrentAnimationStep = 1
    lastStep = "Right"
    Qpressed = False
    ComboPressed = False
    ComboFailed = False
    NoMoveYet = True
    screen.create_rectangle(0,770, 800,800, fill = "gray", outline = "gray")
    CurrentAnimationStep = 1
    
    ##Speed based elements. Curerent player speed, cool things if you reach a certain speed
    speedMeter = 0
    speedMarks = 0
    speedMarksImage = PhotoImage(file = "images/SpeedMarks.gif")
    Distance = 0

    ##Timer varibles
    timeStart = time()
    currentTime = 0
    IngameTime = 0
    Stopwatch = screen.create_text( 40, 40, text="0", font="Times 25", fill="black")

    ####Sprits
    CurrentSprite = PhotoImage(file = "images/player1/player1F1.gif")
    playerX= 100
    playerY=600
    playerXSize=100
    playerYSize=170
    
    ##This is player varibles
    playerMult = 0
    playerSpeed=0
    player=0

    ##End Goal 
    endgoalY= 600
    endgoalXSize= 100
    endgoalYSize= 170
    endgoal=0
    endgoalSprite = PhotoImage(file = "images/FinishFlag.gif")

    if gameType == "Two Player":
        global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
        global speedMeterTWO,speedMarksTWO,DistanceTWO
        global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
        global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
        global endgoalTWOX, endgoalTWOY, endgoalTWOXSize, endgoalTWOYSize, endgoalTWO, endgoalTWOSprite
        
        CurrentAnimationStepTWO = 1
        lastStepTWO = "Right"
        ComboPressedTWO = False
        ComboFailedTWO = False
        NoMoveYetTWO = True


        ##Speed based elements. Curerent player speed, cool things if you reach a certain speed
        speedMeterTWO = 0
        speedMarksTWO = 0
        DistanceTWO = 0


        ####Sprits
        CurrentSpriteTWO = PhotoImage(file = "images/player2/player2F1.gif")
        playerTWOX= 100
        playerTWOY=200
        playerTWOXSize=100
        playerTWOYSize=170

        ##This is player varibles, in the prototype the player will be a block
        playerTWOMult = 0
        playerTWOSpeed=0
        playerTWO=0

        ##End Goal (Will look better at the end)
        endgoalTWOX= endgoalX
        endgoalTWOY= 200
        endgoalTWOXSize= 100
        endgoalTWOYSize= 170
        endgoalTWO=0
        endgoalTWOSprite = endgoalSprite

    

#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler(event):
    global Qpressed, ComboPressed, ComboFailed, lastStep , playerMult, stepList, playerColour, stepList, CurrentSprite, NoMoveYet
    global gameType

    global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    
    if gameType == "One Player": ###This checks if the player wants to play the one player mode
        if event.keysym in ["Left","Right"]: ###This makes it so only left and right can be pressed
            if event.keysym == lastStep: ###if the key the player just pressed matches the last key they pressed, run this code
                ComboPressed = False ###this tells the game that the combo wasn't pressed
                ComboFailed = True ### and that the combo failed 
                CurrentSprite = PhotoImage(file = "images/player1/player1TRIPPING2.gif") ### replaces the sprite with the trip sprite
                playerMult= 0 ### the players multiplying speed is now 0
                
            else: ###if the player's last move isn't the same as the current move, run this
                ComboPressed = True ### tells the game that a combo has been pressed
                playerMult += 1 ### player multiplyer has been increased 
            lastStep = event.keysym ### the last move has been updated
            
            if NoMoveYet != False: ### checks if the game knows that the user pressed a button
                NoMoveYet = False ### if the game doesn't know, tell it
            

                 
    if gameType == "Two Player": ###This checks if the player wants to play the two player mode
        if event.keysym in ["Left","Right"]: ###This checks if the button just pressed was part of the 1st player's controls
            ###This bit is the exact same as if the player wanted to play one player
            if event.keysym == lastStep:
                ComboPressed = False
                ComboFailed = True
                CurrentSprite = PhotoImage(file = "images/player1/player1TRIPPING2.gif")
                playerMult= 0
            else:
                ComboPressed = True
                playerMult += 1            
            lastStep = event.keysym

            if NoMoveYet != False:
                NoMoveYet = False
                
        if event.keysym in ["a","d"]: ###This checks if the button pressed was apart of the 2nd player's controls
            ###This bit is the same as the first player's code, except it uses the varibles for the second player
            if event.keysym == lastStepTWO:
                ComboPressedTWO = False
                ComboFailedTWO = True
                
                CurrentSpriteTWO = PhotoImage(file = "images/player2/player2TRIPPING2.gif")
                playerTWOMult= 0

            else:
                ComboPressedTWO = True
                playerTWOMult += 1
                
            lastStepTWO = event.keysym
            if NoMoveYetTWO != False:
                NoMoveYetTWO = False           

def updateObjects():
    global ComboPressed , Qpressed, ComboFailed
    global playerX, playerY, playerXSize, playerYSize, playerColour, playerSpeed, CurrentAnimationStep, CurrentSprite
    global endgoalX, endgoalY, endgoalYSize,endgoalXSize
    global Stopwatch,IngameTime


    global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO

    
    if ComboPressed == True: ###If the 1st player pressed the combo, up their speed
        playerSpeed = (1 +  playerMult*0.5)
        

    elif ComboFailed == True: ####If the 1st player messed up the combo, set their speed to nothing
        playerSpeed = 0 + 2* playerMult

    if playerSpeed > 0: ##This checks if the 1st player is currently moving
        
        ####This bit is just for the running animation of the 1st player
        ####It uses a constint growing variable and checks it's remainder when dividing by 3
        ####Doing this method will give a loop
        if CurrentAnimationStep % 3 == 0:
            CurrentSprite = PhotoImage(file = "images/player1/player1F1.gif")
            
        elif CurrentAnimationStep % 3 == 1:
            CurrentSprite = PhotoImage(file = "images/player1/player1F2v2.gif")

        elif CurrentAnimationStep % 3 == 2:
            CurrentSprite = PhotoImage(file = "images/player1/player1F3v2.gif")
            
        CurrentAnimationStep += 1 ###This increasing the constint variable

    if gameType == "Two Player": ###This checks if the player is playing the two player mode
        ###This code is the same as the first player except, it uses varibles for the second player
        if ComboPressedTWO == True:
            playerTWOSpeed = (1 +  playerTWOMult*0.5)
            

        elif ComboFailedTWO == True:
            playerTWOSpeed = 0 + 2* playerTWOMult

        if playerTWOSpeed > 0:

            if CurrentAnimationStepTWO % 3 == 0:
                CurrentSpriteTWO = PhotoImage(file = "images/player2/player2F1.gif")
            
            elif CurrentAnimationStepTWO % 3 == 1:
                CurrentSpriteTWO = PhotoImage(file = "images/player2/player2F2.gif")

            elif CurrentAnimationStepTWO % 3 == 2:
                CurrentSpriteTWO = PhotoImage(file = "images/player2/player2F3.gif")

            CurrentAnimationStepTWO += 1


    ###The stopwatch is updated and deleted here, the only updating part not in "drawObjects"
    screen.delete(Stopwatch)
    Stopwatch = screen.create_text( StopwatchX, StopwatchY, text=str( round(IngameTime,2) ) , font="Times 25", fill="black")

    
def drawObjects():
    global player, endgoal
    global endgoalX
    global playerSpeed, speedMarks, speedMeter, CurrentSprite, NoMoveYet, Distance

    global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global endgoalTWOX, endgoalTWOY, endgoalTWOXSize, endgoalTWOYSize, endgoalTWO, endgoalTWOSprite
    global speedMeterTWO,speedMarksTWO,DistanceTWO
    

    if NoMoveYet == False: ###Checks if a move (throughout the whole match) has been made by player 1
        if ComboPressed == True: ### if the move was a combo, run this
            player = screen.create_image(playerX,playerY, image=CurrentSprite, anchor=N)
        else: ### if it was a failed combo, run this
            player = screen.create_image(playerX,playerY+70, image=CurrentSprite, anchor=N)
    else: ##Run this if a move was not pressed at all (the sprite would act funny without this)
            player = screen.create_image(playerX,playerY, image=CurrentSprite, anchor=N)
         
    endgoalX = endgoalX - playerSpeed ###updates where the endgoal currently is 
    endgoal = screen.create_image(endgoalX,endgoalY, image=endgoalSprite, anchor=N) ####draws in current location

    if gameType == "One Player": ###if the player chose the one player mode, put the speed meter and distance tracker and these points
        speedMeter = screen.create_text( 670, 40, text=str(playerSpeed) + " Pixles per Second", font="Times 20 italic bold", fill = "orange")
        Distance = screen.create_text( 300, 50, text="The finish is " + str(endgoalX - playerX) +"pixles away" , font="Times 15", fill="red")

    if gameType == "Two Player": ###if the player chose the two player mode, put the speed meter,distance tracker and player 1 lable at these points
        speedMeter = screen.create_text( 670, 440, text=str(playerSpeed) + " Pixles per Second", font="Times 20 italic bold", fill = "orange")
        Distance = screen.create_text( 300, 440, text="The finish is " + str(endgoalX - playerX) +"pixles away" , font="Times 15", fill="red")
        PlayerOneLable = screen.create_text( 50, 440, text="Player 1" , font="Times 17 bold", fill="red")
    
    if playerSpeed > 30: ### if the player 1 speed is over 30, put in 'speed marks' (the black lines that you see when going fast)
        speedMarks= screen.create_image(30,600, image=speedMarksImage, anchor=N) 
    else: ### if not, don't put the speed marks on
        speedMarks = 0

    if gameType == "Two Player": ###if the player chose the two player mode, run this aswell
        global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
        global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
        global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
        global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
        global endgoalTWOX, endgoalTWOY, endgoalTWOXSize, endgoalTWOYSize, endgoalTWO, endgoalTWOSprite
        global speedMeterTWO,speedMarksTWO,DistanceTWO
        ###This code is the same as the first player except, it uses varibles for the second player
        
        if NoMoveYetTWO == False:
            if ComboPressedTWO == True:
                playerTWO = screen.create_image(playerTWOX,playerTWOY, image=CurrentSpriteTWO, anchor=N)
            else:
                playerTWO = screen.create_image(playerTWOX,playerTWOY+70, image=CurrentSpriteTWO, anchor=N)
                
        else:
                playerTWO = screen.create_image(playerTWOX,playerTWOY, image=CurrentSpriteTWO, anchor=N)
                
        endgoalTWOX = endgoalTWOX - playerTWOSpeed
        endgoalTWO = screen.create_image(endgoalTWOX,endgoalTWOY, image=endgoalTWOSprite, anchor=N)
        speedMeterTWO = screen.create_text( 670, 40, text=str(playerTWOSpeed) + " Pixles per Second", font="Times 20 italic bold", fill = "orange")
        DistanceTWO = screen.create_text( 300, 50, text="The finish is " + str(endgoalTWOX - playerTWOX) +"pixles away" , font="Times 15", fill="red")
        PlayerTwoLable = screen.create_text( 40, 40, text="Player 2" , font="Times 17 bold", fill="red")
        
        if playerTWOSpeed > 30:
            speedMarksTWO=screen.create_image(30,200, image=speedMarksImage, anchor=N)
        else:
            speedMarksTWO = 0

            
            


def RaceCountdown(): ###This creates the countdown you see before matches
    screen.update()
    MultTimer = 0 
    ###Countdown
    for CrazyCountdown in ["red","yellow","orange"]: 
        
        MultTimer = MultTimer + 1 ##Increases the varible 
        CurrentCountdownNum = 4 - MultTimer ###Takes away MultTimer from 4
        StartingCountdown = screen.create_text( 400, 400, text=str(CurrentCountdownNum), font="Times 40 italic bold", fill = CrazyCountdown) ### draws the current number
        screen.update()
        sleep(1)
        screen.delete(StartingCountdown)
            
    StartingCountdown = screen.create_text( 400, 400, text="Go!", font="Times 40 italic bold", fill = "green") ## After "1", create "Go!"
    screen.update()
    sleep(0.3)
    screen.delete(StartingCountdown)

#RUNS THE GAME 
def runGame():
    RaceCountdown()
    
    setInitialValues()
    global playerSpeed, IngameTime,currentTime, timeStart, Stopwatch, playerColour, playerSpeed, Distance, background
    
    global CurrentSpriteTWO, playerTWOX, playerTWOY, playerTWOXSize, playerTWOYSize
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global CurrentAnimationStepTWO,lastStepTWO,ComboPressedTWO,ComboFailedTWO,NoMoveYetTWO
    global playerTWOMult, playerTWOColour, playerTWOSpeed, playerTWO
    global endgoalTWOX, endgoalTWOY, endgoalTWOXSize, endgoalTWOYSize, endgoalTWO, endgoalTWOSprite
    global speedMeterTWO,speedMarksTWO,DistanceTWO
    global StopwatchX, StopwatchY

    global Pavement, Pavement2, backgroundTWO

    ###Sets the placement of the stopwatch based on how many players
    if gameType == "One Player":
        StopwatchX = 40
        StopwatchY = 40
    if gameType == "Two Player":
        StopwatchX = 400
        StopwatchY = 385
   
    
    if gameType == "One Player": ###Creates the background (not including the pavement) for the one player mode
        backgroundImage = PhotoImage(file = "images/sky.gif")
        backgroundX=500
        backgrondY=0
        background = screen.create_image(backgroundX,backgrondY, image=backgroundImage, anchor=N)
        

    if gameType == "Two Player": ###Creates the background (not including the pavement) for the two player mode
        backgroundImage = PhotoImage(file = "images/sky.gif")
        backgroundX=500
        backgrondY=0
        background = screen.create_image(backgroundX,backgrondY, image=backgroundImage, anchor=N)
        backgroundTWO = screen.create_image(backgroundX,-400, image=backgroundImage, anchor=N)

    if gameType == "Two Player": ###Creates the second player's pavement
        PavementTwo = screen.create_rectangle(0,370, 800,400, fill = "gray", outline = "gray")

    ##Creates the pavement for player one (this code always runs)
    Pavement=screen.create_rectangle(0,770, 800,800, fill = "gray", outline = "gray")
    
    while True:
        if gameType == "One Player": ###If the player chose the one player mode, run this
            ###The timer function
            currentTime = time()
            TimeDifference = currentTime - timeStart
            if TimeDifference >= 0.01:
                IngameTime = IngameTime + 0.01
                timeStart = time()

            updateObjects()
            drawObjects()      
            
            if playerSpeed > 5: ##Player speed slowly goes down
                playerSpeed = playerSpeed - 5
                
            screen.update()
            sleep(0.03)
            screen.delete(endgoal, speedMeter, speedMarks, Distance)
            
            
            if playerX+playerXSize >= endgoalX:
                screen.delete(Stopwatch, Distance, Pavement)
                OnePlayerEnd()
                break

        if gameType == "Two Player":
            ###Same as if the gameType was one player except, it also decreases the 2nd player's speed
            currentTime = time()
            TimeDifference = currentTime - timeStart
            if TimeDifference >= 0.01:
                IngameTime = IngameTime + 0.01
                timeStart = time()

            updateObjects()
            drawObjects()      
            if playerSpeed > 5:
                playerSpeed = playerSpeed - 5

            if playerTWOSpeed > 5:
                playerTWOSpeed = playerTWOSpeed - 5
            screen.update()
            sleep(0.03)
            screen.delete(endgoal, speedMeter, speedMarks, Distance, DistanceTWO, speedMeterTWO, endgoalTWO, speedMarksTWO)
            
            
            if playerX+playerXSize >= endgoalX or playerTWOX+playerTWOXSize >= endgoalTWOX :
                screen.delete(Stopwatch, Distance, Pavement, PavementTwo, player, playerTWO)
                TwoPlayerEnd()
                break
            

##################################################
####POST MATCH STUFF            

def OnePlayerEnd(): ###The endscreen for the one player mode
    global FinishText, Stopwatch
    global MainMenuButton, AgainButton, rating
    screen.delete(endgoal, speedMeter, speedMarks, Distance, player)
    screen.create_rectangle(0,0, 800,800, fill="sky blue")
    
    FinishText=screen.create_text( 400, 350, text="Finish!", font="Times 40 italic bold", fill = "orange")
    Stopwatch = screen.create_text( 400, 400, text="Your time was "+str( round(IngameTime,2) ) , font="Times 25", fill="black")

    AgainButton = Button(root, text = "Again", font = "Times 15", command = AgainButtonPressed, anchor=CENTER )
    AgainButton.pack()
    AgainButton.place( x = 250, y = 500, width=100, height = 50 )

    MainMenuButton = Button(root, text = "Main Menu", font = "Times 15", command = MainMenuButtonPressed, anchor=CENTER )
    MainMenuButton.pack()
    MainMenuButton.place( x = 450, y = 500, width=100, height = 50 )

    ##This code finds the score
    if endgoalXBACKUP == 30000:
        if round(IngameTime,2) <= 4.5:
            rating = screen.create_text( 400, 450, text="You scored 3/3!" , font="Times 25", fill="black")
        elif round(IngameTime,2) <= 6:
            rating = screen.create_text( 400, 450, text="You scored 2/3!" , font="Times 25", fill="black")
            
        elif round(IngameTime,2) <= 7:
            rating = screen.create_text( 400, 450, text="You scored 1/3" , font="Times 25", fill="black")

        else:
            rating = screen.create_text( 400, 450, text="You scored 0/3" , font="Times 25", fill="black")
            
    if endgoalXBACKUP == 35000:
        if round(IngameTime,2) <= 5:
            rating = screen.create_text( 400, 450, text="You scored 3/3!" , font="Times 25", fill="black")
        elif round(IngameTime,2) <= 6:
            rating = screen.create_text( 400, 450, text="You scored 2/3!" , font="Times 25", fill="black")
            
        elif round(IngameTime,2) <= 8:
            rating = screen.create_text( 400, 450, text="You scored 1/3" , font="Times 25", fill="black")

        else:
            rating = screen.create_text( 400, 450, text="You scored 0/3" , font="Times 25", fill="black")

    if endgoalXBACKUP == 40000:
        if round(IngameTime,2) <= 10:
            rating = screen.create_text( 400, 450, text="You scored 3/3!" , font="Times 25", fill="black")
        elif round(IngameTime,2) <= 12:
            rating = screen.create_text( 400, 450, text="You scored 2/3!" , font="Times 25", fill="black")
            
        elif round(IngameTime,2) <= 13:
            rating = screen.create_text( 400, 450, text="You scored 1/3" , font="Times 25", fill="black")

        else:
            rating = screen.create_text( 400, 450, text="You scored 0/3" , font="Times 25", fill="black")
            
def TwoPlayerEnd(): ###The endscreen for the two player mode
    global FinishText, Stopwatch
    global AgainButton, MainMenuButton
    global rating
    rating = 0 ###Sets rating to 0 to help prevent crashing
    screen.delete(endgoal, speedMeter, speedMarks, Distance, DistanceTWO, speedMeterTWO, endgoalTWO, speedMarksTWO, player, playerTWO)
    screen.create_rectangle(0,0, 800,800, fill="sky blue")


    ###Checks which player won
    if playerX+playerXSize >= endgoalX:
        FinishText=screen.create_text( 400, 350, text="Finish! Player 1 Wins!", font="Times 40 italic bold", fill = "orange")
        Stopwatch = screen.create_text( 400, 400, text="Their time was "+str( round(IngameTime,2) ) , font="Times 25", fill="black")

    if playerTWOX+playerTWOXSize >= endgoalTWOX:
        FinishText=screen.create_text( 400, 300, text="Finish! Player 2 Wins!", font="Times 40 italic bold", fill = "orange")
        Stopwatch = screen.create_text( 400, 350, text="Their time was "+str( round(IngameTime,2) ) , font="Times 25", fill="black")       


    AgainButton = Button(root, text = "Again", font = "Times 15", command = AgainButtonPressed, anchor=CENTER )
    AgainButton.pack()
    AgainButton.place( x = 250, y = 500, width=100, height = 50 )

    MainMenuButton = Button(root, text = "Main Menu", font = "Times 15", command = MainMenuButtonPressed, anchor=CENTER )
    MainMenuButton.pack()
    MainMenuButton.place( x = 450, y = 500, width=100, height = 50 )


def AgainButtonPressed ():
    global MainMenuButton, AgainButton, endgoalX
    
    AgainButton.destroy()
    MainMenuButton.destroy()
    screen.delete(FinishText)
    screen.delete(Stopwatch)
    if rating != 0:
        screen.delete(rating)
    
    
    endgoalX = endgoalXBACKUP
    runGame()

def MainMenuButtonPressed ():
    global MainMenuButton, AgainButton
    
    AgainButton.destroy()
    MainMenuButton.destroy()
    screen.delete(FinishText)
    screen.delete(Stopwatch)
    if rating != 0:
        screen.delete(rating)
    IntroScreen()

    
##################################################
####INTRO STUFF
def IntroScreen():
    global OnePlayerButton,TwoPlayerButton, HowToButton,  Title, VersionNum, InstructionsTitle
    global ShortDistance, MediumDistance, LongDistance
    global ControlsHeading,ControlsToldOne,ControlsToldTwo,PlayerOneHowToHeading,PlayerOneHowTo,PlayerOneHowToPART2,PlayerTwoHowToHeading,PlayerTwoHowTo

    TitleImage = PhotoImage(file = "images/Titles/RUNNERTitle.gif")
    
    InstructionsTitle = 0
    ShortDistance = 0
    MediumDistance = 0
    LongDistance = 0

    ControlsHeading = 0
    ControlsToldOne = 0
    ControlsToldTwo = 0
    PlayerOneHowToHeading = 0
    PlayerOneHowTo = 0
    PlayerOneHowToPART2 = 0
    PlayerTwoHowToHeading = 0
    PlayerTwoHowTo= 0
    
    OnePlayerButton = Button(root, text = "One player", font = "Times 15", command = OnePlayerPressed, anchor=CENTER )
    OnePlayerButton.pack()
    OnePlayerButton.place( x = 250, y = 400, width=100, height = 50 )

    TwoPlayerButton = Button(root, text = "Two Player", font = "Times 15", command = TwoPlayerPressed, anchor=CENTER )
    TwoPlayerButton.pack()
    TwoPlayerButton.place( x = 450, y = 400, width=100, height = 50 )

    HowToButton = Button(root, text = "Instructions", font = "Times 15", command = HowToButtonPressed, anchor=CENTER )
    HowToButton.pack()
    HowToButton.place( x = 350, y = 700, width=100, height = 50 )
    
    Title = screen.create_text( 400, 300, text="Runner", font="Arial  40  bold underline", fill = "red")
    VersionNum = screen.create_text( 750, 760, text="v0.8", font="Times 25 italic bold", fill = "red")


def HowToButtonPressed():
    global gameMode, OnePlayerButton,TwoPlayerButton, gameType, currentGM, warning, InstructionsTitle, BackToHome
    global ControlsHeading,ControlsToldOne,ControlsToldTwo,PlayerOneHowToHeading,PlayerOneHowTo,PlayerOneHowToPART2,PlayerTwoHowToHeading,PlayerTwoHowTo
    
    OnePlayerButton.destroy()
    TwoPlayerButton.destroy()
    HowToButton.destroy()
    screen.delete(Title)
    screen.delete(VersionNum)

    
    ControlsHeading = screen.create_text( 83, 60, text="Controls:", font="Arial  25 bold", fill = "red")
    ControlsToldOne = screen.create_text( 280, 100, text="Player 1: Left and Right (Maintain Left and Right combo)", font="Arial  15  bold", fill = "red") 
    ControlsToldTwo = screen.create_text( 220, 130, text="Player 2: A and D (Maintain A and D combo)", font="Arial  15  bold", fill = "red")
    
    PlayerOneHowToHeading = screen.create_text( 130, 300, text="Player 1 Mode:", font="Arial  25  bold", fill = "red")
    PlayerOneHowTo = screen.create_text( 390, 340, text="Pick a distance and try and beat your personal best! Compete against the scores of your rivals!", font="Arial  13 bold", fill = "red")
    PlayerOneHowToPART2 = screen.create_text( 140, 365, text="Try to get a perfect score of 3/3!", font="Arial  13 bold", fill = "red")
    
    PlayerTwoHowToHeading = screen.create_text( 130, 500, text="Player 2 Mode:", font="Arial  25  bold", fill = "red")
    PlayerTwoHowTo= screen.create_text( 325, 540, text="Grab a friend, pick a distance, and race! The first person to reach the end wins!", font="Arial  13 bold", fill = "red")
    
    BackToHome = Button(root, text = "Back", font = "Times 15", command = BackToHomePressed, anchor=CENTER )
    BackToHome.pack()
    BackToHome.place( x = 350, y = 700, width=100, height = 50 )

def BackToHomePressed ():
    global BackToHome, InstructionsTitle
    global ControlsHeading,ControlsToldOne,ControlsToldTwo,PlayerOneHowToHeading,PlayerOneHowTo,PlayerOneHowToPART2,PlayerTwoHowToHeading,PlayerTwoHowTo
    if ShortDistance != 0:
        ShortDistance.destroy()
    if MediumDistance != 0:
        MediumDistance.destroy()
    if LongDistance != 0:    
        LongDistance.destroy()

    if ControlsHeading != 0 and ControlsToldOne != 0 and ControlsToldTwo != 0 and PlayerOneHowToHeading != 0 and PlayerOneHowTo != 0 and PlayerOneHowToPART2 != 0 and PlayerTwoHowToHeading != 0 and PlayerTwoHowTo !=  0:
        screen.delete(ControlsHeading,ControlsToldOne,ControlsToldTwo,PlayerOneHowToHeading,PlayerOneHowTo,PlayerOneHowToPART2,PlayerTwoHowToHeading,PlayerTwoHowTo)
    
    screen.delete(Title)
    screen.delete(InstructionsTitle)
    BackToHome.destroy()
    IntroScreen()

def OnePlayerPressed():
    global gameMode, OnePlayerButton,TwoPlayerButton,HowToButton, gameType, currentGM, warning

    gameType = "One Player"
    print(gameType)

    #Erases all the buttons before starting the main game
    OnePlayerButton.destroy()
    TwoPlayerButton.destroy()
    HowToButton.destroy()
    screen.delete(Title)
    screen.delete(VersionNum)
                         

    DistancePicker()

def TwoPlayerPressed():
    global gameMode, OnePlayerButton,TwoPlayerButton,HowToButton, gameType, currentGM, warning
    gameType = "Two Player"
    print(gameType)

    #Erases all the buttons before starting the main game
    OnePlayerButton.destroy()
    TwoPlayerButton.destroy()
    HowToButton.destroy()
    screen.delete(Title)
    screen.delete(VersionNum)
    
    DistancePicker()

def DistancePicker():
    global ShortDistance, MediumDistance, LongDistance, Title, BackToHome
    ShortDistance = Button(root, text = "30k Pixels", font = "Times 15", command = ShortDistancePressed, anchor=CENTER )
    ShortDistance.pack()
    ShortDistance.place( x = 150, y = 400, width=100, height = 50 )

    MediumDistance = Button(root, text = "35k Pixels", font = "Times 15", command = MediumDistancePressed, anchor=CENTER )
    MediumDistance.pack()
    MediumDistance.place( x = 350, y = 400, width=100, height = 50 )

    LongDistance = Button(root, text = "40k Pixels", font = "Times 15", command = LongDistancePressed, anchor=CENTER )
    LongDistance.pack()
    LongDistance.place( x = 550, y = 400, width=100, height = 50 )

    BackToHome = Button(root, text = "Back", font = "Times 15", command = BackToHomePressed, anchor=CENTER )
    BackToHome.pack()
    BackToHome.place( x = 350, y = 700, width=100, height = 50 )


    Title = screen.create_text( 400, 300, text="Pick a distance", font="Arial 40 italic bold", fill = "red")

def ShortDistancePressed():
    global endgoalX, endgoalXBACKUP
    global gameMode, ShortDistance, MediumDistance,LongDistance, gameType, currentGM, warning
    endgoalX = 30000
    endgoalXBACKUP = 30000 ###This is made so that the game knows what the original distance was (since endgoalX is being tampered with)
    print(endgoalX)
    ShortDistance.destroy()
    MediumDistance.destroy()
    LongDistance.destroy()
    BackToHome.destroy()
    screen.delete(Title)

    currentGM = "Play"
    runGame()

def MediumDistancePressed():
    global endgoalX, endgoalXBACKUP
    global gameMode, ShortDistance, MediumDistance,LongDistance, gameType, currentGM, warning
    endgoalX = 35000 
    endgoalXBACKUP = 35000 ###This is made so that the game knows what the original distance was (since endgoalX is being tampered with)
    print(endgoalX)

    #Erases all the buttons before starting the main game
    ShortDistance.destroy()
    MediumDistance.destroy()
    LongDistance.destroy()
    BackToHome.destroy()
    screen.delete(Title)

    currentGM = "Play"
    runGame()


def LongDistancePressed ():
    global endgoalX, endgoalXBACKUP
    global gameMode, ShortDistance, MediumDistance,LongDistance, gameType, currentGM, warning
    
    endgoalX = 40000
    endgoalXBACKUP = 40000 ###This is made so that the game knows what the original distance was (since endgoalX is being tampered with)
    print(endgoalX)
    
    ShortDistance.destroy()
    MediumDistance.destroy()
    LongDistance.destroy()
    BackToHome.destroy()
    screen.delete(Title)

    currentGM = "Play"
    runGame()



def start():
    global currentGM
    
    currentGM = "intro"
    IntroScreen()




#MAKES THE TKINTER WINDOW CALL THE PROCEDURE start AFTER 0 MILLISECONDS
root.after( 0, start )

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)


screen.pack()
screen.focus_set()
root.mainloop()
