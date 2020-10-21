#!/usr/bin/env python

import string
import re
import sys

def create_histogram(src_file):
    src = open(src_file, "r")

    histogram = {}
### add puncuation specific to the 'Project Gutenberg' texts to be parsed
    punctuation = string.punctuation + '’' + '“' + '”' + '‘' + '‘' + '\n'
    for line in src.readlines():
        for word in re.split('[— :]', line):
            word = word.translate(word.maketrans('', '', punctuation))
            histogram[word.lower()] = histogram.setdefault(word.lower(), 0) + 1
    return histogram


def main():
    txt_file = sys.argv[1]
    create_histogram(txt_file)

if __name__ == "__main__":
    main()
