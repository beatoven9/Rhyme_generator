#!/usr/bin/env python

### this program should:
###     *take a list of words
###     *make a list of possible IPA vowels
###     *find the index of the first IPA vowel
###     *cut off everything before the first vowel
###
###
###

### IPA_vowels = ['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'ə', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ɑ', 'ɒ']

from common_words.common_words import compile_histograms
from word_query import Word
import sys

def main():
    new_word = Word(sys.argv[1])
    new_word.debug_word()

if __name__ == "__main__":
    main()

