import nltk
from nltk import word_tokenize, wordpunct_tokenize

text = nltk.word_tokenize("And now for something, completely different.")
nltk.pos_tag(text)

print text
