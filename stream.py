#  -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.tweepy import Tweepy

app = Flask(__name__)
app.config.setdefault('TWEEPY_CONSUMER_KEY', 'ZoPmvcJJX14yKIbDsaeZqMPCh')
app.config.setdefault('TWEEPY_CONSUMER_SECRET', 'UYUdKS1OCVRKNVjGpxhsrbYiQYhnY869KxnQzwSqmEPKhQouvo')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_KEY', '1043745847781912577-aO3hhvkHl1cMQGaCmSYfJZ8zSizVkM')
app.config.setdefault('TWEEPY_ACCESS_TOKEN_SECRET', 'CjUCAYGlp8zR01hVofk1D1Da1sy7Ie3Ywqz7VPPE0ohHj')

tweepy = Tweepy(app)

@app.route('/tweets')
def show_tweets():
    tweets = tweepy.api.public_timeline()
    return render_template('tweets.html', tweets=tweets)

# @app.route('/say-something')
# def say_something():
#     status = tweepy.api.update_status('Hello, world!')
#     status_link = 'http://twitter.com/#!/YourUserName/status/%s' % status.id
#     return render_template('what_i_said.html', status_link=status_link)