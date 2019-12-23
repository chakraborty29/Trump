#    Whist (4 Players)
#    whist.py
#    Raul Chakraborty
#    Lab Section M6
#    rchakr01

from trumpClass import*
from graphics import*
from random import randrange
########################################################################################
# get your deck
def getDeckOfCards(): #(FNC)
    # set ranks and suits
    ranks="A23456789TJQK"
    suits="♣♦♥♠" 
    
    # set the array to return a deck of cards
    deck=[]
    
    # each rank needs a set of suits for nested loop
    for rank in ranks:
        for suit in suits:
            deck.append(rank+suit)
            
    return deck
# end of get DeckOfCards

def getSuitAndNum(card): return card[0],card[1] # get a suit and the number of the card to compare #(FNC)

# draws card into the hands of the 4 players
def getPlayerHand(): #(FNC)
    # get the deck and then shuffle
    deck=Card(getDeckOfCards()) #(CLOD)
    deck.shuffle()
    
    # get number of players
    numPlayers=4
    
    # get how many cards each player will get
    cardsPerPlayer=int(deck.getDeckInfo('length')/numPlayers)
    
    # player arrays:
    player1=[] #team1
    player2=[] #team2
    player3=[] #team1
    player4=[] #team2
    
    for i in range(cardsPerPlayer):
        # players get one card at a time to get the best shuffle
        player1.append(deck.draw())
        player2.append(deck.draw())
        player3.append(deck.draw())
        player4.append(deck.draw())
    
    return player1,player2,player3,player4
# end of getPlayerHand    
########################################################################################


########################################################################################
# this function is for card that are chosen and put on the middle of the table
def playedCardObj(): #(FNC)
    playedCardArr=[]
    
    # sets up an array of Rectangle objects which can be modified later 
    for i in range(68,99,10):
        playedCardArr.append(Button(Rectangle(Point(i,46),Point(i+7,56)))) #(CLOD)
        
    return playedCardArr

# num is the position of where the card goes based on who played first
def displayedPlayedCard(playerCard,playedCardArr,win,num,color): #(FNC) & #(LOOD)
    playedCardArr[num-1].draw(win)
    playedCardArr[num-1].setFill(color)
    playedCardArr[num-1].setText(playerCard,win) #(OTXT) 
    rank,suit=getSuitAndNum(playerCard)
    # this sets the color of the text of the card based on the suit
    if suit=='♦'or suit=='♥':
        playedCardArr[num-1].setColor("red")
    elif suit=='♠'or suit=='♣':
        playedCardArr[num-1].setColor("black")
    

# displays player 1's card
def getDisplayObj():  #(FNC)
    player1CardArr=[]
    
    # sets up an array of Rectangle objects which can be modified later 
    for i in range(25,154,10):
        player1CardArr.append(Button(Rectangle(Point(i,5),Point(i+7,15)))) #(CLOD)
        
    return player1CardArr
# end of getDisplayObj

def setDisplay(player1,player1CardArr,win): #(FNC)
    # undraw it first because as you use the cards they need to be taken out of the display
    for i in range(len(player1CardArr)): #(LOOD)
        player1CardArr[i].undraw()
        
    for i in range(len(player1)): #(LOOD)
        # draw the card on to the screen
        player1CardArr[i].draw(win)
        player1CardArr[i].setFill("white")
        # then set text to every card
        player1CardArr[i].setText(player1[i],win) #(OTXT) 
        rank,suit=getSuitAndNum(player1[i])
        # this sets the color of the text of the card based on the suit
        if suit=='♦'or suit=='♥':
            player1CardArr[i].setColor("red")
        elif suit=='♠'or suit=='♣':
            player1CardArr[i].setColor("black")
# end of setDisplay

# this is to display the cards of the other players on the screen
def otherCardObj(playerNum): #(FNC)
    # playerNum is to determine which player needs cards ... doing it this way it returns one list at a time
    rectObj=[]
    if playerNum==2:
        for i in range(5,90,7):
            rectObj.append(Button(Rectangle(Point(172,i),Point(162,i+7)))) #(CLOD)
            
    elif playerNum==3:
        for i in range(25,154,10):
            rectObj.append(Button(Rectangle(Point(i,95),Point(i+7,85)))) #(CLOD)
    elif playerNum==4:
        for i in range(5,90,7):
            rectObj.append(Button(Rectangle(Point(5,i),Point(15,i+7)))) #(CLOD)
        

    return rectObj
        
