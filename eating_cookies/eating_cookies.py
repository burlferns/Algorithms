#!/usr/bin/python

import sys

############################################################
# First version
############################################################
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookiesOFF(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1

    return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


############################################################
# Second version
############################################################
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1


    terms = [0, 0, 0, 0]
    for i in [1, 2, 3]:
        if cache != None and cache[n - i] != 0:
            terms[i] = cache[n - i]
        else:
            terms[i] = eating_cookies(n - i, cache)
            if cache != None:
                cache[n - i] = terms[i]

    sum = terms[1] + terms[2] + terms[3]

    return sum






if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
