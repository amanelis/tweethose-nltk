#!/usr/bin/python
import nltk
from nltk.corpus import wordnet as wn

#print wn.synsets('dog')

dog = wn.synset('dog.n.01')
boat = wn.synset('run.v.01')

print dog.path_similarity(boat)

