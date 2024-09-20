"""
A bot that chooses a move at random.
"""

from bots.bot import Bot
from dice_utility import possible_moves
from random import choice

class RandomMoveBot(Bot):
    def get_move(self, game_state, dice_roll):
        return choice(possible_moves(dice_roll, game_state))