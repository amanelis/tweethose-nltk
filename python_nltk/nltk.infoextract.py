#!/usr/bin/python
import nltk
from nltk.corpus import ieer, conll2002

for doc in conll2002.chunked_sents('ned.train')[27]:
	print doc



