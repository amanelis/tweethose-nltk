import sys
import nltk
from nltk import word_tokenize, wordpunct_tokenize
from nltk.tokenize import *

def find_words(text, wordlength, result=[]):
	for word in text:
		if len(word) == wordlength:
			result.append(word)
	return result

def tokenizers(text1):
	sent1 = text1

	#simple tokenizer, uses regexp
	TreebankWordTokenizer().tokenize(sent1)

	#same as sent1.split()
	WhitespaceTokenizer().tokenize(sent1)

	#same as sent1.split(' ')
	SpaceTokenizer().tokenize(sent1)

	#same as sent1.split('\n')
	LineTokenizer(blanklines='keep').tokenize(sent1)

	#same as [l for l in s.split('\n') if l.strip()]
	LineTokenizer(blanklines='discard').tokenize(sent1)


if sys.argv[1:] == []:
	print "USAGE: python ./executable [size of word]\n"
	sys.exit()

num = int(sys.argv[1])
print find_words(['omg', 'bee', 'tree', 'help', 'at', 'is'], num)
