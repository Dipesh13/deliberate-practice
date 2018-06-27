import pandas as pd
import json
import requests

column = ['data','label']
df = pd.read_csv('/home/dipesh/deliberate-practice/test.csv',names=column)

labels = df.label.unique()

for label in labels:
    list_data = []
    dict_data = {"sents":[]}
    test_df = df['data'][df['label']==label]
    for row_index,row in test_df.iteritems():
        list_data.append(row)
        dict_data["sents"].append(row)
    # print(label)

    res = requests.post('http://0.0.0.0:8000/predict',data=json.dumps(dict_data))
    # print(res.json())
    preds_dict = res.json()
    preds = preds_dict['prediction']

    # for query,pred in zip(list_data,preds):
    #     print(query,pred)
    df_out = pd.DataFrame({'query':list_data,
                       'predictions':preds})
    df_out.to_csv(label+'.csv',index=False)
