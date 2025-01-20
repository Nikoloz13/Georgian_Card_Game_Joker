def calculate_final_scores(scores):
    """
    Calculate and display the final scores of the players and determine the winner.

    Args:
        scores (dict): A dictionary where keys are player names and values are their total scores.

    Returns:
        str: The name of the winner.
    """
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

    winner = max(scores, key=scores.get)
    print(f"\nThe winner is {winner}\n")
    return winner

if __name__ == "__main__":
    
    example_scores = {
        "Player 1": 120,
        "Player 2": 150,
        "Player 3": 110,
        "Player 4": 135
    }

    calculate_final_scores(example_scores)