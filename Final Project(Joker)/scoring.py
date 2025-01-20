from tabulate import tabulate

class Scoring:
    def __init__(self, players, bids, tricks_won):
        """
        Initialize the Scoring class.
        :param players: List of Player objects.
        :param bids: Dictionary of player names and their bids.
        :param tricks_won: Dictionary of player names and tricks they actually won.
        """
        self.players = players
        self.bids = bids
        self.tricks_won = tricks_won
        self.scores = {player.name: 0 for player in players}

    def calculate_scores(self):
        """
        Calculate the scores for each player based on their bids and tricks won.
        """
        for player in self.players:
            name = player.name
            bid = self.bids.get(name, 0)
            tricks = self.tricks_won.get(name, 0)

            if bid == tricks:
                self.scores[name] += bid * 50 + 50
            elif bid > 0 and tricks == 0:
                self.scores[name] -= 500
            else:
                self.scores[name] += tricks * 10

    def display_scores(self):
        """
        Display the final scores of all players in a table format.
        """
        headers = ["Player", "Bid", "Tricks Won", "Score"]
        table = [
            [player.name, self.bids[player.name], self.tricks_won[player.name], self.scores[player.name]]
            for player in self.players
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"))
