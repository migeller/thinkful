#!/usr/bin/env python

"""

 MetaCode Pirate Bartender, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.

"""

__author__ = 'MetaCode, Inc.'
__version__ = 'Revision 1.0'
__date__ = '11/13/14 11:44 AM'
__copyright__ = 'Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.'
__license__ = 'Python'
__ide__ = 'PyCharm'

import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["shivery", "rusty", "blasted", "cantankerous", "frilly", "sandy"]
nouns = ["fart", "smartphone", "rhinoceros", "smile", "booty", "timbers"]


def identify(all_preferences):
    print ""
    customer = raw_input("What be yer name, matey? ")
    if customer in all_preferences:
        print ""
        print "Quite the pleasure to serve ye again, " + customer + "."
        preferences = all_preferences[customer]
    else:
        print ""
        print "Aye see yer a new lubber, {}. Let me ask ye some questions...".format(customer)
        preferences = order()
        all_preferences[customer] = preferences
    return customer, preferences, all_preferences


def order():
    answers = {}
    for question in questions:
        this_answer = raw_input(questions[question] + ' ')
        answers[question] = this_answer[0].lower() == "y"
    return answers


def construct(preferences):
    drink = []
    for preference in preferences:
        if preferences[preference]:
            drink.append(random.choice(ingredients[preference]))
    return drink


def drink_name():
    name = random.choice(adjectives) + " " + random.choice(nouns)
    return name.title()


def recipe(ingredients):
    for index, ingredient in enumerate(ingredients):
        if ingredient[0].lower() in ["a", "e", "i", "o", "u"]:
            article = "An "
        else:
            article = "A "
        if len(ingredients) == 1:
            print article + ingredient + "."
        elif index != len(ingredients) - 1:
            print article + ingredient + ","
        else:
            print "And " + article.lower() + ingredient + "."


def ask():
    answer = raw_input("Would ye like another round? ")
    result = answer[0].lower() == "y"
    return result


def main():
    another = True
    all_preferences = {}
    print ""
    print "Welcome to ye bar, matey!"
    while another:
        customer, preferences, all_preferences = identify(all_preferences)
        concoction = construct(preferences)
        print ""
        print "{}, here's what aye's going to use when makin' yer drink:".format(customer)
        recipe(concoction)
        print "Aye call it the \"" + drink_name() + "\"!"
        print ""
        another = ask()
    else:
        print ""
        print "Safe travels on yer way home, matey!"


if __name__ == '__main__':
    main()