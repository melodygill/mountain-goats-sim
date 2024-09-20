"""
Parent class for all bots.
"""

class Bot(object):
    """
    All bots should implement a get_move method.
    """
    def get_move(self, game_state, dice_roll):
        raise NotImplementedError