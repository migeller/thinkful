#!/usr/bin/env python

"""

 MetaCode _____, version 1.0
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
    "bitter":  "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter":  ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def order():
    answers = {}
    for question in questions:
        this_answer = raw_input(questions[question]+' ')
        if this_answer[0].lower() == "y":
            answers[question] = True
        else:
            answers[question] = False
    return answers

def construct(preferences):
    drink = []
    for preference in preferences:
        if preferences[preference]:
            drink.append(random.choice(ingredients[preference]))
    return drink

if __name__ == '__main__':
    print ""
    print "Welcome to ye bar, matey!"
    print ""
    preferences = order()
    concoction = construct(preferences)
    print ""
    print "Here's what aye's going to use when makin' yer drink:"
    print concoction