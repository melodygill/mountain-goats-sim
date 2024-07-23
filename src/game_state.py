"""
Class that represents the current state of the game.
Mountains, chips on top of mountain
Location of goats
Players' chips
Current turn
Current dice roll
"""

from mountain import Mountain
from random import Random

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
    def __init__(self, num_players, mountain_info):
        self.num_players = num_players

        # For each player, store score, list of current chips
        # TODO: would this be better as a class or struct?
        players = {}
        for i in range(num_players):
            players[i] = (0, [])  # tuple of score and list of current chips

        # Variable for current turn. Call next_turn before the first turn
        current_turn = -1

        # TODO: should dice roll be a list of all dice values
        # or just the sum of the non-ones and a count of the ones?
        # I went with list, seems simpler
        dice_roll = []

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