# this displays the cards of the oponents on the screen
def otherCardDisplay(playerHand,playerButtonArr,win,color,show): #(FNC)
    # undraws first because cannot draw on already drawn objects
    for i in range(len(playerButtonArr)): #(LOOD)
        playerButtonArr[i].undraw()
        
    for i in range(len(playerHand)): #(LOOD)
        playerButtonArr[i].draw(win)
        playerButtonArr[i].setFill(color)
        # then set text to every card
        if show:
            playerButtonArr[i].setText(playerHand[i],win) #(OTXT)
            rank,suit=getSuitAndNum(playerHand[i])
            if suit=='♦'or suit=='♥':
                playerButtonArr[i].setColor("red")
            elif suit=='♠'or suit=='♣':
                playerButtonArr[i].setColor("black")
        
# this is to make game() shorter- just removes the buttons so it can be drawn again ... Graphics cannot draw over objects already drawn
def removeTextAfter(playerButtonArr): #(FNC)
    for i in range(len(playerButtonArr)): #(LOOD)
        playerButtonArr[i].undrawText()

# this is to make game() shorter- just removes the buttons so it can be drawn again ... Graphics cannot draw over objects already drawn
def removeOldDisplay(menuButtonArr,playedButtonArr): #(FNC)
    menuButtonArr[0].undraw()
    menuButtonArr[0].undrawText()

    
    for i in range(len(playedButtonArr)): #(FNC) & #(LOOD)
        playedButtonArr[i].undraw()
        playedButtonArr[i].undrawText()
########################################################################################        
         


########################################################################################
def logic(player1Card,player2Card,player3Card,player4Card,setSuit): #(FNC)
    
    # this function will return the point to the team that is wining 
    team1Points=0
    team2Points=0

    # this is to compare the ranking of each card by their index so they are placed in their order
    rankIndex=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    
    # get rank and the suit individually to compare
    player1Rank,player1Suit=getSuitAndNum(player1Card)
    player2Rank,player2Suit=getSuitAndNum(player2Card)
    player3Rank,player3Suit=getSuitAndNum(player3Card)
    player4Rank,player4Suit=getSuitAndNum(player4Card)
    
    
    # check between team members who has the higher card
    # Player 1 and 3 are teammate
    
    # check if they have the same suit and if they do then compare to see who has the higher rank
    if player1Suit==player3Suit:
        # comparing the rank
        if rankIndex.index(player1Rank)>rankIndex.index(player3Rank):
            team1Card=player1Card
        else:
            team1Card=player3Card
    # if they dont have the same rank then go based on if they match the suit
    elif player1Suit==setSuit:
        team1Card=player1Card
    elif player3Suit==setSuit:
        team1Card=player3Card
    # if you dont match the suit, it doesnt really matter which card you compare pick one at random
    else:
        cardArr=[player1Card,player3Card]
        team1Card=cardArr[randrange(2)] #(RND)
          
    # player 2 and 4 are teammates
    
    # check if they have the same suit and if they do then compare to see who has the higher rank
    if player2Suit==player4Suit:
        # comparing the rank
        if rankIndex.index(player2Rank)>rankIndex.index(player4Rank):
            team2Card=player2Card
        else:
            team2Card=player4Card
    # if they dont have the same rank then go based on if they match the suit
    elif player2Suit==setSuit:
        team2Card=player2Card
    elif player4Suit==setSuit:
        team2Card=player4Card
    # if you dont match the suit, it doesnt really matter which card you compare pick one at random
    else:
        cardArr=[player2Card,player4Card]
        team2Card=cardArr[randrange(2)] #(RND)
    
    # check the two cards gotten from each team to see who has higher
    team1Rank,team1Suit=getSuitAndNum(team1Card)
    team2Rank,team2Suit=getSuitAndNum(team2Card)
    
    # now comapring the best card from both teams
    
    # check if they have the same suit first and if they do check the rank, the higher rank gets the point
    if team1Suit==team2Suit:
        if rankIndex.index(team1Rank)>rankIndex.index(team2Rank):
            team1Points+=1
        else:
            team2Points+=1
    # if nither of them match the suit then whoever has the suit of the suit that was set gets the points
    elif team1Suit==setSuit:
        team1Points+=1
    elif team2Suit==setSuit:
        team2Points+=1
      
    return team1Points,team2Points
# end of logic

