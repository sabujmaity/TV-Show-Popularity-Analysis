from bs4 import BeautifulSoup
import requests
from tkinter import *
from tkinter.font import Font
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import csv
def webscraping():
    handle = input('Input your account name on Twitter: ')
    ctr = int(input('Input number of tweets to scrape: '))
    res=requests.get('https://twitter.com/'+handle)
    bs=BeautifulSoup(res.content,'lxml')
    all_tweets = bs.find_all('div',{'class':'tweet'})
    if all_tweets:
      for tweet in all_tweets[:ctr]:
        context = tweet.find('div',{'class':'context'}).text.replace("\n"," ").strip()
        content = tweet.find('div',{'class':'content'})
        header = content.find('div',{'class':'stream-item-header'})
        user = header.find('a',{'class':'account-group js-account-group js-action-profile js-user-profile-link js-nav'}).text.replace("\n"," ").strip()
        time = header.find('a',{'class':'tweet-timestamp js-permalink js-nav js-tooltip'}).find('span').text.replace("\n"," ").strip()
        message = content.find('div',{'class':'js-tweet-text-container'}).text.replace("\n"," ").strip()
        footer = content.find('div',{'class':'stream-item-footer'})
        stat = footer.find('div',{'class':'ProfileTweet-actionCountList u-hiddenVisually'}).text.replace("\n"," ").strip()
        if context:
          print(context)
        print(user,time)
        print(message)
        print(stat)
        print()
    else:
        print("List is empty/account name not found.")
        
        from importlib import reload
import sys
from imp import reload
import warnings
warnings.filterwarnings('ignore')
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding("utf-8")
import pandas as pd

df1 = pd.read_csv('labeledTrainData.tsv', delimiter="\t")
df1 = df1.drop(['id'], axis=1)
df1.head()
df2 = pd.read_csv('imdb_master.csv',encoding="latin-1")
df2.head()
df2 = df2.drop(['Unnamed: 0','type','file'],axis=1)
df2.columns = ["review","sentiment"]
df2.head()
df2 = df2[df2.sentiment != 'unsup']
df2['sentiment'] = df2['sentiment'].map({'pos': 1, 'neg': 0})
df2.head()
df = pd.concat([df1, df2]).reset_index(drop=True)
df.head()
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english")) 
lemmatizer = WordNetLemmatizer()


def clean_text(text):
    text = re.sub(r'[^\w\s]','',text, re.UNICODE)
    text = text.lower()
    text = [lemmatizer.lemmatize(token) for token in text.split(" ")]
    text = [lemmatizer.lemmatize(token, "v") for token in text]
    text = [word for word in text if not word in stop_words]
    text = " ".join(text)
    return text

df['Processed_Reviews'] = df.review.apply(lambda x: clean_text(x))
