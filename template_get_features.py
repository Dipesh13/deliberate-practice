import numpy as np
from nltk import word_tokenize
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath,get_tmpfile

def word_embedding(word):
    # print(word)
    word_emb = get_embeddings(word)
    print(word_emb)

def sent_embedding(sentence):
    """
    lower case , remove puncutations and numbers.
    """
    tokens = [w for w in word_tokenize(sentence.lower()) if w.isalpha()]
    sent_emb = np.mean([get_embeddings(t) for t in tokens],axis=0)
    print(sent_emb)

def get_embeddings(word):
    glove_file = datapath('/home/dipesh/deliberate-practice/glove.6B.50d.txt')
    tmp_file = get_tmpfile("glove_word2vec.txt")
    glove2word2vec(glove_file, tmp_file)
    model = KeyedVectors.load_word2vec_format(tmp_file)
    return model.wv[word]

word = 'pizza'
word_embedding(word)
sentence = 'I want to order 5 pizzas.'
sent_embedding(sentence)
