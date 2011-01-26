from nltk import parse_cfg, draw
from nltk.parse import ChartParser, TD_STRATEGY

def parse(sentence, cfg):
    grammar = parse_cfg(cfg)
    parser = ChartParser(grammar, TD_STRATEGY)
    words = sentence.split()
    draw.draw_trees(*parser.get_parse_list(words))

grammar = """
   NP -> P | D J N
   D -> 'a'
   J -> 'red' | 'green'
   N -> 'chair' | 'couch'
"""

grammer = """
   S -> NP VP
   VP -> V NP
   NP -> Det N
   Det -> 'the'
   N -> 'cat' | 'dog'
   V -> 'chased'
"""

phrase = 'the cat chased the dog'
parse(phrase, grammar)
