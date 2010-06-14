#!/usr/bin/python
import nltk
from nltk.tokenize import *

s = ("Good muffins cost $3.88\nin New York. Please buy metwo of them.\n\nThanks.")

tokens = word_tokenize(s)
capword = RegexpTokenizer('[A-Z]\w+').tokenize(s)





