from trunklucator import WebUI

import pandas as pd

df = pd.read_csv('ytb_comments.csv')

title = "Sentiment"


data = df['text']        

controls = [
            {'label':'Positive (D)', 'value':1, 'shortcut':"['d']"}, 
            {'label':'Negative (K)', 'value':0, 'shortcut':"['k']"}, 
            {'label':'Skip (enter)', 'value':-1, 'shortcut':"['enter']"}, 
        ]

df['label'] = 2

l=[]

with WebUI(context={'buttons':controls, 'title':title}) as tru: # start http server in background
    for item in data:
        label = tru.ask({"html": item})

        l.append(label.y)

df['label'] = l

df.to_csv(r'ytb_comments.csv', index = False)