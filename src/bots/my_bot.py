"""
A very simple bot.
"""

class MyBot:
    """
    Takes a GameState object and a list of ints for the dice roll.
    Returns a list of ints which are the mountains of the goats that the bot
    decided to advance.

    This bot doesn't know how to add, so it only advances goats on mountains
    which are rolled by the dice.
    So in the base game, it will only move on mountains 5 and 6.
    """
    def get_moves(self, game_state, dice_roll):
        moves = []
        for die in dice_roll:
            if die in game_state.mountains:
                moves.append(die)
        return moves