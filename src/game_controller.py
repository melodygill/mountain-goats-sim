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

# Experimenter should use this class by calling GameController.init() and 
# then calling GameController.game_loop().  All the other functions are 
# intended for internal use only.

from game_state import Game_State
from mountain import Mountain
from player import Player
import dice_utility
import logging
logger = logging.getLogger(__name__)

MAX_NUM_INVALID_MOVES = 1000 # Protects against potential infinite loop

class GameController:
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
    
        logger.info("***Started game loop***")
        game_over = False
        while (game_over == False):
            self.game_state.current_turn = self.game_state.current_turn + 1
            logger.info(f"Game turn #{self.game_state.current_turn} begins")
            for player in self.players:
                player_move_is_valid = False
                query_counter = 0
                while (player_move_is_valid == False):
                    dice_roll = dice_utility.roll_the_dice()
                    move = self.get_player_move(player, dice_roll)
                    if (self.move_is_valid(move, dice_roll)) == True:
                        player_move_is_valid = True
                        self.implement_move(player, move)
                    else:
                        logger.error(f"Got invalid move from player {player.color}!")
                        query_counter = query_counter + 1
                        
                    if (query_counter > MAX_NUM_INVALID_MOVES):
                        err_message = "Got more than " + str(MAX_NUM_INVALID_MOVES) + "from player " + player.color + ".  Aborting program!"
                        logger.fatal(err_message)  
                        print(err_message)
                        raise Exception(err_message)
            game_over = self.is_game_over()  # This is outside the for loop because every player needs to have an equal number of turns before the game can end
        return self.report_results()  

    def get_player_move(self, player, dice_roll):
        # Find which player's turn it is
        # current_player = self.game_state.current_turn % len(self.players)
        # player_obj = list(self.players.values())[current_player]
        return player.get_moves(self.game_state, dice_roll)

    def move_is_valid(self, move, dice_roll): 
        # A move is a list of integers that say which mountains we want
        # to move up.
        # move_is_valid needs to receive the results of the dice roll and has
        # to make sure that the list of integers submitted can be legally 
        # achieved from the dice roll.  Since this is a difficult task, 
        # move_is_valid() outsources it!
        legal_possibilities = dice_utility.possible_moves(dice_roll, self.game_state)
        if move in legal_possibilities:
            return True
        else:
            return False

    # player is the player who is making this move
    # move is a list of ints representing which mountains have goats to be moved
    def implement_move(self, player, move):
        # Move goat on each mountain in move
        for mountain_num in move:
            mountain_obj = self.game_state.mountains[mountain_num]
            mountain_obj.step_up(player)  # pass player object of current player
    
    def is_game_over(self):
        # Game over when (All bonus point tokens are claimed OR 3 mountains
        # have no tokens) AND (All players have had an equal number of turns).
        # We evaluate the token conditions here and use the placement of 
        # this function call in the game loop to ensure all players have had
        # an equal number of turns.
        # Later, we could add code to allow changing the victory condition
        # to something other than 3 mountains without tokens...
        if (len(self.game_state.unclaimed_bonus.tokens) == 0):
            return True
        num_empty_mountains = 0
        for mountain in self.game_state.mountains:
            if len(mountain) == 0:
                num_empty_mountains = num_empty_mountains + 1
        if num_empty_mountains >= 3:
            return True
        
        #If we get here, game is still going.
        return False
    
    def report_results(self):
        # Returns a tuple of (string winner, (list of tuples of type 
        # (string player_color, int player_score)))
        scores = self.game_state.calculate_scores()
        winner = "Not determined"
        current_high_score = 0
        for player in scores:
            if player[1] > current_high_score:
                winner = player[0]
                current_high_score = player[1]
                
        return (winner, scores)
    
    
if __name__ == "__main__":
    #Call to start unit tests go here.  Use the unittest module in the 
    #standard library
    pass