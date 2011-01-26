import nltk
from nltk.grammar import ContextFreeGrammar,Nonterminal,Production

# function that removes suffixes from a nonterminal
# input: a Nonterminal
# output: the cleaned Nonterminal
def clean_nt(nt):
  sym = nt.symbol()
  if(sym=='-NONE-'):
    return Nonterminal('-NONE-')
  else:
    return Nonterminal(sym.split('-')[0])

# function that cleans all of the Nonterminals in a given Production
# input: a Production
# output: the cleaned Production  
def clean_production(p):
  lhs = clean_nt(p.lhs())
  rhs = [clean_nt(x) for x in p.rhs()]
  return Production(lhs,tuple(rhs))

s = nltk.corpus.treebank.parsed_sents()
p = []
g = []

# let p = a list of all productions in the treebank
for x in s:
  for y in x.productions():
    p += [y]

plex = []
prules = []

# split rules into lex rules and other productions
for prod in p:
  if len(prod.rhs())>0 and isinstance(prod.rhs()[0],str):
    plex += [prod]
  else:
    prules += [prod]

print len(plex)
print len(prules)

# remove annotations from nonterminals in rules
crules = [clean_production(x) for x in prules]

# get rid of rules with -NONE- and NP->NP, VP->VP

drules = []

for y in crules:
    b = True
    for z in y.rhs():
      if z == Nonterminal('-NONE-'):
        b = False
    # delete rules where lhs = rhs    
    if b and (len(y.rhs())>1 or y.lhs()!=y.rhs()[0]):
      drules += [y]
print len(drules)

#tree.collapse_unary(collapsePOS = False) 
#tree.chomsky_normal_form(horzMarkov = 2) 

# srules is the set of non-lexical rules with duplicates removed
srules = list(set(drules))
print len(srules)

# slex is the set of lexical rules with duplicates removed
slex = list(set(plex))
print len(slex)

# create a nonprobabilistic parser
grammar = ContextFreeGrammar(Nonterminal('S'),srules+slex)
parser = nltk.parse.chart.ChartParser(grammar)

# create a probabilistic parser
wgrammar = nltk.induce_pcfg(Nonterminal('S'),plex+drules)
wparser = nltk.parse.viterbi.ViterbiParser(wgrammar)

# try out the probabilistic parser on a few sentences
t = "that is very interesting .".split(' ')
trees = wparser.nbest_parse(t,n=10)
print trees

u = "from the beginning to the end , it was an entertaining game .".split(' ')
trees = wparser.nbest_parse(u,n=10)
print trees

v = "the workers dumped sacks into a bin .".split(' ')
trees = wparser.nbest_parse(v,n=10)
print trees
print trees[0].productions()
