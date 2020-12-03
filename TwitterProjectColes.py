#Nicolas Coles CS 118 Project Section 1
from tkinter import *
import matplotlib.pyplot as plt
import tweepy as tw #Module that handles twitter's api.
import sys


f=open('tweetList.txt','w',encoding='utf-8')

#OAuth keysk, used for acccessing the api
consumer_key= '#KEY'
consumer_secret='#KEY'
access_token='#KEY'
access_token_secret='#KEY'


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tw.API(auth,wait_on_rate_limit=True, 
    wait_on_rate_limit_notify=True)
#Asks the user for input on what word to search and what dates to search it for.
search_words = input("Enter a word to search in Twitter: ")
date_since = input("Enter begin search date (Year-Month-Day): ")
date_until = input("Enter end search date: ")
new_search = search_words + " -filter:retweets"
limit=input('Would you like to limit the number of tweets? (y/n): ') 

if limit.lower() == 'y': #Decides whether to limit the tweet lookup based on user input
    tweetLimit=int(input('What would you like the limit to be?: '))
    tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since,
              until=date_until).items(tweetLimit)
else:
    tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since,
              until=date_until).items()
hourly={}
xAxis=[]
yAxis=[]
count=0
for i in range(25):
    hourly[i]=i
    hourly[i]=0
for tweet in tweets:
    count+=1
    print("\n",tweet.text)
    f.write(str(tweet.text))
    f.write('\n'*3)
    x=tweet.created_at
    for num in hourly:
        if x.hour == num:
            hourly[num]+=1
        else:
            pass
for i in hourly:
    xAxis.append(i)
    yAxis.append(hourly[i])

f.close()


##########################################################################################

def lineGraph(): #Displays and saves line graph based on tweet data
    line.config(bg='gold',fg='blue')
    plt.ylabel('Number of Tweets')
    plt.xlabel('Hour')
    plt.title('Number of tweets per hour of the day')
    plt.plot(xAxis, yAxis)
    plt.savefig('linegraph.png')
    print("Graph 'linegraph.png' saved in current directory ")
    plt.show()

def pieChart(): #Displays and saves pie chart based on tweet data
    pie.config(bg='gold',fg='blue')
    plt.title('Number of tweets at every hour of the day')
    plt.pie(yAxis,labels=xAxis)
    print("Graph 'piechart.png' saved in current directory ")
    plt.savefig('piechart.png') 
    plt.show()
def barGraph():
    bar.config(bg='gold',fg='blue')
    plt.ylabel('Number of Tweets')
    plt.xlabel('Hour')
    plt.title('Number of tweets at each hour of the day')
    plt.bar(xAxis,yAxis)
    plt.savefig('bargraph.png')
    print("Graph 'bargraph.png' saved in current directory ")
    plt.show()




##########################################################################################
win=Tk() #This section impliments the Tkinter UI. Rudimentary but nice start.
win.title("Twitter Data Graphing")
win.geometry("800x700")
graphs=Label(win, text='Select a Graph Type',font=70,anchor=CENTER)

tweetCount=Label(win, text=f'Number of Tweets: {count}',font=70,anchor=CENTER)

line=Button(win, text='Line Graph',bg='blue',fg='gold',command=lineGraph,font=50)
pie=Button(win, text='Pie Graph',bg='blue',fg='gold' ,command=pieChart,font=50)
bar=Button(win, text='Bar Graph',bg='blue',fg='gold' ,command=barGraph,font=50)
graphs.pack(fill=X,padx=10)
line.pack(fill=X, padx=10)
pie.pack(fill=X, padx=10)
bar.pack(fill=X, padx=10)
tweetCount.pack(fill=X,padx=10)

mainloop()


