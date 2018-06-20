import pandas as pd
# import numpy as np
# import json
# from sklearn.base import TransformerMixin
# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import Imputer
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import FunctionTransformer


list_df= [[1,2,3,4,5],[5,6,7,8,9],['and','the','an','a','if'],['bob','foo','bar','boo','bob'],[1,0,0,1,1]]

df= pd.DataFrame(list_df)
df = df.T
# print(df)

num_cols = [0,1]
text_cols = [2,3]

get_text_data = FunctionTransformer(lambda x: x[2], validate=False)
get_numeric_data = FunctionTransformer(lambda x: x[[0,1]], validate=False)

# Fit and transform the text data: just_text_data
just_text_data = get_text_data.fit_transform(df)

# Fit and transform the numeric data: just_numeric_data
just_numeric_data = get_numeric_data.fit_transform(df)

# Print head to check results
print('Text Data')
print(just_text_data.head())
print('\nNumeric Data')
print(just_numeric_data.head())