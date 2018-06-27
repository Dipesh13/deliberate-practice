import pandas as pd

column = ['query','label']
df = pd.read_csv('/home/dipesh/deliberate-practice/test.csv',names=column)

labels = df.label.unique()
# print(labels)

for label in labels:
    list_data = []
    test_df = df['query'][df['label']==label]

    for row_index,row in test_df.iteritems():
        list_data.append(row)
        # print(row)
    print(label)
    print(list_data)