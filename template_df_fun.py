import pandas as pd

def dataframe_test(dataframe,column_name=''):
    if column_name:
        dataframe = df[df['label'] == column_name]
        X = dataframe['query']
        y = dataframe['label']
        print(X.head())
    else:
        X = dataframe['query']
        y = dataframe['label']
        print(X.head())

colnames=['query','label']
df = pd.read_csv('FoodBot Intents - Examples.csv', names=colnames)

dataframe_test(df,'Order')
dataframe_test(df)