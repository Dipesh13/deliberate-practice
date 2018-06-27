import numpy as np
from nltk import word_tokenize
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath,get_tmpfile

def sent_embedding(sentence):
    """
    1) lower case , remove puncutations and numbers.
    2) add check for 1) empty sentence 2) sentence containing all words which are out of vocab. unk token
    """
    tokens = [w for w in word_tokenize(sentence.lower()) if w.isalpha()]
    sent_emb = np.mean([get_embeddings(t) for t in tokens],axis=0)
    # print(sent_emb)
    return sent_emb

def get_embeddings(word):
    glove_file = datapath('/home/dipesh/deliberate-practice/glove.6B.50d.txt')
    tmp_file = get_tmpfile("glove_word2vec.txt")
    glove2word2vec(glove_file, tmp_file)
    model = KeyedVectors.load_word2vec_format(tmp_file)
    # return model[word]
    return model.wv[word]

sentences = ['pizza','I want to order 5 pizzas.']
for sentence in sentences:
    test = sent_embedding(sentence)
    print(test)