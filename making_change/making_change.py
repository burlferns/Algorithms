#!/usr/bin/python

import sys

############################################################
# First version
############################################################
def making_change(amount, denominations):

    def recur_helper(n, branch_control):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        if branch_control == 50:
            return recur_helper(n - 50, 50) \
                + recur_helper(n - 25, 25) \
                + recur_helper(n - 10, 10) \
                + recur_helper(n - 5, 5) \
                + recur_helper(n - 1, 1)

        if branch_control == 25:
            return recur_helper(n - 25, 25) \
                + recur_helper(n - 10, 10) \
                + recur_helper(n - 5, 5) \
                + recur_helper(n - 1, 1)

        if branch_control == 10:
            return recur_helper(n - 10, 10) \
                + recur_helper(n - 5, 5) \
                + recur_helper(n - 1, 1)

        if branch_control == 5:
            return recur_helper(n - 5, 5) \
                + recur_helper(n - 1, 1)

        if branch_control == 1:
            return recur_helper(n - 1, 1)


    return recur_helper(amount, 50)







if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
