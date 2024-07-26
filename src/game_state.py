# -*- coding: utf-8 -*-

"""
Class that represents the current state of the game.  Contains,
List of Mountains (which, in turn, has location of goats and number of tokens
    remaining)
List of Players (which, in turn, has the number of tokens the player owns)
Current turn (int)

Is responsible for generating a dice roll when necessary.
"""
from mountain import Mountain
from random import Random
import logging
logger = logging.getLogger(__name__)

NUM_DICE = 4  # can move this elsewhere

class GameState:
    """
    Initialize the game_state object
    num_players - integer
    mountain_info - list of (int, int, int) that represents number associated with mountain,
      number of steps on the mountain, initial number of tokens -> so (score, steps, num_tokens)
    ^ for now, we could consider hardcoding mountain info and making it configurable
    later
    """
    def __init__(self, players, mountains, bonus_tokens):
        self.players = players # A list of Player objects
        self.mountains = mountains # A list of Mountain objects
        self.unclaimed_bonus_tokens = bonus_tokens
        self.current_turn = 0 # Game hasn't started yet; call increment_turn
                              # at the beginning of the game.      

        # For each mountain, store value of the chips, number of remaining chips,
        # where goats are on mountain, number of steps
        # Dict of mountains where keys are integers that uniquely identify mountains
        # (I chose the value of their token), and values are the mountain objects
        mountains = {}
        for (score, steps, num_tokens) in mountain_info:
            mountains[score] = Mountain(score, steps, num_tokens, num_players)

    """
    Update the current turn to the next player.
    Roll the dice for the next turn.
    TODO: should rolling the dice be a separate function?
    """
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % self.num_players
        self.dice_roll = [Random.randint(1,6) for _ in range(NUM_DICE)]