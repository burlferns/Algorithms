#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    all_plays = []
    rps_list = ['rock', 'paper', 'scissors']
    current_play = [''] * n

    def recursive_helper(current_play, recursive_level):
        for i in rps_list:
            current_play[recursive_level] = i
            if recursive_level < n - 1:
                recursive_helper(current_play, recursive_level + 1)
            if recursive_level == n - 1:
                all_plays.append(current_play.copy())

    if n > 0:
        recursive_helper(current_play, 0)
        return all_plays
    else:
        return [[]]





if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
