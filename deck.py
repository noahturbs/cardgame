import random
import player

#deck is a list of cards
class deck(object):
    """docstring for ."""
    def __init__(self):

        self.deck=self.create_deck()
        #let's make the cardlist here.
        #meaning, 52 cards + 4 joker cards


    def create_deck(self):
        decklist=[]
        suitstring=["Spade", "Heart", "Diamond", "Club"]
        suitrank=[4,3,2,1]
        for x in range(0,4):
            for face in range (0,14):  #0,1,2... 13
                decklist.append(card(suitstring[x], suitrank[x], face))
        return decklist

    def shuffle(self):
        #assume that all cards are in the deck.
        self.deck = random.sample(self.deck, len(self.deck))

    def deal(self):
        #returns the 'top' card of the deck. removes it from the deck
        return self.deck.pop(0)

    def putbackcards(self,players):
        #put back cards that were played this round.
        for x in players:
            self.deck.append(x.showhand())



class card(object):
    def __init__(self,suit,suitrank,face):
        self.suit=suit    #string. ex "Spade"
        self.suitrank=suitrank     #int, correlates to suit. higher means stronger

        self.face=face      #int. ex 0~13
