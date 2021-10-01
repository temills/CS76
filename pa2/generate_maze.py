#!/usr/bin/env python3
import random

def gen_maze(name, num_rows, num_cols, num_robots):
    random.seed()
    maze = []
    with open(name+'.maz', 'w') as f:
        for r in range(num_rows):
            ln_list = random.sample(['#', '.'], counts=[1*num_cols, 4*num_cols], k=num_cols)
            maze.append(ln_list)
            ln = ""
            for c in ln_list:
                ln = ln + c
            f.write(ln + '\n')
        bots = []
        for i in range(num_robots):
            done = False
            while done==False:
                x = random.sample(range(num_cols-1), k=1)[0]
                y = random.sample(range(num_rows-1), k=1)[0]
                if maze[num_rows-1-y][x] == '.' and ((x,y) not in bots):
                    bots.append((x,y))
                    f.write('\\robot ' + str(x) + ' ' + str(y) + '\n')
                    done=True

gen_maze('maze10', 30, 30, 1)