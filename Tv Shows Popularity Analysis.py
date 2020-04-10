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
        
def PlotPieChart(values,Title):
    fig= plt.figure(figsize=(12,6))
    labels='Weakly Positive','Positive','Strongly Positive','Neutral','Weakly Negative','Negative','Strongly Negative'
    color=['tab:blue','tab:orange','tab:purple','tab:cyan','tab:pink','aquamarine','rosybrown']
    plt.pie(values,labels=labels,colors=color,autopct='%1.2f%%')
    plt.axis('equal')
    plt.title(Title)
    plt.legend()
    plt.show()

def ReadFile(FileName):
    list_comments=[]
    with open(FileName,'r') as f:
        for line in f.read().split('\n'):
            list_comments.append(line)
        f.close()
    return list_comments

def ReadCsvFile(FileName):
    Line=[]
    show_name=[]
    trp=[]
    with open('Trpchart.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            Line.append(line)
        for i in range(1,6):
            show_name.append(Line[i][1])
            trp.append(Line[i][2])
    return trp,show_name
        
