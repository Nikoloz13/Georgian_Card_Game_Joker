# Updated determine_ranks.py to remove unnecessary dealer-related messages
from create_deck import Deck

def format_card(card):
    """
    Formats a card string into a card-like visual representation.
    """
    parts = card.split()
    if len(parts) == 2:  
        rank, suit = parts
        return (
            f"┌───────┐\n"
            f"│ {rank:<2}    │\n"
            f"│   {suit}   │\n"
            f"│    {rank:>2} │\n"
            f"└───────┘"
        )
    elif len(parts) == 1: 
        rank = parts[0]
        return (
            f"┌───────┐\n"
            f"│ {rank:<7}│\n"
            f"│       │\n"
            f"│{rank:>7} │\n"
            f"└───────┘"
        )
    else:
        raise ValueError(f"Invalid card format: {card}")

class RankDeterminer:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.last_player = None

    def deal_cards(self):
        """
        Simulate dealing cards to players until the first Ace is drawn.
        """
        print("Dealing cards to determine the last player...")
        while True:
            for player in self.players:
                card = self.deck.cards.pop(0)
                print(f"{player.name} drew:")
                print(format_card(card))
                if "A" in card:  
                    print(f"\n{player.name} drew the first Ace and is the last player.")
                    self.last_player = player
                    return

    def determine_order(self):
        """
        Arrange players based on the last player.
        """
        last_player_index = self.players.index(self.last_player)
        new_order = self.players[last_player_index + 1:] + self.players[:last_player_index + 1]
        return new_order