# this is to make game() shorter
def checkLogic(team1points,team2points,player1Card,player2Card,player3Card,player4Card,setSuit,t1,t2): #(FNC)
    # logic is checked
    point1,point2=logic(player1Card,player2Card,player3Card,player4Card,setSuit)
    # point is awarded
    team1points+=point1
    team2points+=point2
    t1.setText(team1points)
    t2.setText(team2points)
    
    return team1points,team2points
########################################################################################    


########################################################################################
# this function is for the player to click on a card and then to get the text from that card
def playerInput(player1CardArr,win): #(FNC)
    x=True
    while x:
        clickedPoint=win.getMouse()
    # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
        for i in range(len(player1CardArr)):
            if player1CardArr[i].clicked(clickedPoint):
                text=player1CardArr[i].getText()
                x=False
                
    return text
# end of playerInput  
########################################################################################


########################################################################################
# these functions shortens the game() function its just for updating the display
def player1(player1ButtonArr,player1Hand,player1Card,pos,playedButtonArr,win): #(FNC)
    # update display again because card was removed
    removeTextAfter(player1ButtonArr)
    setDisplay(player1Hand,player1ButtonArr,win)
    # put the card on the table
    displayedPlayedCard(player1Card,playedButtonArr,win,pos,'white')
    
def player2(player2ButtonArr,player2Hand,player2Card,pos,playedButtonArr,win,show): #(FNC)
    # update display for player 2
    if show:
        removeTextAfter(player2ButtonArr)
    otherCardDisplay(player2Hand,player2ButtonArr,win,'tan',show)
    # put the card on the table
    displayedPlayedCard(player2Card,playedButtonArr,win,pos,'tan',)
    
def player3(player3ButtonArr,player3Hand,player3Card,pos,playedButtonArr,win,show): #(FNC)
    # update display for player 3
    if show:
        removeTextAfter(player3ButtonArr)
    otherCardDisplay(player3Hand,player3ButtonArr,win,'white',show)
    # put the card on the table
    displayedPlayedCard(player3Card,playedButtonArr,win,pos,'white')
    
def player4(player4ButtonArr,player4Hand,player4Card,pos,playedButtonArr,win,show): #(FNC)
    # update display for player 4
    if show:
        removeTextAfter(player4ButtonArr)
    otherCardDisplay(player4Hand,player4ButtonArr,win,'tan',show)
    # put the card on the table
    displayedPlayedCard(player4Card,playedButtonArr,win,pos,'tan')

# the other players randomly chooses a card ... when they are going first
def getPlayer2Card(player2Hand): #(FNC)
    r = randrange(len(player2Hand)) #(RND)

    return player2Hand.pop(r)

def getPlayer3Card(player3Hand): #(FNC)
    r = randrange(len(player3Hand)) #(RND)
    
    return player3Hand.pop(r)

def getPlayer4Card(player4Hand): #(FNC)
    r = randrange(len(player4Hand)) #(RND)
    
    return player4Hand.pop(r)

# if they are not going first, they will choose based on the played suit
# the other players choose cards based on what suit was played first ... if nothing playLowest card
def getPlayerCard(playerHand,setSuit): #(FNC)
    rankArr=[]
    suitArr=[]
    # to see which card will be played we need to compare both the rank and suits of each cadd to compare it
    for card in playerHand:
        rank,suit=getSuitAndNum(card)
        rankArr.append(rank)
        suitArr.append(suit)
        
    suitIndex=[]
    # checking if the suit set by the player went first is in the players hand
    if setSuit in suitArr:
        for i in range(len(suitArr)):
            if suitArr[i]==setSuit:
                # if it is then we want to get the index of that suit
                suitIndex.append(suitArr.index(setSuit))
                # we want to replace that index with something else so it does not get chosen again
                suitArr[i]='TAKEN'
        
        cardArr=[]
        for i in suitIndex:
            # now we want to get the cards that have that suit, since the ranks, the suits and the playerHand are in the same order,
            # we can use the index to get an array of cards to choose from
            cardArr.append(playerHand[i])
        # out of the cards that match the suit, we want the players to play the higest one to have the best possible chance of getting a point    
        highest=getHighestCard(cardArr)
        
        r=playerHand.index(highest+setSuit)
        # we want to get taht card and remove it from the hand because the card is being played
        return playerHand.pop(r)
    else:
        # if the suit is not there, then we want the player to play the lowest card so we don't waste good cards
        lowest=getLowestCard(playerHand)
        
        return playerHand.pop(lowest)
            
