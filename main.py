import player
import deck







def askplayercount():
    #asks the user how many players will be playing.
    #returns the number of players 2, 3 or 4
    inputString = input('Type in the number of players in this session. Then press enter.\n')
    playercount=1
    if(inputString.isnumeric()):
        playercount= int(inputString)

    while not(playercount == 2 or playercount == 3 or playercount == 4):

        inputString = input('Invalid command. Type 2, 3, or 4. Then press enter.\n')
        if(inputString.isnumeric()):
            playercount= int(inputString)

    return playercount

def playertaketurns(players,thedeck):
    #for loop, where each player takes their turn
    #each player draws their card, and applies any penalty if applicable
    for currentplayer in players:
        #during their turn,
        #pause the game, wait until input
        input('Player ' +  str(currentplayer.showid()) + ' is about to draw. Press enter to draw')
        #then they draw a card
        currentplayer.sethand(thedeck.deal())

        #display the card drawn
        currentplayer.printhand()

        #check for penalty. apply penalty
        currentplayer.checkpenalty()

def main():

    #start game.
    input('Game is about to start. Press enter to continue\n')

    #ask for number of players (2-4)
    playercount = askplayercount()

    #initialize players and deck
    players=[]
    for x in range(playercount):
        players.append(player.player(x))

    thedeck = deck.deck()

    ##print(thedeck.deck[0].suit)

    gameinsession=True


    #start game
    while(gameinsession):
    #every round, each player takes a turn

    #randomize the deck at the start of round
        thedeck.shuffle()

        #each player takes their turn.
        #draws their card, penalty if applicable
        playertaketurns(players,thedeck)


        #end of loop for each player.
        #now do award points. then show score standings.
        #put cards back in deck
        #check if someone won the game

        #award points.
        player.player.calculateround(players)

        #print standings
        player.player.printallscores(players)

        #reset deck
        thedeck.putbackcards(players)

        #has anyone reached the win condition? 21 or greater
        #also, they need to win by 2 or more
        gameinsession = player.player.wincondition(players)


    #end of loop

main()
