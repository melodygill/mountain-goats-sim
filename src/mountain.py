# -*- coding: utf-8 -*-

"""
Class to represent the current state of a mountain
"""
import logging
logger = logging.getLogger(__name__)

class Mountain:
    def __init__(self, token_value, num_tokens, height, players):
        self.token_value = token_value  # Value of token for this mountain;
                                        # must be unique
        self.num_tokens = num_tokens  # Initial number of tokens
        self.height = height # Number of steps on mountain.  Note that if a 
                             # mountain has height 4, 0 is the very bottom 
                             # of the mountain (where the goats start) and 
                             # 4 is the very top (where the goats eat).
        self.players = players # We keep this for input checking; will log 
                               # error if a Mountain is asked to move a goat
                               # of a color that doesn't exist

        # dict mapping goat color to int to store which goats are on each step
        # bottom of mountain is 0; top of mountain is self.height.  Start by
        # putting all the goats at the bottom.
        goat_locations = {}
        for player in players:
            goat_locations[player.color] = 0

    """
    Move @param player's goat up by one step, or do nothing if goat is already
    at the top of the mountain.
    Return true if the goat is at the top of the mountain after the step, or
    false if it is not at the top.
    """
    # TODO: should this function also kick other goats off if they're at the top?
    # could also decrement num_tokens here, but calling function needs to update
    # player's score
    # ^ in that case, we should only return true if the player will get a token
    # by stepping up
    def step_up(self, player):
        pass

    # Assuming that num_tokens will be decremented through the game
    def get_num_tokens(self):
        return self.num_tokens