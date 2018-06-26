import pandas as pd
import argparse

def dataframe_test(dataframe,label=''):
    if label:
        dataframe = df[df['label'] == label]
        X = dataframe['query']
        y = dataframe['label']
        print(X.head())
    else:
        X = dataframe['query']
        y = dataframe['label']
        print(X.head())

if __name__ == '__main__':
    colnames=['query','label']
    df = pd.read_csv('FoodBot Intents - Examples.csv', names=colnames)
    parser = argparse.ArgumentParser(description='train one class svm.')
    # parser.add_argument('-filename', help='path to an excel file')
    parser.add_argument('-label', help='subtype/type for which you want to train the bot', required=False,
                        choices=['Book Table', 'Checkout', 'Order'])
    args = parser.parse_args()
    # filename = args.filename
    if args.label:
        dataframe_test(df,args.label)
    else:
        dataframe_test(df)
