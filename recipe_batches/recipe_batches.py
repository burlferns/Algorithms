#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    max_batches = 0
    first_item = True
    for key in recipe:
        if key not in ingredients.keys():
            return 0
        if first_item:
            max_batches = (ingredients[key] // recipe[key])
            first_item = False
        elif (ingredients[key] // recipe[key]) < max_batches:
            max_batches = (ingredients[key] // recipe[key])

    return max_batches




if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
