#!/usr/bin/python
import nltk
from nltk.corpus import treebank
from itertools import islice
from nltk import parse_pcfg, induce_pcfg, toy_pcfg1, toy_pcfg2
from nltk.parse import ViterbiParser

#nltk.parse.chart.demo(2, should_print_times=False, trace=1, sent='I saw John with a dog', numparses=2)

nltk.parse.featurechart.demo(should_print_times=False,
							 should_print_grammar=False, trace=1,
							 parser=nltk.FeatureTopDownChartParser,
							 sent='I saw John with a dog')


