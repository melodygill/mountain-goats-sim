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

# Experimenter should use this class by calling Game_Controller.init() and 
# then calling Game_Controller.game_loop().  All the other functions are 
# intended for internal use only.

from game_state import Game_State
from mountain import Mountain
from player import Player
import logging
logger = logging.getLogger(__name__)

MAX_NUM_INVALID_MOVES = 1000 # Protects against potential infinite loop

class Game_Controller:
    """
    Receive a dict of Player objects and a dict of Mountain objects and
    create a Game_State object
    """
    def __init__(self, players, mountains, list_of_bonus_tokens):
        self.game_state = Game_State(players, mountains, list_of_bonus_tokens)
        self.players = players
        self.mountains = mountains
        self.list_of_bonus_tokens = list_of_bonus_tokens
        
    """
    Main game loop
    """
    def game_loop(self):
    # Receive properties from caller:
    #   * Names of players and where to find the associated code for each.
    #   * Order of play (if random order is desired, the caller is responsible
    #     for creating and passing a new random order on each call).
    
        game_over = False
        while (game_over == False):
          for player in self.players:
              player_move_is_valid = False
              query_counter = 0
              while (player_move_is_valid == False):
                  move = self.get_player_move()
                  if (self.move_is_valid(move)) == True:
                      player_move_is_valid = True
                      self.implement_move()
                  else:
                      logger.error(f"Got invalid move from player {player.color}!")
                      query_counter = query_counter + 1
                      
                  if (query_counter > MAX_NUM_INVALID_MOVES):
                      err_message = "Got more than " + str(MAX_NUM_INVALID_MOVES) + "from player " + player.color + ".  Aborting program!"
                      logger.fatal(err_message)  
                      print(err_message)
                      raise Exception(err_message)
          if (self.is_game_over() == True):
              game_over = True
        return self.report_results()  

    def get_player_move(self):
        pass        

    def move_is_valid(self, move): 
        # A move is a list of integers that say which mountain we want
        # to move up.
        # move_is_valid needs to receive the results of the dice roll 
        # and just has to make sure that the list of integers submitted
        # can be legally achieved from the dice roll.
        # Player code likely wants to know whether the move that it's
        # thinking about is valid as well.  Maybe we should pull this
        # function out to a utility class since both player code and 
        # GameController need it.
        pass

    def implement_move(self, move):
        pass
    
    def is_game_over(self):
        pass
    
    def report_results(self):
        pass
    
    
if __name__ == "__main__":
    #Call to start unit tests go here.  Use the unittest module in the 
    #standard library
    pass