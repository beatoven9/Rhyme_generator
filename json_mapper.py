#!/usr/bin/env python

from word_query import Word
import sys
import json

def make_word_dict():
    filename = open('common_words.txt', 'r')
    word_list = {}

    for word in filename.readlines()[:100]:
        new_word = Word(word.strip()) 
        word_list[new_word.word] = new_word.word_info

    for word in word_list.keys():
        print(word, word_list[word])

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
