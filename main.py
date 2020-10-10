"""
Input: str (written numeral)
Output: float/int (numeral in digits)
"""

import pandas as pd
import numpy as np
from itertools import chain
# 'One-hundred'

# Need to create a list of written numerals as a starting point
wordnumdict = {'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'nine':10,
                'eleven':11,
                'twelve':12,
                'thirteen':13,
                'fourteen':14,
                'fifteen':15,
                'sixteen':16,
                'seventeen':17,
                'eighteen':18,
                'nineteen':19,
                'twenty':20,
                'thirty':30,
                'forty':40,
                'fifty':50,
                'sixty':60,
                'seventy':70,
                'eighty':80,
                'ninety':90,
                'one hundred':100,
                'one thousand':1000}

word = 'one thousand, two hundred and thirty-four and 56/100'
#1000+200+30+4+.56 = 1234.56

def flatten_listoflists(l):
    #works for list of lists, i.e. not list of list of lists
    return [item for sublist in l for item in sublist]

def split_delim(l, delim):
    return [str(l[i]).split(delim) for i in range(0, len(l))]

def word_splitter(word):
    split_commas = word.split(', ')
    split_and = flatten_listoflists(split_delim(split_commas, ' and '))
    split_hyphen = flatten_listoflists(split_delim(split_and, '-'))
    return split_hyphen

def match_word2num(l):
    # check if written numeral is a key in wordnumdict
    # if not, split item apart to see if contains 'hundred' or 'thousand'
    numlist = []
    for item in l:
        if item in wordnumdict:
            numlist.append(wordnumdict[item])
        else:
            split_item = item.split()
            if 'hundred' in split_item:
                split_item = int(wordnumdict[split_item[0]]) * 100
            elif 'thousand' in split_item:
                split_item = int(wordnumdict[split_item[0]]) * 1000
                # TODO: figure out how to handle '/'
            numlist.append(split_item)
    return numlist

print(match_word2num(word_splitter(word)))

