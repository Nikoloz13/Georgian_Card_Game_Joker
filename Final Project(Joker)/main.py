from create_players import PlayerCreator
from determine_ranks import RankDeterminer
from multi_round_game import MultiRoundGame

def main():
    """
    Main function to run the game.
    """
    print("Welcome to the Georgian card game 'Joker'!\n")

    creator = PlayerCreator()
    players = creator.create_players()

    rank_determiner = RankDeterminer(players)
    rank_determiner.deal_cards()
    ranked_players = rank_determiner.determine_order()

    multi_round_game = MultiRoundGame(ranked_players, rank_determiner.last_player)
    multi_round_game.play_game()  

if __name__ == "__main__":
    main()