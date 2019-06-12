from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_cors import CORS
# from TwitterAPI import TwitterAPI
import tweepy #https://github.com/tweepy/tweepy
import json
import re
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
#  -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)
api = Api(app)
cors = CORS(app)

# Twitter API credentials

consumer_key = "ZoPmvcJJX14yKIbDsaeZqMPCh"
consumer_secret = "UYUdKS1OCVRKNVjGpxhsrbYiQYhnY869KxnQzwSqmEPKhQouvo"
access_key = "1043745847781912577-aO3hhvkHl1cMQGaCmSYfJZ8zSizVkM"
access_secret = "CjUCAYGlp8zR01hVofk1D1Da1sy7Ie3Ywqz7VPPE0ohHj"

# consumer_key = "qJmIQDMX5INqRcbllTP7bCfIq"
# consumer_secret = "xqxtURKhdb1vk8dIbJUPKHZVvvs14yJ9GvlL9G7oHMTuRYdeFT"
# access_key = "1043745847781912577-kH9YKHaGarhILLE56D0b6DiWyYuMaH"
# access_secret = "iotvF4GFaI0TKJIE3dI4Ml3IQ4Ykzk2bKwWSq7JEd2AHz"


# class Employees(Resource):
#    def get(self):
#        # conn = db_connect.connect() # connect to database
#        # query = conn.execute("select * from employees") # This line performs query and returns json result
#        # return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
#        return "q Employeee"
# from http.server import HTTPServer, SimpleHTTPRequestHandler, test
# import sys

# class CORSRequestHandler (SimpleHTTPRequestHandler):
#     def end_headers (self):
#         self.send_header('Access-Control-Allow-Origin', '*')
#         SimpleHTTPRequestHandler.end_headers(self)


def application(environ, start_response):
        if environ['REQUEST_METHOD'] == 'OPTIONS':
            start_response(
            '200 OK',
            [
                ('Content-Type', 'application/json'),
                ('Access-Control-Allow-Origin', '*'),
                ('Access-Control-Allow-Headers', 'Authorization, Content-Type'),
                ('Access-Control-Allow-Methods', 'POST'),
            ]
            )
        return ''

class SearchProducts(Resource):
    def get(self, SearchProducts_id):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
       
        #Put your search term
        searchquery = SearchProducts_id and 'ราคา'

        # users = tweepy.Cursor(api.search,q=searchquery).items()
        users = tweepy.Cursor(api.search,
                           q=searchquery,
                           rpp=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items()
        count = 0
        errorCount=0
        items =[]
        r = []
        
        while count < 10:
            try:
                user = next(users)
                r.append(user._json)
                datetime = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
                detail = {
                    "line_id": "test",
                    "price": 200,
                    "shop_name": "shop2",
                    "shop_link": "https://twitter.com/tw_shopp",
                    "description": r[count]['text'],
                    "photo": "http://www.personalbrandingblog.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
                    "save": "false",
                    "created_at": datetime,
                    "favorite_count": r[count]['favorite_count'],
                    "priority_score": 9,
                    "retweet_count": r[count]['retweet_count'],
                    "cnt" : count
                }
                items.append(detail)
                count += 1
                

                # items.append(user._json)
                # bi=str(type(user))
                #use count-break during dev to avoid twitter restrictions
                #if (count>10):
                #    break
            except tweepy.TweepError:
                #catches TweepError when rate limiting occurs, sleeps, then restarts.
                #nominally 15 minnutes, make a bit longer to avoid attention.
                print("sleeping....")
                time.sleep(60*16)
                user = next(users)
            except StopIteration:
                break
            try:
                print("Writing to JSON tweet number:"+str(count))
                # json.dump(user._json,file,sort_keys = True,indent = 4)
                
            except UnicodeEncodeError:
                errorCount += 1
                print("UnicodeEncodeError,errorCount ="+str(errorCount))
        
        
            # print ("...%s tweets downloaded so far" % (len(alltweets)))
            # str = json.dumps(dict)
    
        return(items) 
        # return(r) 


class Shop(Resource):
   def get(self,shop_name):
       #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        #initialize a list to hold all the tweepy Tweets
        alltweets = []    
        
        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = shop_name,count=100)
    
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = shop_name,count=100,max_id=oldest)
            
            #save most recent tweets
            alltweets.extend(new_tweets)
            
            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1
            
            outtweets = [] #initialize master list to hold our ready tweets
           
            items =[];
            for tweet in alltweets:
                    #not all tweets will have media url, so lets skip them
                    try:
                        datetime = tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
                        caption = tweet.text
                        print (type(tweet))
                        checkRT = ''+caption[0]+caption[1];
                        # print(checkRT)
                        if(checkRT not in 'RT'):
                            detail = {
                                "line_id": "test",
                                "price": 200,
                                "shop_name": "shop2",
                                "shop_link": "",
                                "description": caption,
                                "photo": tweet.entities['media'][0]['media_url'],
                                "save": "false",
                                "created_at": datetime,
                                "favorite_count": tweet.favorite_count,
                                "priority_score": 9,
                                "retweet_count": tweet.retweet_count
                            }
                        items.append(detail)

                    except (NameError, KeyError):
                            #we dont want to have any entries without the media_url so lets do nothing
                            pass
                    else:
                            #got media_url - means add it to the output
                            outtweets.append([tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.entities['media'][0]['media_url']])   
           
            # print ("...%s tweets downloaded so far" % (len(alltweets)))
            # str = json.dumps(dict)
            return(items)

