from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
from dotenv import load_dotenv
import tweepy
import os
import matplotlib.pyplot as plt
import numpy as np

global count_Neg
count_Neg = 0
global count_Pos
count_Pos = 0
global count_Neut
count_Neut = 0

#info_initilisation
tweeterUser = "kunalkamra88"
number_oF_tweets = 100000

#getting access tokkens and api key form .env
project_folder = os.path.expanduser('~/Desktop/projects/python/senti')  
load_dotenv(os.path.join(project_folder, '.env') )
api_key =  os.getenv("api_key")
api_seceret = os.getenv("api_seceret")
access_key = os.getenv("access_key")
access_tokken = os.getenv("access_tokken")

#twitter api authentication 
auth = tweepy.OAuthHandler(api_key,api_seceret)
auth.set_access_token(access_key, access_tokken)
api = tweepy.API(auth)
try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')


#textblob senti analysis check
def sentimenti(sent):
    testimonial = TextBlob(sent)
    if testimonial.sentiment.polarity > 0 :
        print("Nice Words")
        global count_Pos
        count_Pos = count_Pos +1
    elif testimonial.sentiment.polarity < 0:
        print("Negative Sentiment") 
        global count_Neg
        count_Neg = count_Neg +1

    else:
        print("Neutral Sentiment")
        global count_Neut 
        count_Neut = count_Neut +1

        
user = api.get_user(tweeterUser)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)    


tweets = api.user_timeline(tweeterUser)
for info in tweets[:number_oF_tweets-1]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.text)
     sentimenti(info.text)
     print("\n")

y = np.array([count_Pos,count_Neg,count_Neut])
mylabels = ["Positive", "Negative", "Neutral"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show() 
