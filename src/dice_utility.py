# -*- coding: utf-8 -*-

"""
dice_utility.py - a collection of routines to make and analyze dice rolls for 
the Mountain Goats board game.
"""

from random import randint
from itertools import combinations, permutations
from copy import deepcopy
import logging
logger = logging.getLogger(__name__)

NUM_DICE = 4 # 4 dice in the traditional Mountain Goats game


def roll_the_dice():
    return [randint(1,6) for _ in range(NUM_DICE)]

# Generates all combinations of dice rolls that can be formed by summing any of
# the dice together, according to the Mountain Goats rules.
# E.g. if dice = [2,3,4], here are examples of valid combinations:
# [[2], [5], [5, 4], [9]]
# TODO: this doesn't find all valid moves.
# e.g. misses [7, 8] from the roll [2, 3, 5, 5]
def generate_combinations_old(dice):
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

    # Remove duplicates
    final_result = [list(x) for x in set(tuple(sorted(sublist)) for sublist in final_result)]

    return final_result

# Function to generate all combinations of dice rolls by summing
# and/or removing dice from the roll.
# Input is list of ints, return value is list of list of ints
def generate_combinations(dice_roll):
    final_list = [dice_roll]
    # Base case: 1 die in the dice roll; return it
    # TODO: do we want empty list in the list of possibilities?
    if len(dice_roll) <= 1:
        return final_list
    
    # Recursive case
    # Generate all permutations of the dice roll as a list of lists
    perms = [list(p) for p in permutations(dice_roll)]

    # For each permutation
    for p in perms:
        # Create 2 new lists by adding first 2 numbers / removing first number
        sum_list = [p[0] + p[1]] + p[2:]
        remove_list = p[1:]
        # Recurse on the new lists
        final_list.extend(generate_combinations(sum_list))
        final_list.extend(generate_combinations(remove_list))

    # Strip duplicates and return final result
    # TODO do we want to be removing duplicates on every recursive call?
    final_list = [list(x) for x in set(tuple(sorted(sublist)) for sublist in final_list)]
    return final_list

# Given a dice roll, return a list of all the dice rolls that could be made by
# converting extra ones into other values. (No summing, only changing the 1s)
# E.g. [1, 1, 2, 3] has 2 1s, so one of the 1s can be changed to any other value.
# Return value: [[1,1,2,3],[1,2,2,3],[1,3,2,3],[1,4,2,3],[1,5,2,3],[1,6,2,3]]
def expand_ones_in_dice_roll(dice_roll):
    final_list = [dice_roll]
    # Base case: Zero or one 1s in the dice roll
    if how_many_ones_in_die_roll(dice_roll) <= 1:
        return final_list
    
    # Recursive case: Generate lists
    not_one_values = [2, 3, 4, 5, 6]
    new_dice_roll = deepcopy(dice_roll)
    new_dice_roll.remove(1)
    for val in not_one_values:
        final_list.extend(expand_ones_in_dice_roll(new_dice_roll + [val]))
    return final_list

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
        

    # Find add all dice rolls that
    # are possible with substituting the 1's as per game rules.
    expanded_dice_roll = expand_ones_in_dice_roll(dice_roll)

    # Generate all moves that are possible via simple addition.  Start with 
    # the case where we add all of the dice together.  Then do the cases where
    # we add all of the dice except one together.  Then all of the cases where
    # we all of the dice except two together... and so on till we get to the
    # case where we don't do any addition but take each individual die as a 
    # single component of an overall move.
    
    # Do magic recursions here to populate raw_list_of_moves
    raw_list_of_moves = []
    for roll in expanded_dice_roll:
        raw_list_of_moves.extend(generate_combinations(roll))

    # From each move, remove the elements that refer to mountains that don't
    # exist.  First make a list of mountains that exist, second compare the
    # elements to that list.
    existing_mountains = []
    for mountain in game_state.mountains.values():
        existing_mountains.append(mountain.token_value)
        
    moves_involving_real_mountains = []
    for possible_move in raw_list_of_moves:
        filtered_move = []
        for item in possible_move:
            if item in existing_mountains:
                filtered_move.append(item)
        moves_involving_real_mountains.append(filtered_move)
    
    # Include []. Kind of a hack
    moves_involving_real_mountains.append([])
    # Now strip out all of the duplicates by converting the list to a set
    # could make this faster with itertools https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
    final_output = [list(x) for x in set(tuple(sorted(sublist)) for sublist in moves_involving_real_mountains)]

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

