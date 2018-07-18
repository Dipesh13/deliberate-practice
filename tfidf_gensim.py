corpus = 'the big brown fox jumped over the lazy fox'

tfidf = gensim.models.tfidfmodel.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
d = {}
for doc in corpus_tfidf:
    for id, value in doc:
        word = dictionary.get(id)
        d[word] = value