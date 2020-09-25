Created by Noah Turbin
The game was created with python 3.7.6.

How to play:
using the terminal, navigate to the folder containing this file
then type "python main.py". press enter to start the game

First, you will be asked to input the number of players. 2-4 people can play

In each round, each person will draw a card from the deck.
The person with the best card in that round will be awarded 2 points.
Cards will be shuffled back into the deck at the end of the round.

There are 56 different card;the standard 52 cards plus 4 penalty cards.


Each card has a suit (Spade, Heart, Diamond, Club)
And a face value (0-13).

Cards with the larger face value are better.
In case of ties between face values, the suit will break the tie.
The hierarchy is Spade > Heart > Diamond > Club.
With spades being the best, and clubs being the worst.

The penalty cards are the cards with a face value of 0.
If a player draws a penalty card, they will receive a 1 point penalty.

Technically, if all players draw a penalty card, a person can still win the round
although everyone will still receive a penalty. In this niche case, the penalty card
with the higest suit will break the tie.

The game ends when there is a winner.
The winner must have:
21 points or more
and also lead by 2 points or more.

Good luck!