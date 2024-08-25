# -*- coding: utf-8 -*-

"""
Class to represent the current state of a mountain
"""
import logging
logger = logging.getLogger(__name__)

class Mountain:
    def __init__(self, token_value, num_tokens, height, players):
        self.token_value = token_value  # Value of token for this mountain;
                                        # must be unique amongst all mountains
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
    Move @param player's goat up by one step, or keep goat at the top.
    Return true if the goat is at the top of the mountain after the step, or
    false if it is not at the top.
    Decrements num_tokens and adds self.token_value to the player's list of
    tokens.
    Kicks other goats off the top if this player is at the top.
    """
    def step_up(self, player):
        # Input checking
        if player.color not in self.goat_locations:
            err_message = "Attempted to move player " + player.color + ", which does not exist in " + self.goat_locations + ".  Aborting program!"
            logger.fatal(err_message)  
            print(err_message)
            raise Exception(err_message)

        current_loc = self.goat_locations[player.color]
        # Go up one step if goat isn't at the top
        if current_loc < self.height:
            self.goat_locations[player.color] += 1

        # Goat is at the top of the mountain
        if current_loc == self.height:
            # Update token counts
            self.num_tokens -= 1
            player.add_token(self.token_value)

            # Kick off other goats
            for goat_loc in self.goat_locations:
                if self.goat_locations[goat_loc] == self.height:
                    self.goat_locations[goat_loc] = 0
            return True
        # Goat isn't at the top
        else:
            return False

    # Assuming that num_tokens will be decremented through the game
    def get_num_tokens(self):
        return self.num_tokens