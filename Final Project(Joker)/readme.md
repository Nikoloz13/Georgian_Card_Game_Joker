# Georgian Card Game: Joker

## Overview

The Georgian card game **Joker** is an exciting, multi-round card game where players compete across 16 rounds (divided into 4 parts) to score the most points and emerge as the ultimate winner. The game involves strategy, bidding, trump suits, and skillful card play to secure victory.

## Features

- **Dynamic Player Creation**: Add up to 4 players with unique names.
- **Card Dealing and Trump Suit Selection**: Cards are shuffled and dealt to players, with one player choosing a trump suit each round.
- **Bidding System**: Players make bids on how many tricks they can win.
- **Round-Based Scoring**: Earn points based on bidding accuracy and tricks won.
- **Final Winner Announcement**: After all rounds, the player with the most points is crowned the winner.

---

## Problem of This Project

One limitation of the current implementation is related to the Joker functionality:

> **"A player cannot land on a joker on their turn when they land on a card first."**

I attempted to write these functionalities for the joker:\
\
1.)If a Joker is led and announced as high, each of the other players must play their highest card of the specified suit (or the other Joker).

If the specified suit is trumps, a player who has no trumps may play any card (not necessarily a high one).

If a non-trump suit is specified, then a player who has no cards of this suit and does not play the other Joker must play a trump if possible (any trump, not necessarily a high one) or holding no trumps and no card of the specified suit may play any card.

2.)If a Joker is led and announced as low, the other players must play cards of the suit specified by the leader if possible (they do not have to play their lowest cards), or if they cannot follow suit they must trump if they can. As always, the holder of the other Joker may play it instead of following suit or trumping.  \
\
but I didn't manage to complete it. Unfortunately, I didn't have time to return to this part during development. I plan to add this joker functionality very soon.

---

## File Descriptions

### **`main.py`**

The central script orchestrating the entire game. It:

- Initializes players.
- Determines the order of play and last player.
- Manages the multi-round gameplay.
- Displays final scores and announces the winner.

### **`create_players.py`**

Handles player creation by:

- Allowing up to 4 players to join the game.
- Validating player names.

### **`create_deck.py`**

Generates a shuffled deck of cards, including:

- Standard cards (Ace through 7 of all suits).
- Two 6s (Diamonds and Hearts).
- Two Jokers.

### **`dealing_cards.py`**

Manages:

- Card dealing for all players.
- Trump suit selection.
- Displaying player hands during gameplay.

### **`call_it.py`**

Implements the bidding system:

- Players make bids based on their cards.
- Bids are validated to ensure fair gameplay.

### **`take_card.py`**

Simulates card-playing rounds:

- Players play cards in turn.
- Determines the winner of each round based on rules (trump suits, jokers, and leading suits).

### **`scoring.py`**

Calculates and displays scores:

- Rewards points for meeting bids.
- Penalizes for failing to meet bids.
- Displays round-wise and cumulative scores in a table format.

### **`determine_ranks.py`**

- Determines player order by dealing cards until the first Ace is drawn.
- Sets the last player and defines the order of play.

### **`multi_round_game.py`**

Manages the overall gameplay:

- Divides the game into 4 parts, each with 4 rounds.
- Tracks and updates scores for each part and overall.
- Displays scores in a table format.
- Bonus - the player who gets as many points as he bets will receive a bonus (the highest score from the first three rounds will be added to the total points at the end of the round).
- Calls the winner announcement function after all rounds.

### **`determine_winner.py`**

- Calculates and displays final scores.
- Announces the player with the most points as the winner.

---

## How to Play

1. **Setup**: Run the `main.py` file to start the game.
2. **Player Creation**: Enter names for all 4 players.
3. **Game Flow**:
   - Cards are shuffled and dealt to players.
   - Players bid on how many tricks they can win.
   - Players take turns playing cards, aiming to meet their bids.
   - After each part (4 rounds), scores are calculated and displayed.
4. **Winning the Game**: The player with the highest total score after all 16 rounds wins.

---

## Technologies Used

- **Python 3.9+**
- **Libraries**:
  - `random` (shuffling deck)
  - `tabulate` (displaying scores in table format)
  - `os` (clearing the terminal screen)

---

Enjoy the game!
