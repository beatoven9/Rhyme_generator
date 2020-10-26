#!/usr/bin/env python

### add a second json mapper. this one should be a dictionary with words as keys and IPA endings as values.
### generate_rhyme.py will take in a word as a command_line argument, check if it knows the word and give the list of rhymes.
### if it doesn't know the word, it will look it up, add it to both dictionaries, then give you rhymes. 

from word_query import Word
import sys
import json

def make_word_dict():
    filename = open('common_words.txt', 'r')
    word_list = {}

    for word in filename.readlines()[:1000]:
        new_word = Word(word.strip()) 
        word_list[new_word.word] = new_word.word_info

#    for word in word_list.keys():
#        print(word, word_list[word])
#
    return word_list


def make_ending_dict(word_dict):
    ending_dict = {}
    for word in word_dict.keys():
        ending_dict[word_dict[word]['strict_rhyme_end']] = ending_dict.setdefault(word_dict[word]['strict_rhyme_end'], [])
        ending_dict[word_dict[word]['strict_rhyme_end']].append(word)

    return ending_dict

if __name__ == "__main__":
    word_dict = make_word_dict()
    ending_dict = make_ending_dict(word_dict)
    
    with open('endings.json', 'w') as outfile:
        json.dump(ending_dict, outfile, indent=4)
