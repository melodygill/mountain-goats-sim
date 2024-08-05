# -*- coding: utf-8 -*-

# game_controller.py - when called, runs a single game of Mountain Goats
# and returns the result to the caller.  We anticipate that the calling 
# function will be an object of the Experimenter class and will set up
# 10,000 (or so) calls to game_controller.py to test which of several 
# Mountain Goat strategies is superior.

# A GameController maintains a GameState which is the current state of 
# the game in progress.  Players are objects and the GameController will
# pass the GameState to each player in turn.  The player will examine 
# the GameState and return its move.  GameController will then make the
# appropriate changes to the GameState and then pass the new GameState
# to the next player.  This continues until the conditions for ending
# the game are reached and then the results (as well as the final 
# GameState) are returned to the caller.

from game_state import Game_State
from mountain import Mountain
from player import Player
import logging
logger = logging.getLogger(__name__)

class Game_Controller:
    """
    Receive a dict of Player objects and a dict of Mountain objects and
    create a Game_State object
    """
    def __init__(self, players, mountains, 
        list_of_bonus_tokens):
        self.game_state = Game_State(players, mountains, 
            list_of_bonus_tokens)
            

    def validate_move(self, move): #name it move_is_valid so return result
                                   #of True is easily understood?
        # A move is a list of integers that say which mountain we want
        # to move up.
        # Validate_move needs to receive the results of the dice roll 
        # and just has to make sure that the list of integers submitted
        # can be legally achieved from the dice roll.
        # Player code likely wants to know whether the move that it's
        # thinking about is valid as well.  Maybe we should pull this
        # function out to a utility class since both player code and 
        # GameController need it.
        pass

    """
    Update game state to reflect that the move was made
    """
    def implement_move(self, move):
        pass

    def requery(self): #In retrospect, is this necessary given the 
        pass           #game loop psuedocode below?
    
    """
    Game routines
    """
    def is_game_over(self):
        pass
    
    def roll_dice(self):
        pass
    
    """
    Main game loop
    """
    def game_loop():
    # Receive properties from caller:
    #   * Names of players and where to find the associated code for each.
    #   * Order of play (if random order is desired, the caller is responsible
    #     for creating and passing a new random order on each call)
    
    # Create GameState with initial state
    
    # game_over = false
    # while (game_over == false)
    #   foreach (player)
    #       player_move_is_valid = false
    #       query_counter = 0
    #       while (player_move_is_valid == false)
    #           GetPlayerMove()
    #           if (validate_move()) == true
    #               player_move_is_valid = true
    #               implement_move()
    #           else
    #               Write error message (player code returned bad result)
    #               query_counter++
    #           if (query_counter > some_magic_number):
    #               Write error message - player code failing too much
    #               print("Potential infinite loop; ending program")
    #               throw Exception 
    #   if (is_game_over() == true):
    #       game_over = true
    #   ReportResults()  
        pass
    
if __name__ == "__main__":
    #Call to start unit tests go here.  Use the unittest module in the 
    #standard library
    pass