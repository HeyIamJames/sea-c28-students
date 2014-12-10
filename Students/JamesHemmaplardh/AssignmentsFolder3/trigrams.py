#this requires NLTK, "sudo pip install -U nltk", assuming you have pip.

"""This creates trigrams from text, change n to ngarms""" 
from nltk.util import ngrams
text = "This is just a short story to prove that this works. It is very boring. Once I walked into a car and drove, then I got fast food at McDonalds. I went home and cried. At the end of the day I realized McDonalds is bad"
n = 3
trigrams = ngrams(text.split(), n)
for i in trigrams:
  print i
