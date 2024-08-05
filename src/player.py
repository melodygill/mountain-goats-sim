# -*- coding: utf-8 -*-
"""
An object of the Player class represents a single player in the game Mountain 
Goats.  The class is short and just stores data.

color = this player's color as a string, e.g. "Red" or "White"
list_of_tokens = this player's tokens as a list of ints, e.g. if it's 
    [5, 6, 3], the player has a token of value 5, a token of value 6, and 
    a token of value 3.
list_of_bonus_tokens = this player's bonus tokens as a list of ints; e.g.
    if it's [15], the player has one bonus token with a value of 15.
"""
import logging
logger = logging.getLogger(__name__)

class Player:
    def __init__(self, color):
        self.color = color # String.  Must be unique amongst all the players
        self.list_of_tokens = [] # List of ints; might not be sorted
        self.list_of_bonus_tokens = [] # List of ints; might not be sorted

    def __str__(self):
        return f"{self.color} player has tokens: {self.list_of_tokens} and bonus tokens: {self.list_of_bonus_tokens}"
        
# Player objects are almost always found in lists which makes it a bit 
# difficult if you want to do things like add a token to the Red player.
# That will involve searching the list of the Red player object and then 
# adding an in to the list_of_tokens for that specific object.  The helper
# functions below, while not part of the Player class, will help the
# programmer do these sorts of things.

def Give_Token_To_Player(color, token, list_of_players):
    for this_player in list_of_players:
        if (this_player.color == color):
            this_player.list_of_tokens.append(token)
            return
    logger.error("Player.Give_Token_To_Player() could not find the color " + 
        f"{color} in list_of_players")
    

def Give_Bonus_Token_To_Player(color, bonus_token, list_of_players):
    for this_player in list_of_players:
        if (this_player.color == color):
            this_player.list_of_bonus_tokens.append(bonus_token)
            return
    logger.error("Player.Give_Bonus_Token_To_Player() could not find the " + 
            f"color {color} in list_of_players")

def Remove_Token_From_Player(color, token, list_of_players):
    # Write this function if it becomes needed.  Think about how to 
    # signal the calling function if color doesn't happen to have the
    # token that we want to remove.  Probably return True if removal
    # succeeds and False if it does not because there was no such token
    # to remove
    pass

def Remove_Bonus_Token_From_Player(color, bonus_token, list_of_players):
    # See comments for Remove_Token_From_Player(), above
    pass