class Player:
    def __init__(self, name):
        self.name = name

class PlayerCreator:
    def __init__(self):
        self.players = []

    def add_player(self, name):
        """
        Adds a player to the game after validating the name.
        """
        if not name:
            print("Error: Username cannot be empty. Please try again.")
            return False
        if len(self.players) >= 4:
            print("Error: Only 4 players are allowed.")
            return False
        self.players.append(Player(name))
        return True

    def create_players(self):
        """
        Allows the user to add exactly 4 players by providing valid names.
        """
        print("Welcome to the player creation process!")
        print("You can enter any nickname, symbol, or name for each player.")
        print("Note: Usernames cannot be empty. You must add exactly 4 players.")

        while len(self.players) < 4:
            name = input(f"Enter name for Player {len(self.players) + 1}: ").strip()
            if self.add_player(name):
                print(f"Player '{name}' has been added successfully.")
            else:
                print("Invalid input. Please try again.")

        print("All players have been created!")
        print("Players in the game:")
        for idx, player in enumerate(self.players):
            print(f"{idx + 1}. {player.name}")

        return self.players