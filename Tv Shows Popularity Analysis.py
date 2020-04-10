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
def SentimentAnalysis(Data):
    positive = 0
    wpositive = 0
    spositive = 0
    negative = 0
    wnegative = 0
    snegative = 0
    neutral = 0
    for i in range(0,50):
        analysis = TextBlob(Data[i])
        if (analysis.sentiment.polarity >=-0.03 and analysis.sentiment.polarity <= 0.03):  
            neutral += 1
        elif (analysis.sentiment.polarity > 0.03 and analysis.sentiment.polarity <= 0.3):
            wpositive += 1
        elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.55):
            positive += 1
        elif (analysis.sentiment.polarity > 0.55 and analysis.sentiment.polarity <= 1):
            spositive += 1
        elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= -0.03):
            wnegative += 1
        elif (analysis.sentiment.polarity > -0.55 and analysis.sentiment.polarity <= -0.3):
            negative += 1
        elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.55):
            snegative += 1
    return wpositive,positive,spositive,neutral,wnegative,negative,snegative
        
def TrpChart(trp,show_name):
    fig= plt.figure(figsize=(10,6))
    left = [1, 2, 3, 4, 5] 
    plt.ylim(0,5)
    plt.bar(left, trp, tick_label = show_name,width = 0.2, color = ['red', 'green'],zorder=2) 
    plt.xlabel('Show Name') 
    plt.ylabel('TRP') 
    plt.title('TRP Comparison Show Wise')
    plt.grid(axis="y")
    plt.show()

def Trp():
    Trp,Show_Name=ReadCsvFile('Trpchart.csv')
    top=Toplevel()
    top.title("TRP")
    top.geometry("300x150+1150+0")
    top.configure(bg='floral white')
    photo = PhotoImage(file = "TRP.png")
    top.iconphoto(False, photo)
    label=Label(top,text='Show Name',bg='floral white',font=Font(family="Times New Roman",size=15))
    label.grid(row=0,column=0)
    label0=Label(top,text='TRP',bg='floral white',font=Font(family="Times New Roman",size=15))
    label0.grid(row=0,column=8)
    label1=Label(top,text=Show_Name[0],bg='floral white',font=Font(family="Times New Roman",size=11))
    label1.grid(row=3,column=0)
    label2=Label(top,text=Show_Name[1],bg='floral white',font=Font(family="Times New Roman",size=11))
    label2.grid(row=6,column=0)
    label3=Label(top,text=Show_Name[2],bg='floral white',font=Font(family="Times New Roman",size=11))
    label3.grid(row=9,column=0)
    label4=Label(top,text=Show_Name[3],bg='floral white',font=Font(family="Times New Roman",size=11))
    label4.grid(row=12,column=0)
    label5=Label(top,text=Show_Name[4],bg='floral white',font=Font(family="Times New Roman",size=11))
    label5.grid(row=15,column=0)
    label6=Label(top,text=Trp[0],bg='floral white',font=Font(family="Times New Roman",size=11))
    label6.grid(row=3,column=8)
    label7=Label(top,text=Trp[1],bg='floral white',font=Font(family="Times New Roman",size=11))
    label7.grid(row=6,column=8)
    label8=Label(top,text=Trp[2],bg='floral white',font=Font(family="Times New Roman",size=11))
    label8.grid(row=9,column=8)
    label9=Label(top,text=Trp[3],bg='floral white',font=Font(family="Times New Roman",size=11))
    label9.grid(row=12,column=8)
    label10=Label(top,text=Trp[4],bg='floral white',font=Font(family="Times New Roman",size=11))
    label10.grid(row=15,column=8)
    Trp=list(map(float,Trp))
    TrpChart(Trp,Show_Name)

def BiggBoss13Analysis():
    BiggBoss13=[]
    BiggBoss13=ReadFile('BiggBoss13.txt')
    BiggBoss13_wpositive,BiggBoss13_positive,BiggBoss13_spositive,BiggBoss13_neutral,BiggBoss13_wnegative,BiggBoss13_negative,BiggBoss13_snegative = SentimentAnalysis(BiggBoss13)
    BiggBoss13_value=[BiggBoss13_wpositive*2,BiggBoss13_positive*2,BiggBoss13_spositive*2,BiggBoss13_neutral*2,BiggBoss13_wnegative*2,BiggBoss13_negative*2,BiggBoss13_snegative*2]
    PlotPieChart(BiggBoss13_value,'Bigg Boss 13')

