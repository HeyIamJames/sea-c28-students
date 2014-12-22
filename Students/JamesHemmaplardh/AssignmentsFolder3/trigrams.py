"""take a file and creates trigrams"""

from io import open
import sys
import string
import random


def create_words(text):
    get_words = open(text, 'r')
    text = get_words.read()
    words = []
    for word in text.split(): 
        word = word.strip(string.punctuation + string.whitespace) 
        word = word.lower() 
        words.append(word)
    return words

def create_trigrams(words):
    trigram = {}   
    for i in range(len(words)-2):
        key = (words[i], words[i+1])
        if key not in  trigram:
            value = [words[i+2]]
            trigram[key] = value
        else:   
            trigram[key].append(words[i+2])
    return trigram

def create_text():
    new = ''
    for key, value in trigram.items():
        value = value[random.randint(0,len(value)-1)]
        new += ' ' + value
    return new

if __name__ == '__main__':
    words = create_words(sys.argv[1])
    trigram = create_trigrams(words)
    print create_text()
    