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
    verb_check(soup)

def verb_check(soup):
    part_of_speech = soup.find(class_="luna-pos").text
    print(part_of_speech)

if __name__ == "__main__":
    main()