def RoadiesAnalysis():
    Roadies=[]
    Roadies=ReadFile('Roadies.txt')
    Roadies_wpositive,Roadies_positive,Roadies_spositive,Roadies_neutral,Roadies_wnegative,Roadies_negative,Roadies_snegative = SentimentAnalysis(Roadies)
    Roadies_value=[Roadies_wpositive*2,Roadies_positive*2,Roadies_spositive*2,Roadies_neutral*2,Roadies_wnegative*2,Roadies_negative*2,Roadies_snegative*2]
    PlotPieChart(Roadies_value,'Roadies')

def TheKapilSharmaShowAnalysis():
    TheKapilSharmaShow=[]
    TheKapilSharmaShow=ReadFile('TheKapilSharmaShow.txt')
    TheKapilSharmaShow_wpositive,TheKapilSharmaShow_positive,TheKapilSharmaShow_spositive,TheKapilSharmaShow_neutral,TheKapilSharmaShow_wnegative,TheKapilSharmaShow_negative,TheKapilSharmaShow_snegative = SentimentAnalysis(TheKapilSharmaShow)
    TheKapilSharmaShow_value=[TheKapilSharmaShow_wpositive*2,TheKapilSharmaShow_positive*2,TheKapilSharmaShow_spositive*2,TheKapilSharmaShow_neutral*2,TheKapilSharmaShow_wnegative*2,TheKapilSharmaShow_negative*2,TheKapilSharmaShow_snegative*2]
    PlotPieChart(TheKapilSharmaShow_value,'The Kapil Sharma Show')

def SplitsvillaAnalysis():
    Splitsvilla=[]
    Splitsvilla=ReadFile('Splitsvilla.txt')
    Splitsvilla_wpositive,Splitsvilla_positive,Splitsvilla_spositive,Splitsvilla_neutral,Splitsvilla_wnegative,Splitsvilla_negative,Splitsvilla_snegative = SentimentAnalysis(Splitsvilla)
    Splitsvilla_value=[Splitsvilla_wpositive*2,Splitsvilla_positive*2,Splitsvilla_spositive*2,Splitsvilla_neutral*2,Splitsvilla_wnegative*2,Splitsvilla_negative*2,Splitsvilla_snegative*2]
    PlotPieChart(Splitsvilla_value,'Splitsvilla')

