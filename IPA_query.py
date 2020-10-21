#!/usr/bin/env python

### make this function as a standalone script or a module
### do this so that you can easily test it by running it through a large word list and find the exceptions

from bs4 import BeautifulSoup
import requests
import sys

def get_IPA(site, word):
    page = requests.get(site + word)
    soup = BeautifulSoup(page.content, 'html.parser')


    try:
        IPA_raw_text = soup.find(class_='pron-ipa-content css-cqidvf evh0tcl2').text
    except:
        print("Skipping: " + word)
        return
    return clean_up(IPA_raw_text)

def clean_up(IPA_text):
    comma_index = IPA_text.find(",")
    if comma_index > 0:
        IPA_text = IPA_text[:comma_index]
    

    ### this is to catch the semicolon in the words 'an' and 'the'
    semi_colon_index = IPA_text.find(";")
    if semi_colon_index > 0:
        IPA_text = IPA_text[:semi_colon_index]

    ### this is to delete the word "stressed" from the word 'the'
    sub_string = 'stressed'
    IPA_text = IPA_text.replace(sub_string, '')

    return IPA_text.replace("/", "").strip()

def main():
    site = 'https://www.dictionary.com/browse/'
    print(get_IPA(site, sys.argv[1]))

if __name__ == "__main__":
    main()