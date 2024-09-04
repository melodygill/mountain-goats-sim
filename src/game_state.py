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

class GameState:
    def __init__(self, players, mountains, bonus_tokens):
        self.players = players # A dict of Player objects
        self.mountains = mountains # A dict of Mountain objects
        self.unclaimed_bonus_tokens = bonus_tokens
        self.current_turn = 0 # Game hasn't started yet; call increment_turn
                              # at the beginning of the game. 

    """
    Update the current turn to the next player.
    Roll the dice for the next turn.
    TODO: should rolling the dice be a separate function?
    """
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % self.num_players
        # I moved dice roll to game_controller because I need the results
        # there for is_move_valid()
        
    def calculate_scores(self):
        # Returns a list of tuples of type (string player_color, int 
        # player_score)
        output = []
        for player in self.players:
            score = 0
            for token in player.list_of_tokens:
                score = score + token
            for token in player.list_of_bonus_tokens:
                score = score + token
            output.append((player.color, score))
            
        return output
    
    
# Gill da Great wuz here!