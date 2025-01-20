
import os
import time

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
    elif len(parts) == 1 and parts[0].lower() == "joker":  
        return (
            f"┌───────┐\n"
            f"│       │\n"
            f"│   🃏  │\n"
            f"│       │\n"
            f"└───────┘"
    )

    else:
        raise ValueError(f"Invalid card format: {card}")

class DealingCards:
    suit_map = {
        "Hearts": "♥",
        "Spades": "♠",
        "Diamonds": "♦",
        "Clubs": "♣",
    }

    def __init__(self, players, deck):
        """
        Initializes the DealingCards class.
        :param players: List of Player objects.
        :param deck: A Deck object.
        """
        self.players = players
        self.deck = deck
        self.hands = {player.name: [] for player in players}
        self.trump = None

    def deal_cards(self):
        """
        The dealer deals cards to all players, including themselves, until all cards are dealt.
        """
        round_counter = 0

        while len(self.hands[self.players[0].name]) < 9:
            for player in self.players:
                card = self.deck.cards.pop(0)
                self.hands[player.name].append(card)

            round_counter += 1
            if round_counter == 3 and self.trump is None:
                
                self.trump = self.ask_for_trump(self.players[0])

        print("\nAll cards have been dealt.")

    def ask_for_trump(self, player):
        """
        Allow the trump chooser to pick any trump suit or no trump.
        """
        first_three_cards = self.hands[player.name][:3]
        print(f"\n{player.name}, here are your first three cards:")
        card_art = [format_card(card) for card in first_three_cards]
        for line in zip(*(art.split("\n") for art in card_art)):
            print("   ".join(line))

        while True:
            print("\nYou may choose any trump suit (Hearts, Spades, Diamonds, Clubs) or 'None':")
            try:
                trump = input("Enter your choice: ").strip().capitalize()
                if trump in self.suit_map:
                    print(f"Trump suit declared: {trump} ({self.suit_map[trump]}).")
                    return self.suit_map[trump]
                elif trump == "None":
                    print("No trump suit declared.")
                    return None
                else:
                    print("Invalid input. Please choose a valid suit or 'None'.")
            except ValueError:
                print("Invalid input. Please try again.")

    def display_and_clear_hands(self, call_it):
        """
        Displays each player's cards one by one, asks for a bid, then clears the screen.
        """
        for i, player in enumerate(self.players):
            print(f"\n{player.name}, your cards:")
            card_art = [format_card(card) for card in self.hands[player.name]]
            for line in zip(*(art.split("\n") for art in card_art)):
                print("   ".join(line))

            call_it.get_valid_bid(player)

            if i == len(self.players) - 1:
                input("\nPress Enter to display all players' points...")
                self.clear_screen()
            else:
                input("\nPress Enter to clear the screen for the next player...")
                self.clear_screen()

    def clear_screen(self):
        """
        Clears the terminal screen for the next player.
        """
        os.system("cls" if os.name == "nt" else "clear")