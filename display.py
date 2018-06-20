# encoding=utf8
import spacy
from spacy import displacy

#  to do : add this to jupyter notebook
nlp = spacy.load('en')
doc_dep = nlp(u'This is a sentence.')
displacy.serve(doc_dep, style='dep')

doc_ent = nlp(u'When Sebastian Thrun started working on self-driving cars at Google '
              u'in 2007, few people outside of the company took him seriously.')
displacy.serve(doc_ent, style='ent')