class SearchBy(Resource):
   def get(self, SearchBy_keyword):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        searchquery = SearchBy_keyword+" บาท" 

        # tweets = tweepy.Cursor(api.search, q=searchquery, count=10, include_entities=True)
        tweets =  tweepy.Cursor(api.search, q=searchquery+ ' -RT', lang="th", include_entities=True).items(100)
        items=[]
    
        for status in tweets:
            try:
                datetime = status.created_at.strftime("%Y-%m-%d %H:%M:%S")
                detail = {
                            "item_id" : status.id,
                            "line_id": "",
                            "price": 200,
                            "shop_name": status.user.screen_name,
                            "shop_link": "",
                            "description": status.text,
                            "photo": status.extended_entities['media'][0]['media_url'],
                            "save": "false",
                            "created_at": datetime,
                            "favorite_count": status.favorite_count,
                            "priority_score": 9,
                            "retweet_count": status.retweet_count
                        }
                
                items.append(detail)
            except AttributeError:
                pass 
        return (items)

class Trending(Resource):
   def get(self, trending_keyword):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        searchquery = trending_keyword+" ราคา" 

        # tweets = tweepy.Cursor(api.search, q=searchquery, count=10, include_entities=True)
        tweets =  tweepy.Cursor(api.search, q=searchquery+ ' -RT', lang="th", include_entities=True).items(100)
        items=[]
        price = 0
        for status in tweets:
            try:
                datetime = status.created_at.strftime("%Y-%m-%d %H:%M:%S")
                price = status.text
                detail = {
                            "item_id" : status.id,
                            "line_id": "",
                            "price": 100,
                            "shop_name": status.user.screen_name,
                            "shop_link": "",
                            "description": status.text,
                            "photo": status.extended_entities['media'][0]['media_url'],
                            "save": "false",
                            "created_at": datetime,
                            "favorite_count": status.favorite_count,
                            "priority_score": 9,
                            "retweet_count": status.retweet_count
                        }
                
                items.append(detail)
            except AttributeError:
                pass 
        return (items)

# class StreamNewProducts(StreamListener):
#    def get(self):
#         auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#         auth.set_access_token(access_key, access_secret)
#         api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        
#         stream = tweepy.Stream(api.auth, StreamNewProducts())
#         filtro = ['เสื้อ', 'กางเกง', 'ราคา']
#         stream.filter(track=filtro)
#         items = []
#         try:
#             datetime = stream.created_at.strftime("%Y-%m-%d %H:%M:%S")
#             detail = {
#                         "item_id" : stream.id,
#                         "line_id": "",
#                         "price": 100,
#                         "shop_name": stream.user.screen_name,
#                         "shop_link": "",
#                         "description": stream.text,
#                         "photo": stream.extended_entities['media'][0]['media_url'],
#                         "save": "false",
#                         "created_at": datetime,
#                         "favorite_count": stream.favorite_count,
#                         "priority_score": 9,
#                         "retweet_count": stream.retweet_count
#                     }
            
#             items.append(detail)
#         except AttributeError:
#             pass 
#         return (items)


api.add_resource(SearchProducts, '/product/<SearchProducts_id>')
# api.add_resource(StreamNewProducts, '/new')
api.add_resource(Shop, '/shop/<shop_name>')  # Route_2
api.add_resource(SearchBy, '/searchby/<SearchBy_keyword>')  # Route_3
api.add_resource(Trending, '/trending/<trending_keyword>')  # Route_3


if __name__ == '__main__':
    # get("@jassada53510747")
    app.run(port='5002')
    # test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
    # app.run(port='5002')


    