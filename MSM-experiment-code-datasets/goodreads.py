#Copyright (C) 2014, Simon Dooms

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from backbone import Backbone
from datetime import datetime
import re
import json
import glob
import urllib
import os
from multiprocessing import Pool

def scrape_goodreads_data(url):
    #scrape the url
    try:
        search = urllib.urlopen(url)
    except:
        return -1, -1, -1
    html = search.read()
    search.close()
    #check if goodreads page
    pattern = '<meta property="og:site_name" content="Goodreads"/>'
    p = re.compile(pattern,re.M | re.I)
    matches = p.search(html)
    if matches == None:
        return -1, -1, -1
    #extract goodreads user
    pattern = '<span class="reviewer"><a href="/user/show/(.+?)" class="userReview" itemprop="author">'
    p = re.compile(pattern,re.M | re.I | re.S)
    matches = p.findall(html)
    if len(matches) == 0:
        return -1, -1, -1
    goodreads_user = matches[0]
    #extract item id and title
    pattern = '<a href="/book/show/(.+?)" class="bookTitle" itemprop="url">' 
    m = re.search(pattern,html)
    if m == None:
        return -1, -1, -1
    item = m.group(1)
    pattern = '<a href="/book/show/'+str(item)+'" class="bookTitle" itemprop="url">(.+?)</a>'
    m = re.search(pattern, html)
    if m == None:
        return -1, -1, -1
    title = m.group(1)
    return goodreads_user, item, title

def extractRatingFromTweet(tweet):
    rating = -1
    text = tweet['text']
    pattern = '([1-5]) of 5 stars'
    m = re.search(pattern, text)
    if m == None:
        return -1, -1, -1
    rating = m.group(1)
    return rating

def extractDataFromTweet(tweet):
    try:
        user = -1
        item = -1
        rating = -1
        timestamp = -1
        goodreads_user = -1
        title = -1
        #user
        user = tweet['user']['id']
        #timestamp
        timestamp = tweet['created_at']
        the_time = datetime.strptime(timestamp.replace(' +0000',''), '%a %b %d %H:%M:%S %Y')
        timestamp = (the_time-datetime(1970,1,1)).total_seconds()
        timestamp = int(timestamp)
        #rating
        rating = extractRatingFromTweet(tweet)
        #item, goodreads_user, title
        try:
            url = tweet['entities']['urls'][0]['url']
        except:
            #there are no URLs? 
            print 'No URLs found, skipping this tweet...' 
            return user, item, timestamp, goodreads_user, title, rating
        goodreads_user, item, title = scrape_goodreads_data(url)        
        return user, item, timestamp, goodreads_user, title, rating
    except:
        return -1,-1,-1,-1,-1,-1
    
def extractDataset(tweets):
    ratings = dict() #twitteruserid => item (isbn) => (rating, timestamp)
    items = dict() #isbn => title
    users = dict() #twitteruserid => goodreads_userid
    
    #in Parallel!
    p = Pool(50)
    results = p.map(extractDataFromTweet, tweets)
    
    for (user, item, timestamp, goodreads_user, title, rating) in results:
        if user == -1 or item == -1 or timestamp == -1 or rating == -1 or goodreads_user == -1 or title == -1:
            continue
        try:
            ratings[user][item] = (rating, timestamp)
        except:
            ratings[user] = {item : (rating, timestamp)}
        items[item] = title
        users[user] = goodreads_user
    return ratings, items, users
    
def writeDataset(ratings, items, users, path):
    lines = list()
    for user in ratings:
        for item in ratings[user]:
            tup = ratings[user][item]
            rating = tup[0]
            timestamp = tup[1]
            line = str(user) + '::' + str(users[user]) + '::' + str(item) + '::' + str(items[item]) + '::' + str(rating) + '::'  + str(timestamp) + '\n'
            lines.append(line)
    with file(path + '/ratings.dat', 'a') as outfile:
        outfile.writelines(lines)

    
def writeTweets(tweets, filename):
    line = json.dumps(tweets, ensure_ascii = False).encode('UTF-8')
    with file(filename, 'w') as outfile:
        outfile.writelines(line)
        
def get_since_id(path):
    since_id  = 0
    for infile in glob.glob( os.path.join(path, 'tweets_*.json') ):
        pattern = 'tweets_([0-9]*).json'
        p = re.compile(pattern,re.M | re.I)
        matches = p.findall(infile)
        id = int(matches[0])
        #keep maximum id
        since_id = max(id, since_id)
    return since_id

if __name__ == "__main__":    
    b = Backbone()

    datasetpath = 'datasets/Goodreads'
    since_id = get_since_id(datasetpath)

    tweets, new_since_id =  b.searchTweets('of 5 stars to', since_id)
    ratings, items, users = extractDataset(tweets)
    writeDataset(ratings, items, users, datasetpath)
    writeTweets(tweets,datasetpath + '/tweets_' + str(new_since_id) + '.json')