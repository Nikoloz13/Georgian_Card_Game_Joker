from determine_winner import calculate_final_scores  
from create_deck import Deck
from dealing_cards import DealingCards
from call_it import CallIt
from take_card import TakeCard
from scoring import Scoring
from tabulate import tabulate

class MultiRoundGame:
    def __init__(self, players, last_player):
        self.players = players
        self.last_player = last_player
        self.round_scores = []
        self.part_scores = {player.name: 0 for player in players}
        self.total_scores = {player.name: 0 for player in players}
        self.dealer_index = self.players.index(self.last_player)
        self.is_first_round = True

    def play_part(self):
        """
        Play 4 rounds and calculate part scores.
        """
        for round_number in range(1, 5):
            print(f"\nRound {round_number} begins!")

            if self.is_first_round:
                dealer = self.players[self.dealer_index]
                trump_chooser_index = (self.dealer_index + 1) % len(self.players)
                self.is_first_round = False
            else:
                self.dealer_index = (self.dealer_index + 1) % len(self.players)
                dealer = self.players[self.dealer_index]
                trump_chooser_index = (self.dealer_index + 1) % len(self.players)

            trump_chooser = self.players[trump_chooser_index]
            print(f"Dealer: {dealer.name}, Trump Chooser: {trump_chooser.name}")

            deck = Deck()
            dealing_cards = DealingCards(self.players, deck)
            dealing_cards.deal_cards() 

            trump_suit = dealing_cards.trump  

            call_it = CallIt(self.players)
            call_it.start_bidding(dealing_cards)

            
            take_card_game = TakeCard(self.players, dealing_cards.hands, trump_suit)
            take_card_game.play_game()

            
            scoring = Scoring(
                self.players,
                call_it.bids,
                take_card_game.scores
            )
            scoring.calculate_scores()
            self.round_scores.append(scoring.scores)
            scoring.display_scores()

            
            for player in self.players:
                self.part_scores[player.name] += scoring.scores[player.name]

        
        for player in self.players:
            if all(round_scores[player.name] >= call_it.bids[player.name] for round_scores in self.round_scores):
                max_score = max(
                    self.round_scores[0][player.name],
                    self.round_scores[1][player.name],
                    self.round_scores[2][player.name]
                )
                self.part_scores[player.name] += max_score

            self.total_scores[player.name] += self.part_scores[player.name]

        print("\nPart scores:")
        self.display_table(self.part_scores)

    def play_game(self):
        """
        Play all parts of the game (16 rounds).
        """
        for part in range(1, 5):  
            print(f"\nStarting Part {part}!")
            self.play_part()
            input("\nPress Enter to start the next part...")

        
        print("\nFinal scores after all parts:")
        self.display_table(self.total_scores)

        # Determine and display the winner
        calculate_final_scores(self.total_scores)

    def display_table(self, scores):
        """
        Display scores in a table format.
        """
        headers = ["Player", "Score"]
        table = [[player, scores[player]] for player in scores]
        print(tabulate(table, headers=headers, tablefmt="grid"))
    
    
