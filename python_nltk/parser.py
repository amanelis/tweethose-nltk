import nltk
import tweetstream
import sys
from nltk import Nonterminal, nonterminals, Production, parse_cfg, ContextFreeGrammar
from nltk.corpus import treebank

#Standard sentence parsing
nltk.parse.chart.demo(1, should_print_times=False, trace=1,sent='I saw John with a dog', numparses=2)

