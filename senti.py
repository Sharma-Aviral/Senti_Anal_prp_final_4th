from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
from dotenv import load_dotenv
import tweepy
import os
tweeterUser = "INCIndia"
number_oF_tweets = 1000000
count_Nice = 0
count_Neg = 0
count_Neutral = 0

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
        count_Nice = +1
    elif testimonial.sentiment.polarity < 0:
        print("Negative Sentiment") 
        count_Neg = +1
    else:
        print("Neutral Sentiment")
        count_Neutral = +1

def count_Senti():
    if count_Nice >= count_Neg:
        print("Overall Nice")
    elif count_Neg >= count_Nice:
        print("BAd bad") 
    elif count_Neutral >= count_Neg or count_Neutral >= count_Nice:
        print("Neutral")        
    else:
        print("GG undetermuibg")
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
count_Senti()     