def getLowestCard(playerHand): #(FNC)
    rankArr=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    rankIndex=[]
    for card in playerHand:
        rank,suit=getSuitAndNum(card)
        # we only want the rank to see which is the lowest
        rankIndex.append(rank)
    lowest=rankIndex[0]
    for i in range(len(rankIndex)):
        # comparing the ixdex of the rank to see which is the lowest rank
        if rankArr.index(rankIndex[i])<rankArr.index(lowest):
            lowest=rankIndex[i]
    r=rankIndex.index(lowest)
    
    return r
          
def getHighestCard(cardArr): #(FNC)
    rankArr=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    rankIndex=[]
    for card in cardArr:
        rank,suit=getSuitAndNum(card)
        # we only want the rank to see which is the higest
        rankIndex.append(rank)
    highest=rankIndex[0]
    for i in range(len(rankIndex)):
        # comparing the ixdex of the rank to see which is the highest rank
        if rankArr.index(rankIndex[i])>rankArr.index(highest):
            highest=rankIndex[i]
    return highest
    
    
########################################################################################

########################################################################################
# this stores the button objects of the buttons on the main menu and during game
def menuOptions(): #(FNC)
    menuButtonArr=[]
    # In Game buttons
    # Next Round -0
    menuButtonArr.append(Button(Rectangle(Point(35,20),Point(55,27)))) #(CLOD)
    # Save Game -1
    menuButtonArr.append(Button(Rectangle(Point(105,20),Point(125,27)))) #(CLOD)
    # Home Page Buttons
    # Start Game-2, Saved Game-3, Quit Game-4
    for i in range(1,10,3):
        menuButtonArr.append(Button(Rectangle(Point(i,3),Point(i+2,4)))) #(CLOD)
        
    
    return menuButtonArr
# this displays the button Play Next or save game 
# def displayInGame(menuButtonArr,counter,win): #(FNC) & #(LOOD)
#     menuButtonArr[0].draw(win) 
#     menuButtonArr[0].setFill('orange')
#     menuButtonArr[0].setText('Next Play',win)
#     
#     # keeps asking until a button is pressed
#     while True:
#         clickedPoint=win.getMouse() #(IMS)
#     # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
#         if menuButtonArr[0].clicked(clickedPoint):
#             counter+=1
#             return counter
    
########################################################################################

def setUpBoard(): #(FNC)
    # get each player hand
    player1Hand,player2Hand,player3Hand,player4Hand=getPlayerHand()
    # get the list of Objects which sets up display later
    player1ButtonArr=getDisplayObj()
    player2ButtonArr=otherCardObj(2)
    player3ButtonArr=otherCardObj(3)
    player4ButtonArr=otherCardObj(4)
    # this is for the cards played already
    playedButtonArr=playedCardObj()
    # this is for every time a round is played
    menuButtonArr=menuOptions()
    return player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,menuButtonArr

def firstRound(player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win): #(FNC)
    # player 1 goes
    player1Card=playerInput(player1ButtonArr,win)
    rank,setSuit=getSuitAndNum(player1Card)
    player1Hand.remove(player1Card)
    # updating the display
    player1(player1ButtonArr,player1Hand,player1Card,1,playedButtonArr,win)

    # player 2 goes
    player2Card=getPlayerCard(player2Hand,setSuit)
    # update display
    player2(player2ButtonArr,player2Hand,player2Card,2,playedButtonArr,win,show)
    
    # player 3 goes
    player3Card=getPlayerCard(player3Hand,setSuit)
    # update display
    player3(player3ButtonArr,player3Hand,player3Card,3,playedButtonArr,win,show)
    
    # player 4 goes
    player4Card=getPlayerCard(player4Hand,setSuit)
    # update display
    player4(player4ButtonArr,player4Hand,player4Card,4,playedButtonArr,win,show)
    
    return player1Card,player2Card,player3Card,player4Card,setSuit

def secondRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win): #(FNC)
    # remove old display table
    removeOldDisplay(menuButtonArr,playedButtonArr)
    # player 2 goes
    player2Card=getPlayer2Card(player2Hand)
    rank,setSuit=getSuitAndNum(player2Card)
    # update display
    player2(player2ButtonArr,player2Hand,player2Card,1,playedButtonArr,win,show)
    
    # player 3 goes
    player3Card=getPlayerCard(player3Hand,setSuit)
    # update display
    player3(player3ButtonArr,player3Hand,player3Card,2,playedButtonArr,win,show)
    
    # player 4 goes
    player4Card=getPlayerCard(player4Hand,setSuit)
    # update display
    player4(player4ButtonArr,player4Hand,player4Card,3,playedButtonArr,win,show)
    
    # player 1 goes
    player1Card=playerInput(player1ButtonArr,win)
    player1Hand.remove(player1Card)
    # update display
    player1(player1ButtonArr,player1Hand,player1Card,4,playedButtonArr,win)

    return player1Card,player2Card,player3Card,player4Card,setSuit 

def thirdRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win): #(FNC)
    # remove old display table
    removeOldDisplay(menuButtonArr,playedButtonArr)
    
    player3Card=getPlayer3Card(player3Hand)
    rank,setSuit=getSuitAndNum(player3Card)
    # update display
    player3(player3ButtonArr,player3Hand,player3Card,1,playedButtonArr,win,show)
    
    # player 4 goes
    player4Card=getPlayerCard(player4Hand,setSuit)
    # update display
    player4(player4ButtonArr,player4Hand,player4Card,2,playedButtonArr,win,show)
    
    # player 1 goes
    player1Card=playerInput(player1ButtonArr,win)
    player1Hand.remove(player1Card)
    # update display
    player1(player1ButtonArr,player1Hand,player1Card,3,playedButtonArr,win)
    
    # player 2 goes
    player2Card=getPlayerCard(player2Hand,setSuit)
    # update display
    player2(player2ButtonArr,player2Hand,player2Card,4,playedButtonArr,win,show)

    return player1Card,player2Card,player3Card,player4Card,setSuit

def fourthRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win): #(FNC)
    # remove old display table
    removeOldDisplay(menuButtonArr,playedButtonArr)
        
    player4Card=getPlayer4Card(player4Hand)
    rank,setSuit=getSuitAndNum(player4Card)
    # update display
    player4(player4ButtonArr,player4Hand,player4Card,1,playedButtonArr,win,show)
    
    # player 1 goes
    player1Card=playerInput(player1ButtonArr,win)
    player1Hand.remove(player1Card)
    # update display
    player1(player1ButtonArr,player1Hand,player1Card,2,playedButtonArr,win)
    
    # player 2 goes
    player2Card=getPlayerCard(player2Hand,setSuit)
    # update display
    player2(player2ButtonArr,player2Hand,player2Card,3,playedButtonArr,win,show)
    
    # player 3 goes
    player3Card=getPlayerCard(player3Hand,setSuit)
    # update display
    player3(player3ButtonArr,player3Hand,player3Card,4,playedButtonArr,win,show)

    return player1Card,player2Card,player3Card,player4Card,setSuit
########################################################################################
def checkPlayedCard(menuButtonArr,win,player1Card,player2Card,player3Card,player4Card,setSuit):
    menuButtonArr[0].draw(win) 
    menuButtonArr[0].setFill('orange')
    menuButtonArr[0].setText('Next Play',win)
    
    rank,suit=getSuitAndNum(player1Card)
    highestCard=getHighestCard([player1Card,player2Card,player3Card,player4Card])+setSuit
    if highestCard==rank+suit:
        while True:
            clickedPoint=win.getMouse() #(IMS)
            # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[0].clicked(clickedPoint):
                return 1
    rank,suit=getSuitAndNum(player2Card)
    if highestCard==rank+suit:
        while True:
            clickedPoint=win.getMouse() #(IMS)
            # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[0].clicked(clickedPoint):
                return 2
    rank,suit=getSuitAndNum(player3Card)
    if highestCard==rank+suit:
        while True:
            clickedPoint=win.getMouse() #(IMS)
            # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[0].clicked(clickedPoint):
                return 3
    rank,suit=getSuitAndNum(player4Card)
    if highestCard==rank+suit:
        while True:
            clickedPoint=win.getMouse() #(IMS)
            # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[0].clicked(clickedPoint):
                return 4
    
