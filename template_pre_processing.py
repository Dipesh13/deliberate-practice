import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer

label = ['Hi! , I want to order 5 pizzas.']

df = pd.DataFrame({'data':label})
print(df)

# 1)no need to lower case as tfidf take care of that
# df['data'] = df['data'].str.lower()
# print(df)

# 2) remove punctuation
df['data']= df['data'].apply(lambda x: x.translate(None, string.punctuation))
print(df)

# 3) remove digits
df['data']= df['data'].apply(lambda x: x.translate(None, string.digits))
print(df)

# 4) lowercase and remove stop words usinf tfidf itself.
vectorizer= TfidfVectorizer(stop_words='english',ngram_range=(1,3),min_df=3,max_df=100,max_features=None)