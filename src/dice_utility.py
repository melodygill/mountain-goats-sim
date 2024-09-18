# -*- coding: utf-8 -*-

"""
dice_utility.py - a collection of routines to make and analyze dice rolls for 
the Mountain Goats board game.
"""

import random as Random
from itertools import combinations
import logging
logger = logging.getLogger(__name__)

NUM_DICE = 4 # 4 dice in the traditional Mountain Goats game


def generate_combinations(dice):
    result = []
    n = len(dice)
    
    # First, generate all possible subsets of dice
    for r in range(1, n+1):
        for subset in combinations(dice, r):
            result.append(list(subset))
    
    # Then, for each subset, generate all possible sums of any dice
    def generate_sums(dice_subset):
        if len(dice_subset) == 1:
            return [dice_subset]
        
        all_lists = []
        n = len(dice_subset)
        
        # Generate combinations of which dice to sum
        for r in range(2, n+1):
            for combo in combinations(dice_subset, r):
                remaining = [die for die in dice_subset if die not in combo]
                summed = sum(combo)
                new_list = remaining + [summed]
                all_lists.append(new_list)
                all_lists.extend(generate_sums(new_list))  # Recursively sum the remaining dice
        
        return all_lists

    # Now, generate the sum combinations for each subset
    final_result = []
    for subset in result:
        final_result.append(subset)  # Add the original subset
        final_result.extend(generate_sums(subset))  # Add all possible sums

    return final_result


def roll_the_dice():
    return [Random.randint(1,6) for _ in range(NUM_DICE)]

def possible_moves(dice_roll, game_state):
    # Given a list of ints in dice_roll, enumerate all possible legal 
    # Mountain Goats moves.  Return a list of lists where each individual
    # list is a list of ints (a list of ints is a single move).
    
    # Input checking
    if type(dice_roll) != type([1, 2, 3, 4]):
        err_message = "dice_utility.possible_moves() got a bad type for dice_roll.  dice_roll must be a list of ints.  Aborting program!"
        logger.fatal(err_message)  
        print(err_message)
        raise Exception(err_message)
        
    raw_list_of_moves = []
    
    # Generate all moves that are possible via simple addition.  Start with 
    # the case where we add all of the dice together.  Then do the cases where
    # we add all of the dice except one together.  Then all of the cases where
    # we all of the dice except two together... and so on till we get to the
    # case where we don't do any addition but take each individual die as a 
    # single component of an overall move.
    
    # Do magic recursions here to populate raw_list_of_moves
    combinations_with_sums = generate_combinations(dice_roll)

    # Removing duplicates by converting to set of tuples, then back to list
    combinations_with_sums = [list(x) for x in set(tuple(sorted(sublist)) for sublist in combinations_with_sums)]

    
    # If there is more than one 1 in the dice roll, add all moves that
    # are possible with substituting the 1's as per game rules.
    if how_many_ones_in_die_roll(dice_roll) > 1:
        pass # Do magic recursions here to further populate raw_list_of_moves
    
    # From each move, remove the elements that refer to mountains that don't
    # exist.  First make a list of mountains that exist, second compare the
    # elements to that list.
    existing_mountains = []
    for mountain in game_state.mountains:
        existing_mountains.append(mountain.token_value)
        
    moves_involving_real_mountains = []
    for possible_move in raw_list_of_moves:
        filtered_move = []
        for item in possible_move:
            if item in existing_mountains:
                filtered_move.append(item)
        moves_involving_real_mountains.append(filtered_move)        
        
    # Now strip out all of the duplicates by converting the list to a set
    # and then back to a list again
    final_output = []
    final_output = list(set(moves_involving_real_mountains))
    
    # Finally done!
    return final_output

def how_many_ones_in_die_roll(dice_roll):
    # Count the number of 1's in dice_roll
    
    # Input checking
    if type(dice_roll) != type([1, 2, 3, 4]):
        err_message = "dice_utility.how_many_ones_in_die_roll() got a bad type for dice_roll.  dice_roll must be a list of ints.  Aborting program!"
        logger.fatal(err_message)  
        print(err_message)
        raise Exception(err_message)
    
    num_of_ones = 0
    for die in dice_roll:
        if die == 1:
            num_of_ones = num_of_ones + 1
    
    return num_of_ones