# this function is the game
def game(team1Name,team2Name,show): #(FNC)
    win=GraphWin("Whist",1430,770) #(GW)
    # 1430/770 * 100
    win.setCoords(0,0,186,100)
    win.setBackground("#966F33")
    # get player hand and set up display objects
    player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,menuButtonArr=setUpBoard()
    
    # couters and point system to keep track
    team1points=0
    team2points=0
    disPlaycounter=0
    setTeamNameDisplay(team1Name,team2Name,win)
    t1,t2=setPointDisplay(win)
    # when set to true, Opponents card is shown
    restart=True
    counter=1
    while restart:
        restart=False
        while True:
            if disPlaycounter>0:
                # remove old display table
                removeOldDisplay(menuButtonArr,playedButtonArr)

            if counter==1: # player 1 goes first
                # original display
                if disPlaycounter==0:
                    setDisplay(player1Hand,player1ButtonArr,win)
                    otherCardDisplay(player2Hand,player2ButtonArr,win,'tan',show)
                    otherCardDisplay(player3Hand,player3ButtonArr,win,'white',show)
                    otherCardDisplay(player4Hand,player4ButtonArr,win,'tan',show)
                
                player1Card,player2Card,player3Card,player4Card,setSuit=firstRound(player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win)
                
                team1points,team2points=checkLogic(team1points,team2points,player1Card,player2Card,player3Card,player4Card,setSuit,t1,t2)
                # check if score has reached its limit
                if checkScore(team1points,team2points,menuButtonArr,win,team1Name):
                    break
                
                counter=checkPlayedCard(menuButtonArr,win,player1Card,player2Card,player3Card,player4Card,setSuit)
                restart=True
                disPlaycounter=1
                break
            
            if counter==2: # player 2 goes first
                # players go
                player1Card,player2Card,player3Card,player4Card,setSuit=secondRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win)
                # check logic
                team1points,team2points=checkLogic(team1points,team2points,player1Card,player2Card,player3Card,player4Card,setSuit,t1,t2)
                # check if score has reached its limit
                if checkScore(team1points,team2points,menuButtonArr,win,team1Name):
                    break
                counter=checkPlayedCard(menuButtonArr,win,player1Card,player2Card,player3Card,player4Card,setSuit)
                restart=True
                break
            if counter==3: # player 3 goes first
                # players go
                player1Card,player2Card,player3Card,player4Card,setSuit=thirdRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win)
                team1points,team2points=checkLogic(team1points,team2points,player1Card,player2Card,player3Card,player4Card,setSuit,t1,t2)
                # check if score has reached its limit
                if checkScore(team1points,team2points,menuButtonArr,win,team1Name):
                    break
                counter=checkPlayedCard(menuButtonArr,win,player1Card,player2Card,player3Card,player4Card,setSuit)
                restart=True
                break
            if counter==4: # player 4 goes first            
                # players go
                player1Card,player2Card,player3Card,player4Card,setSuit=fourthRound(menuButtonArr,player1Hand,player2Hand,player3Hand,player4Hand,player1ButtonArr,player2ButtonArr,player3ButtonArr,player4ButtonArr,playedButtonArr,show,win)
                team1points,team2points=checkLogic(team1points,team2points,player1Card,player2Card,player3Card,player4Card,setSuit,t1,t2)
                # check if score has reached its limit
                if checkScore(team1points,team2points,menuButtonArr,win,team1Name):
                    break
                
                counter=checkPlayedCard(menuButtonArr,win,player1Card,player2Card,player3Card,player4Card,setSuit)
                restart=True
                break
            disPlaycounter=1
            # loop starts from the begning

########################################################################################
def mainMenu(): #(FNC)
    win=GraphWin("Trump",600,600) #(GW)
    win.setCoords(0,0,10,10)
    
    title=Text(Point(5,9),'WHIST')
    title.setSize(36)
    title.draw(win)
    
    t1=Text(Point(2,7),'Team 1 Name:')
    t1.setSize(18)
    t1.draw(win)
    team1Name=Entry(Point(3.7,7),9) #(IEB) 
    team1Name.draw(win)
    
    menuButtonArr=menuOptions()
    #Start Game-2, Saved Game-3, Quit Game-4
    for i in range(2,5):
        menuButtonArr[i].draw(win)
        
    devMode=Button(Rectangle(Point(1,1),Point(3,2)))
    devMode.setText('Dev Mode',win)
    devMode.draw(win)
    menuButtonArr[2].setText('Start Game',win)
    menuButtonArr[2].setFill("green")
    menuButtonArr[3].setText('Past Scores',win)
    menuButtonArr[3].setFill("black")
    menuButtonArr[3].setColor("white")
    menuButtonArr[4].setText('Quit Game',win)
    menuButtonArr[4].setFill("red")
    menuButtonArr[4].setColor("black")
    
    restart=True
    # keeps asking until a a team name is given
    while restart:
        restart=False
        # keeps asking until a button is pressed
        while True:
            clickedPoint=win.getMouse() #(IMS)
        # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[2].clicked(clickedPoint):
                # if a team name is not written in a text box, the loop needs to run again so there can be a team name to defend against bad input
                if team1Name.getText()=="":
                    warning=Text(Point(5,5),"Please Type A Team Name")
                    warning.draw(win)
                    warning.setTextColor("red")
                    restart=True
                    break
                else:
                    win.close()               
                    game(team1Name.getText(),"Computer",False) #(IEB)
                    break
            elif menuButtonArr[3].clicked(clickedPoint):
                win.close()
                displayScores()
                break
            elif menuButtonArr[4].clicked(clickedPoint):
                win.close()
                break
            elif devMode.clicked(clickedPoint):
                game("DEV MODE","Computer",True)

