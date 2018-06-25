# -*- coding: utf-8 -*-
import spacy
import pandas as pd
from create_dataset import df

nlp = spacy.load('en')
X= df['data']
y = df['labels']

df['data'] = df['data'].apply(lambda x : nlp(x.decode('utf-8')).vector)

print(df['data'].head(1))