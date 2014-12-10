#this requires NLTK, "sudo pip install -U nltk", assuming you have pip.

from nltk.util import ngrams
sentence = "This is just a short story to prove that this works. It is very boring. Once I walked into a car and drove, then I got fast food at McDonalds. I went home and cried. At the end of the day I realized McDonalds is bad"
n = 3
trigrams = ngrams(sentence.split(), n)
for grams in trigrams:
  print grams
