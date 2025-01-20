class CallIt:
    def __init__(self, players):
        """
        Initializes the CallIt class.
        :param players: List of Player objects.
        """
        self.players = players
        self.bids = {player.name: 0 for player in players}

    def start_bidding(self, dealing_cards):
        """
        Start the bidding phase. Each player is shown their cards and asked for their bid.
        """
        print("\nBidding Phase Begins!")
        dealing_cards.display_and_clear_hands(self)
        print("\nBidding Phase Ends!")
        self.display_bids()

    def get_valid_bid(self, player):
        """
        Prompts a player to make a valid bid.
        :param player: The player making the bid.
        :return: The player's valid bid.
        """
        total_bids = sum(self.bids.values())
        is_last_player = player == self.players[-1]

        while True:
            try:
                bid = int(input(f"{player.name}, how many point can you take? (0-9): "))
                if 0 <= bid <= 9:
                    if is_last_player:
                        if total_bids == 9 and bid == 0:
                            print("Invalid bid. You cannot say 0.")
                        elif total_bids < 9 and bid == 9 - total_bids:
                            print(f"You cannot say {bid}, choose another bid.")
                        else:
                            self.bids[player.name] = bid
                            return bid
                    else:
                        self.bids[player.name] = bid
                        return bid
                else:
                    print("Invalid bid. Please enter a number between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_bids(self):
        """
        Display the bids made by all players.
        """
        print("\nPlayer Bids:")
        for player, bid in self.bids.items():
            print(f"{player}: {bid}")