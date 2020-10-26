#!/usr/bin/env python

### make this function as a standalone script or a module
### do this so that you can easily test it by running it through a large word list and find the exceptions

###   this is to get the diff inflections of an adjective:       class_='luna-inflected-form bold'


from bs4 import BeautifulSoup
import requests
import sys
import string

class Word:
    def __init__(self, word):
        self.word = word
        self.html = query_word(self.word)
        self.IPA = parse_IPA(self.html, self.word)
        self.strict_rhyme_end = strict_rhyme(self.IPA, self.word)
        self.loose_rhyme_end = loose_rhyme(self.strict_rhyme_end, self.word)
        self.parts_of_speech = get_POS(self.html, self.word)

        self.word_info = self.format_dict()

    def format_dict(self):
        word_vars = {}
        word_vars['word'] = self.word
        word_vars['part_of_speech'] = self.parts_of_speech
        #word_vars['html'] = self.html
        word_vars['IPA'] = self.IPA
        word_vars['strict_rhyme_end'] = self.strict_rhyme_end
        word_vars['loose_rhyme_end'] = self.loose_rhyme_end

        return word_vars

    def debug_word(self):
        print()
        for key in self.word_info.keys():
            print(key + ':', self.word_info[key])

def query_word(word):
    print("Querying word:", word)
    site = 'https://www.dictionary.com/browse/'

    try:
        page = requests.get(site + word)
        soup = BeautifulSoup(page.content, 'lxml')
    except:
        print("Skipping:", word, "((query word))")
        return
    return soup


def get_POS(soup, word):
    try:
        return soup.find(class_='luna-pos').text.replace(",", "")
    except:
        return None

def parse_IPA(soup, word):
    try:
        IPA_raw_text = soup.find(class_='pron-ipa-content css-cqidvf evh0tcl2').text
    except AttributeError:
        print("Skipping:",  word,  " class 'pron-ipa-content css-cqidvf evh0tcl2' does not exist")
        return
    except:
        print("unknown error")
        sys.exc_info()[0]
    return clean_up(IPA_raw_text)

def clean_up(IPA_text):
    ### this probably needs to be rewritten. so many branches and so many weird exceptions.

    parts_of_speech = ['noun', 'pronoun', 'verb', 'adjective', 'adverb', 'preposition', 'conjunction', 'interjection']

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

    for part in parts_of_speech:
        IPA_text = IPA_text.replace(part, '')

    ### this is to handle the secondary accent
    IPA_text = IPA_text.replace('ˌ', ' ˌ')

    return IPA_text.replace("/", "").strip()

def strict_rhyme(IPA, word):
    IPA_vowels = set(['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'ə', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ɑ', 'ɒ'])

    try:
        IPA_list = IPA.split()
        rhyme = IPA_list[-1]

        ### fix one syllable words ending in a vowel. allow them to represent their own ending in full
        if len(IPA_list) == 1 and rhyme[-1] in IPA_vowels:
            return rhyme
        ### if the last sound is a vowel, use the last two syllables
        elif rhyme[-1] in IPA_vowels:
            rhyme = IPA_list[-2] + IPA_list[-1]

        ### if the last sound is a consonant, use only the last syllable
        for i in range(len(rhyme)):
            if rhyme[i] in IPA_vowels:
                rhyme = rhyme[i:]
                break
        return rhyme


    except TypeError:
        print("Skipping:", word, "-- no string fed to strict_rhyme()")
        return
    except AttributeError:
        print("attribute error. None type fed to strict_rhyme()")    
        return
    except:
        print('unkown error occurred strict rhyme')
        print(sys.exc_info()[0])
        return

def loose_rhyme(ending, word):
    IPA_vowels = set(['i', 'y', 'ɨ', 'ʉ', 'ɯ', 'u', 'ɪ', 'ʏ', 'ʊ', 'e', 'ø', 'ɘ', 'ɵ', 'ɤ', 'o', 'ə', 'ɛ', 'œ', 'ɜ', 'ɞ', 'ʌ', 'ɔ', 'æ', 'ɐ', 'a', 'ɶ', 'ɑ', 'ɒ'])

    try:
        
        
        ### if the last sound is a vowel, ignore the consonants
        if ending[-1] in IPA_vowels:
            for char in ending:
                if char not in IPA_vowels:
                    ending = ending.replace(char, '_')
                    return ending
        
        ### if the last sound is a consonant, ignore the first consonant
        for i in range(len(ending)):
            if ending[i] not in IPA_vowels:
                ending = ending[:i]
                return ending
    except TypeError:
        print('Skipping:', word, "-- no string fed to loose_rhyme()")
    except AttributeError:
        print("attribute error. None type fed to loose_rhyme()")
    except:
        print('unkown error occurred loose rhyme')
        sys.exc_info()[0]
        return


if __name__ == "__main__":
    new_word = Word(sys.argv[1])
    
    new_word.debug_word()