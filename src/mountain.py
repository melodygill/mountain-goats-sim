"""
Class to represent the current state of a mountain
"""

class Mountain:
    def __init__(self, value, steps, num_tokens, num_players):
        self.value = value  # value of token for this mountain
        self.steps = steps  # number of steps on mountain
        self.num_tokens = num_tokens  # initial amount of tokens

        # dict mapping int to list to store which goats are on each step
        # bottom of mountain is 0; top of mountain is self.steps
        # lists will start empty (zero players) except for bottom (all players)
        # We are representing players by integers starting from 0
        goats = {}
        goats[0] = [i for i in range(num_players)]
        for i in range(1, steps+1):
            goats[i] = []

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