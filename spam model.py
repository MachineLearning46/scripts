# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:25:56 2019

@author: tshaik
"""
import pandas as pd
import sqlalchemy
from pandas.io import sql
import io
import sys
import pyodbc
import numpy as np
import re
    


# Import credentials from text file on the secured H: Drive. Reach out to Ludwid for the text file format
dictionary=dict(line.split(':', 1) for line in open('H:\ActiveDirectory.txt'))
# Remove line artifacts from the dictionary
dictionary=dict(map(str.strip,x) for x in dictionary.items()) 
# Declare Dictionary as variables
locals().update(dictionary)

#importing using excel
hamdata=pd.read_excel(r'C:\Users\tshaik\Documents\Data C\hamV1.xlsx')
#Not working using CSV
hamdata2=pd.read_csv(r'C:\Users\tshaik\Documents\Data C\hamV1.csv')

spamdata=pd.read_excel(r'C:\Users\tshaik\Documents\Data C\spamV1.xlsx')
#lowecase column
spamdata['tweet_body']=spamdata['tweet_body'].str.lower()
#lowercase dataframe and all into character
x_spamdata_v1=spamdata.apply(lambda x: x.astype(str).str.lower())
x_hamdata_v1=hamdata.apply(lambda x: x.astype(str).str.lower())
x_spamdata_v1.dtypes
#lowercase dataframe for strings only
spamdata_v1=spamdata.applymap(lambda x: x.lower() if type(x)==str else x)
hamdata_v1=hamdata.applymap(lambda x: x.lower() if type(x)==str else x)
#identify data type
spamdata_v1.dtypes

#def remove_tags(hamdata_v1):



import re

# This string contains HTML.
v = "My life,my choice/ كلام معلمين /fCES^^/18 years"

# Replace HTML tags with an empty string.
result = re.sub("<!--.*?-->", "", v)

print(result)


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

parse=MLStripper()
x=parse.feed("My life,my choice/ كلام معلمين /fCES^^/18 years")
x
TAG_RE = re.compile(r'/<[^>]+>/')
def remove_tags(x):
    return TAG_RE.sub('', x)
remove_tags(v)

conda install url_normalize
from url_normalize import url_normalize
from urllib.parse import urlparse
o = urlparse('http://www.cwi.nl:80/%7Eguido/Python.html')
vectorizer=TfidfVectorizer("english")

data=np.genfromtxt(r'C:\Users\tshaik\Documents\Data C\hamV1.txt',delimiter='\t')
print(data)
