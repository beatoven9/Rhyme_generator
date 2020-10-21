#!/usr/bin/env python

### this program should:
###     *take a list of words
###     *query the web to see if it's a verb
###     *if it is a verb, record the IPA in a dict where the word is the key
###     *make a list of possible IPA vowels
###     *find the index of the first IPA vowel
###     *cut off everthing before the first vowel
###
### this will make only strict rhymes. future functionality could be to have a switch to allow loose rhymes as well
###
###

from bs4 import BeautifulSoup
import requests
from common_words.common_words import compile_histograms

def main():
    site = 'https://www.dictionary.com/browse/'
    word = 'bow'
    query_web_dict(site, word)

def query_web_dict(site, word):
    page = requests.get(site + word)
    soup = BeautifulSoup(page.content, 'html.parser')
    part_of_speech = pos_check(soup)
    print(part_of_speech)

def pos_check(soup):
    raw_pos_text = soup.find(class_="luna-pos").text
    pos = raw_pos_text[:4]
    if pos == 'verb':
        return (pos, raw_pos_text[5:])


if __name__ == "__main__":
    main()