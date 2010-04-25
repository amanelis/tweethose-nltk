#!/usr/bin/python
import nltk
from nltk import wordpunct_tokenize

s = ("Good muffins cost $3.88\nin New York. Please buy me \n two of them\n")
print wordpunct_tokenize(s)


