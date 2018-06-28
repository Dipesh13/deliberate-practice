# encoding=utf8
import spacy

nlp = spacy.load('en')
# tokens = nlp(u'dog cat banana')

# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))

with open('../doc-classification/football/zlatan-ibrahimovic-in-spotlight-again-after-red-card-for-slapping-opponent.txt','rb') as fi:
    doc1 = fi.read().decode('utf8')
    token1 = nlp(doc1)
with open('../doc-classification/football/zlatan-ibrahimovics-red-card-la-galaxy-mls.txt','rb') as fo:
    doc2 = fo.read().decode('utf8')
    token2 = nlp(doc2)

# use this for recommendation :
# to do 1) find top tokens for each class then calculate score of new article wrt each class and print max score
print(token1.similarity(token2))
# print(token1.vector)