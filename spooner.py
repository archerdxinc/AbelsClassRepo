#!/usr/bin/env python

import argparse

def spoonit(firstword, secondword):
    print "{} {}".format(firstword, secondword)
    print "{}{} {}{}".format(secondword[0], firstword[1:], firstword[0], secondword[1:])

def main():
    parser = argparse.ArgumentParser("Print the spoonerism of two words")
    parser.add_argument('firstword', action="store", type=str, default="Abel")
    parser.add_argument('secondword', action="store", type=str, default="Licon")
    words = parser.parse_args()
    return spoonit(words.firstword, words.secondword)

def foo():
    hello

if "__main__" == __name__:
    main()
