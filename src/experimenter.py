# -*- coding: utf-8 -*-
"""
experimenter.py - evaluates various Mountain Goat strategies by causing a 
number of Mountain Goat games to be played.  For each game, experimenter 
will create a number of Player and Mountain objects and send them to 
game_controller.py which will play a single game of Mountain Goats and then
return the results.

experimenter is responsible for,
1.  Determining the number of games played.
2.  Deciding the number and order of players by creating a list of Player
    objects that are arranged in the order of play.
3.  Creating the Mountains and putting them in a list (usually the 
    Mountains will be the usual Mountains defined in the published game
    but you can change this if you like).
4.  Creating a list of bonus tokens that will be available in the game.
5.  Keeping track of the victories and deciding which strategy is best.
"""

from mountain import Mountain
from player import Player
from game_controller import Game_Controller

from collections import OrderedDict
import logging
logger = logging.getLogger(__name__)

logging.basicConfig(filename = "log.txt", encoding = "utf-8", 
    level = logging.DEBUG)
# All logging must take place after the line above

# These values define a four-player game according to the game rules as
# published.  Change them if you want less players (the game is published as
# a 2-4 player game) or if you want to explore variants outside of the 
# published game.  Note that the player colornames must be unique and the 
# values of the chips on each mountain must be unique (you can't have two
# mountains having 5 point chips at the top!)

LIST_OF_PLAYER_COLORS = ["Red", "Black", "Yellow", "White"]
LIST_OF_BONUS_TOKENS = [15, 12, 9, 6]
FIVE_MOUNTAIN = Mountain(5, 12, 4, LIST_OF_PLAYER_COLORS)
SIX_MOUNTAIN = Mountain(6, 11, 4, LIST_OF_PLAYER_COLORS)
SEVEN_MOUNTAIN = Mountain(7, 10, 3, LIST_OF_PLAYER_COLORS)
EIGHT_MOUNTAIN = Mountain(8, 9, 3, LIST_OF_PLAYER_COLORS)
NINE_MOUNTAIN = Mountain(9, 8, 2, LIST_OF_PLAYER_COLORS)
TEN_MOUNTAIN = Mountain(10, 7, 2, LIST_OF_PLAYER_COLORS)

# First, make a dict of Player objects.
# The order of LIST_OF_PLAYER_COLORS determines who goes first, who goes second, etc.
players = OrderedDict()
for color in LIST_OF_PLAYER_COLORS:
    players[color] = Player(color)
    
# Now make a list of Mountain objects.
list_of_mountains = [FIVE_MOUNTAIN, SIX_MOUNTAIN, SEVEN_MOUNTAIN, 
    EIGHT_MOUNTAIN, NINE_MOUNTAIN, TEN_MOUNTAIN]
# Organize Mountain objects in a dict
mountains = dict()
for mountain in list_of_mountains:
    mountains[mountain.token_value] = mountain

# Call game_controller
game_controller = Game_Controller(players, mountains, 
    LIST_OF_BONUS_TOKENS)
results = game_controller.game_loop()

# TO-DO
# The part where we run 10,000 games with each player using a different 
# strategy and collate and report the results.