########################################################################################
        
########################################################################################
def checkScore(team1points,team2points,menuButtonArr,win,team1Name): #(FNC)
        
    if not(team1points<7 and team2points<7):
        menuButtonArr[0].undrawText()
        #menuButtonArr[1].undrawText()
        menuButtonArr[0].draw(win)
        menuButtonArr[1].draw(win)
        menuButtonArr[0].setText('Main Menu',win)
        menuButtonArr[1].setFill('orange')
        menuButtonArr[1].setText('Quit Game',win)
        # keeps asking until a button is pressed
        while True:
            clickedPoint=win.getMouse() #(IMS)
    # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
            if menuButtonArr[0].clicked(clickedPoint):
                # after the game is finished, when clicking main menu or quit the score gets saved in a file
                inputScore(team1Name,team1points,team2points)
                win.close()
                mainMenu()
                return True
            elif menuButtonArr[1].clicked(clickedPoint):
                # after the game is finished, when clicking main menu or quit the score gets saved in a file
                inputScore(team1Name,team1points,team2points)
                win.close()
                return True
########################################################################################
            
########################################################################################                        
def setTeamNameDisplay(team1Name,team2Name,win): #(FNC)
    t1=Text(Point(35,75),team1Name+' Points:')
    t2=Text(Point(125,75),team2Name+' Points:')
    t1.setSize(18)
    t2.setSize(18)
    t1.draw(win)
    t2.draw(win)
    
# shows the points on win   
def setPointDisplay(win): #(FNC)
    t1=Text(Point(52,75),'')
    t2=Text(Point(142,75),'')
    t1.setTextColor('white')
    t2.setTextColor('tan')
    t1.setSize(18)
    t2.setSize(18)
    t1.draw(win)
    t2.draw(win)
    
    return t1,t2
########################################################################################

def inputScore(team1Name,team1points,team2points): #(FNC)
    gameFile=open("highScores","a") #(OFL)
    
    for i in [team1Name,team1points,team2points]:
        print(i,end=" ",file=gameFile)
        
    print(file=gameFile)
        
    gameFile.close()

def displayScores(): #(FNC)
    win=GraphWin("Trump",600,600) #(GW)
    win.setCoords(0,0,10,10)
    
    # open the file with the scores
    gameFile=open("highScores","r") #(IFL) 
    
    # keep a list of the scores so they can be displayed
    scoreList=[]
    for line in gameFile:
        # line contains name then player score then computer score
        contentList=line.split(" ")
        
        name=contentList[0]
        playerScore=contentList[1]
        computerScore=contentList[2]
        
        scoreList.append(name+" "+"-"+" "+playerScore+" "+"V.S"+" "+"Computer"+" "+"-"+" "+computerScore)
    
    # starting y value of the text displayed on win
    y=9.5
    for i in range(len(scoreList)):
        Text(Point(5,y),scoreList[i]).draw(win)
        # lower each text by .5
        y-=.5
       
    # to go back to main menu    
    button=Button(Rectangle(Point(4,.5),Point(6,1.5))) #(CLOD)
    button.draw(win)
    button.setText("Main Menu",win)
    # keeps asking until a button is pressed
    while True:
        clickedPoint=win.getMouse() #(IMS)
    # using win.getMouse() to get clickedPoint then checking if the clicked point is one of the buttons
        if button.clicked(clickedPoint):
            win.close()
            mainMenu()
            break
        
    
def main(): #(FNC)
    mainMenu()
    

main()


