import random

class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        """
        Creates a shuffled deck with the following configuration:
        - Ace, King, Queen, Jack, 10, 9, 8, 7 of all four suits
        - Two 6s: Diamonds and Hearts
        - Two Jokers
        """
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7']
        
        # Create cards for the given ranks and suits
        deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
        
        # Add two 6s (Diamonds and Hearts)
        deck += ['6 ♦', '6 ♥']
        
        # Add two Jokers
        deck += ['joker', 'joker']
        
        # Shuffle the deck
        random.shuffle(deck)
        return deck