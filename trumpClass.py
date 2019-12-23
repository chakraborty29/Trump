from random import randrange
from graphics import*
#############################################################
class Card: #(CLOD)
    def __init__(self,deck):
        self.deck=deck
    
    # shuffle the deck of cards
    def shuffle(self):
        for i in range(len(self.deck),0,-1):
            r=randrange(i)
            self.deck[i-1],self.deck[r]=self.deck[r],self.deck[i-1]
    # end of shuffle 
    
    # draw a card from the deck, default is one
    def draw(self,amt=1):
        card=[]
        if amt>len(self.deck):
            print("Sorry you are drawing more cards than you have")
        else:
            for i in range(amt):
                card.append(self.deck.pop())
            if amt>1:
                return card[0:amt+1]
            else:
                return card[0]
    # end of draw
   
    def getDeckInfo(self,item):
        if item.lower()=="length":
            return len(self.deck)
        elif item.lower()=='deck':
            return self.deck
    # end of getDeckInfo
    
    # show either the length or the list of deck
    def display(self,info='deck'):
        if info.lower()=="deck":
            print("Your deck of card is:",self.deck)
        elif info.lower()=="length":
            print("The length of your deck is:",len(self.deck))
    # end of display
    
#############################################################
class Button: #(CLOD)
    def __init__(self,rect):
        self.rect=rect
        self.leftLower=self.rect.getP1()
        self.rightUpper=self.rect.getP2()
        self.centerPoint=self.rect.getCenter()
        
    def clicked(self,clickedPoint): return (self.leftLower.getX()<=clickedPoint.getX() and clickedPoint.getX()<=self.rightUpper.getX() and self.leftLower.getY()<=clickedPoint.getY() and clickedPoint.getY()<=self.rightUpper.getY())
        
    
    # draw the rectangle
    def draw(self,win):
        self.rect.draw(win)
    # undraw the rectangle    
    def undraw(self):
        self.rect.undraw()
        
    # set the colors of the rectangles to a color
    def setFill(self,color):
        self.rect.setFill(color)
        
    # add the name of the cards to the center of the rectangle
    def setText(self,item,win):
        self.textMsg=item
        self.text=Text(self.centerPoint,item)
        self.text.draw(win)
        self.text.setSize(18)
        
    def setColor(self,color):
        self.text.setTextColor(color)
        
    def undrawText(self):
        self.text.undraw()
        
    def getText(self): return self.textMsg
#############################################################        


