#!/usr/bin/python

import sys

############################################################
# First version
############################################################
# def making_change(amount, denominations):

#     def recur_helper(n, branch_control):
#         if n < 0:
#             return 0
#         elif n == 0:
#             return 1

#         if branch_control == 50:
#             return recur_helper(n - 50, 50) \
#                 + recur_helper(n - 25, 25) \
#                 + recur_helper(n - 10, 10) \
#                 + recur_helper(n - 5, 5) \
#                 + recur_helper(n - 1, 1)

#         if branch_control == 25:
#             return recur_helper(n - 25, 25) \
#                 + recur_helper(n - 10, 10) \
#                 + recur_helper(n - 5, 5) \
#                 + recur_helper(n - 1, 1)

#         if branch_control == 10:
#             return recur_helper(n - 10, 10) \
#                 + recur_helper(n - 5, 5) \
#                 + recur_helper(n - 1, 1)

#         if branch_control == 5:
#             return recur_helper(n - 5, 5) \
#                 + recur_helper(n - 1, 1)

#         if branch_control == 1:
#             return recur_helper(n - 1, 1)


#     return recur_helper(amount, 50)


############################################################
# Second version
############################################################
def making_changeOFF(amount, denominations):

    sorted_denom = denominations.copy()
    sorted_denom.sort()

    def recur_helper(n, branch_control):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        sum = 0
        for i in range(len(branch_control)):
            sum += recur_helper(n - branch_control[i], branch_control[0:i + 1])

        # print(f'sum={sum}')

        return sum

    return recur_helper(amount, sorted_denom)


############################################################
# Third version
#       --- Note recursion limit is changed to 100000
############################################################
sys.setrecursionlimit(100000)
def making_change(amount, denominations):

    sorted_denom = denominations.copy()
    sorted_denom.sort()
    cache = {}

    def recur_helper(n, branch_control):
        if n < 0:
            return 0
        elif n == 0:
            return 1

        sum = 0
        for i in range(len(branch_control)):
            if (f'{n - branch_control[i]},{i+1}') in cache.keys():
                sum += cache[f'{n - branch_control[i]},{i+1}']
            else:
                cache[f'{n - branch_control[i]},{i+1}'] =  \
                    recur_helper(
                        n - branch_control[i], branch_control[0:i + 1])
                sum += cache[f'{n - branch_control[i]},{i+1}']

        return sum

    return recur_helper(amount, sorted_denom)


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
