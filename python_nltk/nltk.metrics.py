#!/usr/bin/python
import nltk
from nltk.metrics import precision, recall, f_measure

reference = 'DET NN VB DET JJ NN NN IN DET NN'.split()
test    = 'DET VB VB DET NN NN NN IN DET NN'.split()
reference_set = set(reference)
test_set = set(test)

print "Precision: "
print precision(reference_set, test_set)

print "\n"

print "Recall: "
print recall(reference_set, test_set)

print "\n"

print "F_Measure: "
print f_measure(reference_set, test_set)

