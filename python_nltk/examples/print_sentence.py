import nltk

for line in open("file.txt"):
	for word in line.split():
		print word
