import pandas as pd
import numpy as np
from nltk import word_tokenize
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
from gensim.test.utils import datapath,get_tmpfile

df = pd.DataFrame({'numeric':[1,2,3],'text':['pizza','hey there','I want a pizza']})
# print(df)

def sent_embedding(sentence):
    # print(sentence)
    sent_emb = np.mean([get_embeddings(sent) for sent in sentence],axis=0)
    return sent_emb

def get_embeddings(word):
    glove_file = datapath('/home/mohit/Desktop/git/glove.6B.50d.txt')
    tmp_file = get_tmpfile("glove_word2vec.txt")
    glove2word2vec(glove_file, tmp_file)
    model = KeyedVectors.load_word2vec_format(tmp_file)
    return model.wv[word]

# here text = row . iterating over all the rows of text column one by one
def preprocess(text):
    """
    to do 1) if no words found return unk token in order to get embeddings of unk
    :param text:
    :return:
    """
    text = text.lower()
    doc = word_tokenize(text)
    # doc = [word for word in doc if word not in stop_words]
    doc = [word for word in doc if word.isalpha()]
    embedding = sent_embedding(doc)
    return embedding

# add axis=1 to apply to each row?
df['features'] = df['text'].apply(preprocess)
df.to_csv('temp.csv')
# print(df)
# print(df.columns)
