# encoding=utf8
from __future__ import unicode_literals
import spacy

article= "Russia coast past Saudi Arabia and leave them all smiling in Putins place."

nlp = spacy.load('en',tagger=False,parser=False,matcher=False)

# doc = nlp(unicode(article))
doc = nlp(article)

# print(doc.ents)
for ent in doc.ents:
    print(ent.label_ , ent.text)

# for ent in doc.ents:
#     print(ent,ent.label_)