def ComparisonBetweenShows():
    BiggBoss13=[]
    BiggBoss13=ReadFile('BiggBoss13.txt')
    BiggBoss13_wpositive,BiggBoss13_positive,BiggBoss13_spositive,BiggBoss13_neutral,BiggBoss13_wnegative,BiggBoss13_negative,BiggBoss13_snegative = SentimentAnalysis(BiggBoss13)
    BiggBoss13Positive=(BiggBoss13_wpositive+BiggBoss13_positive+BiggBoss13_spositive)*2
    BiggBoss13Negative=(BiggBoss13_wnegative+BiggBoss13_negative+BiggBoss13_snegative)*2
    BiggBoss13Neutral=BiggBoss13_neutral
    
    Roadies=[]
    Roadies=ReadFile('Roadies.txt')
    Roadies_wpositive,Roadies_positive,Roadies_spositive,Roadies_neutral,Roadies_wnegative,Roadies_negative,Roadies_snegative = SentimentAnalysis(Roadies)
    RoadiesPositive=(Roadies_wpositive+Roadies_positive+Roadies_spositive)*2
    RoadiesNegative=(Roadies_wnegative+Roadies_negative+Roadies_snegative)*2
    RoadiesNeutral=Roadies_neutral

    TheKapilSharmaShow=[]
    TheKapilSharmaShow=ReadFile('TheKapilSharmaShow.txt')
    TheKapilSharmaShow_wpositive,TheKapilSharmaShow_positive,TheKapilSharmaShow_spositive,TheKapilSharmaShow_neutral,TheKapilSharmaShow_wnegative,TheKapilSharmaShow_negative,TheKapilSharmaShow_snegative = SentimentAnalysis(TheKapilSharmaShow)
    TheKapilSharmaShowPositive=(TheKapilSharmaShow_wpositive+TheKapilSharmaShow_positive+TheKapilSharmaShow_spositive)*2
    TheKapilSharmaShowNegative=(TheKapilSharmaShow_wnegative+TheKapilSharmaShow_negative+TheKapilSharmaShow_snegative)*2
    TheKapilSharmaShowNeutral=TheKapilSharmaShow_neutral
    
    Splitsvilla=[]
    Splitsvilla=ReadFile('Splitsvilla.txt')
    Splitsvilla_wpositive,Splitsvilla_positive,Splitsvilla_spositive,Splitsvilla_neutral,Splitsvilla_wnegative,Splitsvilla_negative,Splitsvilla_snegative = SentimentAnalysis(Splitsvilla)
    SplitsvillaPositive=(Splitsvilla_wpositive+Splitsvilla_positive+Splitsvilla_spositive)*2
    SplitsvillaNegative=(Splitsvilla_wnegative+Splitsvilla_negative+Splitsvilla_snegative)*2
    SplitsvillaNeutral=Splitsvilla_neutral
    
    labels=['BiggBoss13','Roadies','The Kapil Sharma Show','Splitsvilla']
    positive=[BiggBoss13Positive, RoadiesPositive, TheKapilSharmaShowPositive, SplitsvillaPositive]
    negative=[BiggBoss13Negative, RoadiesNegative, TheKapilSharmaShowNegative, SplitsvillaNegative]
    neutral=[BiggBoss13Neutral, RoadiesNeutral, TheKapilSharmaShowNeutral, SplitsvillaNeutral]
    x = np.arange(4)
    bar_width=0.15
    plt.bar(x,positive,width=bar_width,color='green',zorder=2)
    plt.bar(x+bar_width,negative,width=bar_width,color='red',zorder=2)
    plt.bar(x+bar_width*2,neutral,width=bar_width,color='blue',zorder=2)
    plt.xticks(x+bar_width,labels)
    plt.xlabel('Shows')
    plt.ylabel('Percentage')
    green_patch= mpatches.Patch(color='green',label='Positive Views')
    red_patch= mpatches.Patch(color='red',label='Negative Views')
    blue_patch= mpatches.Patch(color='blue',label='Neutral Views')
    plt.legend(handles=[green_patch, red_patch, blue_patch])
    plt.grid(axis="y")
    plt.show()
    
    
    root = Tk()
root.geometry("1920x1080+0+0")
photo = PhotoImage(file = "analysis.png")
root.iconphoto(False, photo)
root.title('TV SHOW POPULARITY ANALYSIS')

buttontrpchart=PhotoImage(file='button_trp-chart.png')
buttonbiggbossanalysis = PhotoImage(file = "button_biggboss-analysis.png")
buttonroadiesanalysis = PhotoImage(file = "button_roadies-analysis.png")
buttonthekapilsharmashowanalysis = PhotoImage(file = "button_the-kapil-sharmashow-analysis.png")
buttonsplitsvillaanalysis = PhotoImage(file = "button_splitsvilla-analysis.png")
buttoncompareshowsaccordingtoview = PhotoImage(file = "button_compare-shows-according-to-view.png")
buttontweetsextractor = PhotoImage(file ='button_tweets-extractor.png')

logo=PhotoImage(file='logo.png')
Logo=Label(root,image=logo)
Logo.place(x=650,y=10)
button1=Button(root,image=buttontrpchart,command=Trp,border=0)
button1.place(x=10,y=220)
button2=Button(root,image=buttonbiggbossanalysis,command=BiggBoss13Analysis,border=0)
button2.place(x=10,y=300)
button3=Button(root,image=buttonroadiesanalysis,command=RoadiesAnalysis,border=0)
button3.place(x=10,y=380)
button4=Button(root,image=buttonthekapilsharmashowanalysis,command=TheKapilSharmaShowAnalysis,border=0)
button4.place(x=10,y=460)
button5=Button(root,image=buttonsplitsvillaanalysis,command=SplitsvillaAnalysis,border=0)
button5.place(x=10,y=540)
button6=Button(root,image=buttoncompareshowsaccordingtoview,command=ComparisonBetweenShows,border=0)
button6.place(x=10,y=620)
button7=Button(root,image=buttontweetsextractor,command=webscraping,border=0)
button7.place(x=10,y=700)

photo1 = PhotoImage(file = "image.png")
LabelPhoto=Label(root,image=photo1)
LabelPhoto.place(x='1000',y='200')

root.mainloop()
