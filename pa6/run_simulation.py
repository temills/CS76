#!/usr/bin/env python3
# Tracey Mills 11/15/2021
# This file runs the HMMbot simulation

import random
from HMMbot import HMMbot
from Maze import Maze

num_iter = 10
random.seed(2)

maze = Maze("maze0.maz")
#maze = Maze("maze1.maz")
#maze = Maze("maze2.maz")

bot = HMMbot(maze)
# Returns location after robot attempts to make a random move
# Attempts to move N,S,E or W each with equal probability
# Walls stop movement
def move(bot, true_loc):
    dir = random.choice(["N","E","S","W"])
    return bot.make_given_move(true_loc, dir), dir


# Returns color sensed by robot (r, g, b, or y)
# True color with probability 0.88
# Any other color with probability 0.04
def sense(bot, true_loc):
    true_color = bot.maze.get_color(true_loc[0], true_loc[1])
    other_colors = ["r","g","y","b"]
    other_colors.remove(true_color)
    
    r = random.random()

    if r<0.88:
        return true_color
    elif r<0.92:
        return other_colors[0]
    elif r<0.96:
        return other_colors[1]
    else:
        return other_colors[2]

# Runs simulation
def run(bot):
    print("Predictions before sensing")
    bot.print_distr()

    print("True starting location")
    true_loc = random.choice(bot.locs)
    bot.print_maze(true_loc)

    color = sense(bot, true_loc)
    print("Sensed color " + color)
    bot.step(color)
    print("Updated predictions")
    bot.print_distr()

    for i in range(num_iter):
        print("Step " + str(i+1))
        print("-------------")
        #robot moves
        true_loc, dir = move(bot, true_loc)
        #senses color
        color = sense(bot, true_loc)
        
        print("Attemped move " + dir + ", sensed color " + color)

        print("True location")
        #print true location
        bot.print_maze(true_loc)
        #update predictions
        bot.step(color)
        print("Updated predictions")
        #print predictions
        bot.print_distr()

run(bot)


