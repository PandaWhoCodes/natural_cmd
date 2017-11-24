"""
Rule based functions. Rules are represented as a graph of
meta-edges from list of nodes to various actions, and are stored as a
lookup tree.
"""

from subprocess import call
import os
import glob


def ls(x=None):
    """
    Lists the files and directories in the given directory
    Parameters:
        params (dict): Path from current directory to directory to list
        files / directories from
    Returns:
        listing (list): A list of the files and directories in params
    """
    try:
        if x != None:
            os.chdir(x)
        else:
            x = os.getcwd()
        for f in os.listdir('.'):
            print(f, end="\t")
    except FileNotFoundError:
        print("I couldn't find file " + x)


def text2int(textnum, numwords={}):
    """
    Returns integer number from its string representation, or False if the
    string doesn't represent a number.
    """
    if not numwords:
        units = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
            "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
            "sixteen", "seventeen", "eighteen", "nineteen",
        ]

        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        scales = ["hundred", "thousand", "million", "billion", "trillion"]

        numwords["and"] = (1, 0)
        for idx, word in enumerate(units):    numwords[word] = (1, idx)
        for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
        for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
            return False

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

