#!/usr/bin/python
import nltk
from nltk.corpus import wordnet as wn

motorcar = wn.synset('car.n.01')
types_of_motorcar = motorcar.hyponyms()
print types_of_motorcar[26]
