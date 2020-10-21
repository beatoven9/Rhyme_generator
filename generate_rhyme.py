#!/usr/bin/env python

### this program should:
###     *take a list of words
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


if __name__ == "__main__":
    main()