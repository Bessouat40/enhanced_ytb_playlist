import numpy as np
import pandas as pd
import re

from joblib import dump, load

def analyse_sentiment(liste):

    
    classifier = load('ml/model_saved.joblib')
    vectorizer = load('ml/vectorizer_saved.joblib')
   
    df = pd.DataFrame(data=liste,columns=['text'])
  
    rm_n = lambda x: re.sub(r'\\n','',x)
    rm_html = lambda x: re.sub(r'(<.*>)','',x)
    rm_dble_slash = lambda x: re.sub(r'(\\)',' ',x)
    rm_timecode = lambda x: re.sub(r'(\d+:\d+)','',x)
    
    df['text'] = df['text'].apply(rm_n)
    df['text'] = df['text'].apply(rm_html)
    df['text'] = df['text'].apply(rm_dble_slash)
    df['text'] = df['text'].apply(rm_timecode)
    
    
    X = vectorizer.transform(df['text']).toarray()
    
    predict = pd.DataFrame(classifier.predict_proba(X),columns=['neg','pos'])
   
    seuil = 0.85
    choose = lambda val: 0 if val<seuil else 1 
    predict['class'] = predict['pos'].apply(choose)
    df['class'] = predict['class']
    
    moy = df['class'].sum()/df.shape[0]

    return moy
