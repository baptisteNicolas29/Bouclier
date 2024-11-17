
# Description:

This repository is a simple integration of the card game "Shield".


**Number of players:** 2+ (funnier with 4+ players)

**Material:** a deck of playing cards (standard 52 card deck is nice)


# Set up the Game:
```
1. Each player is distributed a "Life" card. 
    The value of this card represents their life total for the current round of the game.

2. Then each player is distributed two "Shield" cards. 
    The value of these cards represents the value of a Shield their opponents 
    will have to go through to reach their Life total.
    
3. Leave a space for the "Discard Pile".
    All cards not used anymore will go to the Discard Pile
```


# Rules:
```
1. The goal of the game is to bring opponent's Life total down to zero to remove them from the current round.

2. The game is won by the last player left in the game.

3. The starting player takes a turn to perform one of the possible actions of the game. 
    Then the next player takes a turn to perform one of the possible actions of the game.
    The process continues until only one player is left in the game.
    
4. Any cards not used anymore (Swapped by another or used in an Attack) is discarded (put into the Discard Pile)

5. If the deck of cards (aka: Draw Pile) is empty (the last card of the deck was used). 
    Shuffle the Discard Pile and use it as Draw Pile.
```
# Player Turn:
```
1. Declare an action to perform
2. Designate an opponent
3. Draw a card for the action (most actions require to draw a card)
4. Perform chosen action
5. Put all used cards in the Discard Pile
```

# Actions:
- ### Attack:
```
To Attack: 
  1. Designate an opponent to attack
  2. Draw a card (aka: Attack card)
  3. Add any "Charged Attack" cards' value to the Attack card's value
  4. Subtract the value of the Attack from the opponent's Shield value
  5. If the Shield value is more than the Attack value,
    the new Shield value equals the rest of the Shield after the subtraction (new Shield = Shield - Attack)
  6. If the Shield value is less than the Attack value, 
    subtract the rest of the Attack value from the opponent's Life total (aka: Damage)
  7. If a Player takes Damage (at least 1 Damage hit their Life total) they draw two new Shield cards  
```
- ### Charge an Attack:
```
To Charge an Attack: 
  1. Draw a card without looking at it (aka: Charged Attack)
  2. Put it face down next to the Life total card
  3. Any charged cards are used when an Attack is declared
```
> If a player takes Damage to their life total (at least 1 Damage passed through the Player's Shield), 
> all that player's Charged Attacks are lost (put them into the Discard Pile)
- ### Swap Player Shield:
```
To Swap Player's Shield: 
  1. Designate one of the Shield cards of a player (current player or opponent)
  2. Draw a card
  3. Replace the chosen Shield card with the drawn card
```
- ### Custom Action / Custom Rules:
```
Custom Actions and Custom Rules are special actions/rules added by a player after winning a round of the game.
They are used to diversify the game and make it more interesting.
Custom actions and Custom Rules can be about card colors, card value or any other aspect of the game.

Exemple Custom Rule: 
    1. Shield cards of the color Hearts are worth double Shield value
    2. When attacking the Spades color counts as double value when hitting Shield but 0 value for Life damage

Exemple Custom Action: 
    1. Swap one Shield card between two players
    2. If a player has a Shield card of the color Hearts they can swap it with their Life card 
```

# Miscellaneous Info:
### In a standard 52 card deck:
- Aces' value equals 1
- Numbers' values are equal to their card number (two of clubs equals 2)
- Jacks' value equals 11
- Queens' value equals 12
- Kings' value equals 12