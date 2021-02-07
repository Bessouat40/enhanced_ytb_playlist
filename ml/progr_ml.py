import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
import re

from joblib import dump, load

reg = load('regression_model_saved.joblib')

def analyse_sentiment(liste):
    liste = df['text']
    liste = liste.replace('\n','',regex=True)
    rm_html = lambda x: re.sub(r'(<.*>)','',x)
    rm_dble_slash = lambda x: re.sub(r'(\\)',' ',x)
    rm_timecode = lambda x: re.sub(r'(\d+:\d+)','',x)

    liste = liste.apply(rm_html)
    liste = liste.apply(rm_dble_slash)
    liste = liste.apply(rm_timecode)
    vectorizer = CountVectorizer(min_df=0, lowercase=False,stop_words='english')
    vectorizer.fit(liste)
    X = vectorizer.transform(liste).toarray()
    res = reg.predict(X)
    moy = res.sum()/res.shape[0]

    return moy
