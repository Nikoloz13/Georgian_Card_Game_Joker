import time
import os

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system("cls" if os.name == "nt" else "clear")

class TakeCard:
    def __init__(self, players, hands, special_suit):
        """
        Initializes the TakeCard class.
        :param players: List of Player objects.
        :param hands: Dictionary containing player hands.
        :param special_suit: The chosen special suit (trump card).
        """
        self.players = players
        self.hands = hands
        self.special_suit = special_suit
        self.scores = {player.name: 0 for player in players}

    def card_rank(self, card):
        """
        Returns the rank of a card. Higher ranks have higher values.
        """
        ranks = {
            "joker": 100,  
            "A": 14, "K": 13, "Q": 12, "J": 11,
            "10": 10, "9": 9, "8": 8, "7": 7, "6": 6
        }
        rank = card.split()[0].strip()  
        return ranks.get(rank.upper(), 0)  

    def determine_winner(self, played_cards, first_suit, trump_suit):
        """
        Determines the winner of the round based on the cards played.
        :param played_cards: List of tuples (player, card).
        :param first_suit: The suit of the first card played (leading suit).
        :param trump_suit: The trump suit for the game.
        :return: The player who wins the round.
        """
        leading_suit_cards = [
            (player, card) for player, card in played_cards
            if first_suit and first_suit in card
        ]
        trump_cards = [
            (player, card) for player, card in played_cards
            if trump_suit and trump_suit in card
        ]
        joker_cards = [
            (player, card) for player, card in played_cards
            if "joker" in card.lower()
        ]

        if joker_cards:
            return joker_cards[-1][0]

        if trump_cards:
            return max(trump_cards, key=lambda x: self.card_rank(x[1]))[0]

        if leading_suit_cards:
            return max(leading_suit_cards, key=lambda x: self.card_rank(x[1]))[0]

        return max(played_cards, key=lambda x: self.card_rank(x[1]))[0]

    def play_game(self):
        """
        Main gameplay loop. Continues until all cards are played.
        """
        current_player_index = 0

        while any(self.hands[player.name] for player in self.players):
            clear_screen()
            print(f"\nScores: {self.scores}\n")

            played_cards = []
            first_suit = None

            for i in range(len(self.players)):
                current_player = self.players[current_player_index]
                print(f"\n{current_player.name}, it's your turn.")
                print("Your cards:")
                for idx, card in enumerate(self.hands[current_player.name]):
                    print(f"{idx + 1}. {card}")

                valid_cards = []

                if i == 0:  
                    valid_cards = self.hands[current_player.name]
                else:  
                    if first_suit:  
                        valid_cards = [
                            card for card in self.hands[current_player.name]
                            if first_suit in card
                        ]
                        if not valid_cards and self.special_suit:
                            valid_cards = [
                                card for card in self.hands[current_player.name]
                                if self.special_suit in card
                            ]
                        if not valid_cards:
                            valid_cards = self.hands[current_player.name]

                jokers = [
                    card for card in self.hands[current_player.name]
                    if "joker" in card.lower()
                ]
                valid_cards = jokers + [card for card in valid_cards if card not in jokers]

                while True:
                    try:
                        print("\nValid cards to play:")
                        for idx, card in enumerate(valid_cards):
                            print(f"{idx + 1}. {card}")

                        choice = int(input(f"{current_player.name}, choose a card to play (1-{len(valid_cards)}): ")) - 1
                        if 0 <= choice < len(valid_cards):
                            chosen_card = valid_cards[choice]
                            self.hands[current_player.name].remove(chosen_card)
                            break
                        else:
                            print("Invalid choice. Please choose a valid card.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                if i == 0:  
                    first_suit = chosen_card.split()[1]

                played_cards.append((current_player, chosen_card))
                print(f"{current_player.name} played: {chosen_card}")
                time.sleep(2)

                current_player_index = (current_player_index + 1) % len(self.players)

            round_winner = self.determine_winner(played_cards, first_suit, self.special_suit)
            print(f"\n{round_winner.name} wins the round!")
            self.scores[round_winner.name] += 1

            current_player_index = self.players.index(round_winner)
            input("\nPress Enter to continue...")