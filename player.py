import deck



class player(object):

    def __init__(self,id):
        self.id= id         # 0 or 1 or 2 or 3
        self.hand=None      #this is a card object
        self.score= 0

    def sethand(self, card):
        #function to set player's hand to a card. use with deck.deal()
        self.hand=card

    def showid(self):
        #function to show a player's id. returns an int
        return self.id

    def showscore(self):
        #function to show a player's score. returns an int
        return self.score

    def showhand(self):
        #function to show a player's hand. returns a card
        return self.hand

    def printhand(self):
        #function to print a player's hand. prints hand

        print('Card is '+ str(self.hand.suit) + ' ' + str(self.hand.face) )

    def checkpenalty(self):
        #checks if card drawn is penalty. applies and prints penalty
        if(self.hand.face==0):
            print('A joker card was drawn. Applying penalty (-1p) to player immediately.')
            self.decrementscore()
            print('Player ' +  str(self.showid()) + ' score is ' + str(self.showscore()) )

    def decrementscore(self):
        #decrements score
        self.score = self.score - 1

    def incrementscore(self):
        #increments score
        self.score = self.score + 2


    def calculateround(players):
        #prints the winner of the round.
        #increments the score of the winner.
        #prints winner and their new score

        #players is a list of players.

        tempcard=players[0].hand    #store the card here temporarily
        indexcard=0   #store the winning index here temporarily
        for x in players:
            if(x.hand.face == tempcard.face) and (x.hand.suitrank>tempcard.suitrank):
                tempcard=x.showhand()
                indexcard=x.showid()

            if (x.hand.face > tempcard.face):#
                tempcard=x.showhand()
                indexcard=x.showid()

        players[indexcard].incrementscore()

        print('Player ' +  str(indexcard) + ' has won the round (+2p). Their score is now ' + str(players[indexcard].showscore()) )

    def printallscores(players):
        #prints all scores for all players
        print('End of the round. Current standings are...')
        for x in players:

            playerid=x.showid()
            playerscore=x.showscore()
            print('Player ' +  str(playerid) + ' has ' + str(playerscore) +' points.' )

    def wincondition(players):
        #checks if game is done.
        #prints winner.
        scorelist=[]
        for x in players:
            scorelist.append(x.showscore())

        #now we have a list of the scores.

        #find the highestscore.
        #and its index
        maxscore=0
        indexscore=0
        for y in range(len(scorelist)):
            if (scorelist[y] > maxscore):
                maxscore= scorelist[y]
                indexscore = y

        #delete the highest score.

        scorelist.pop(indexscore)
        #find the highest remaining score.
        secondmaxscore=0
        for z in range(len(scorelist)):
            if (scorelist[z] > secondmaxscore):
                secondmaxscore= scorelist[z]


        #now we have the highest and second highest score.
        #first, check if the highest score is 21 or higher.
        #then, check if the second highest score is more than two points away

        if((maxscore>20) and (maxscore-secondmaxscore>2)):
            #if both conditions are met, we print winner and return false
            print('Player ' + str(indexscore) + ' has won.')
            print('Game is now ending')
            return False





        #game is not finished yet!
        return True
