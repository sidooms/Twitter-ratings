#Copyright (C) 2014, Simon Dooms

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from twitter import *
import sys

class Backbone:
    t = None

    def __init__(self):
        #Twitter API v1.1 needs oAuth   
        token = 'xxx'
        token_secret = 'xxx'
        con_key = 'xxx'
        con_secret = 'xxx'
        try:        
            self.t = Twitter(auth=OAuth(token, token_secret, con_key, con_secret)) 
        except:
            print 'Error connecting to twitter' 
            sys.exit()
        
    def searchTweets(self, query, since):
        tweets = list()
        the_max_id = None #start with empty max
        the_max_id_oneoff = None
        new_since_id = since   
        
        number_of_iterations = 0
        while (number_of_iterations <= 50):
            number_of_iterations += 1
            count = 100 #maximum number of tweets allowed in one result set
            try:
                if the_max_id != None:
                    the_max_id_oneoff = the_max_id -1
                    res = self.t.search.tweets(q=query, result_type='recent', count=count,since_id=since,max_id=the_max_id_oneoff)
                else:
                    res = self.t.search.tweets(q=query, result_type='recent', count=count,since_id=since)
            except:
                print 'Error searching for tweets'
                return tweets, new_since_id
            
            try:
                #Extract the tweets from the results
                num_results = len(res['statuses'])
                print '  Found ' + str(num_results) + ' tweets.'
                for d in res['statuses']:    
                    tweets.append(d)
                    tweetid = d['id']
                    if the_max_id == None or the_max_id > tweetid:
                        the_max_id = tweetid
    
                    if new_since_id < tweetid:
                        new_since_id = tweetid
                    
                #end the while loop if no more tweets were found
                if len(res['statuses']) == 0:
                    break
                #break #for debug (quits after 1 iteration of count tweets)
            except ValueError:
                print 'Error ', sys.exc_info()[0]
                traceback.print_exc(file=sys.stdout)
                return tweets, new_since_id
        return tweets, new_since_id
