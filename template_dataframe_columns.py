import pandas as pd

def dataframe_test(dataframe,label,numeric_col=[],text_col=[],categorical_col=[]):
    if numeric_col:
        num_data = dataframe[numeric_col]
        # print(num_data.head(1))
    if text_col:
        text_data = dataframe[text_col]
        # print(text_data.head(1))
    if categorical_col:
        categorical_data = dataframe[categorical_col]
        # print(categorical_data.head(1))
    label = dataframe[label]
    # print(label.head(1))

df = pd.read_csv('train.csv')
numeric_col = ['id','B','C']
text_col = ['D','E','F','G']
categorical_col = ['H']
label = ['P']
# call the function and pass numeric col, text col , categorical col and  labels
dataframe_test(df,label,numeric_col,text_col,categorical_col)