#Copyright (C) 2014, Simon Dooms

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from backbone import Backbone
from datetime import datetime
import re
import json
import glob
import os

def extractYouTubeIDFRomLink(url):
    #youtu.be/qFIUHACQ-gM?a
    pattern = 'youtu.be/(.*)\?a$' 
    p = re.compile(pattern,re.M | re.I)
    matches = p.findall(url)
    if len(matches) > 0:
        return matches[0]
    else:
        return -1

def extractDataFromTweet(tweet):
    user = ''
    item = ''
    timestamp = ''
    #user
    user = tweet['user']['id']
    #timestamp
    timestamp = tweet['created_at']
    the_time = datetime.strptime(timestamp.replace(' +0000',''), '%a %b %d %H:%M:%S %Y')
    timestamp = (the_time-datetime(1970,1,1)).total_seconds()
    timestamp = int(timestamp)
    #item
    url = tweet['entities']['urls'][0]['display_url']
    item = extractYouTubeIDFRomLink(url)
    return user, item, timestamp
    
def extractDataset(tweets):
    dataset = list()
    for tweet in tweets:
        try:
            user, item, timestamp = extractDataFromTweet(tweet)
            if user == -1 or item == -1 or timestamp == -1:
                continue
        except:
            continue
        dataset.append((user, item, timestamp))
    return dataset
    
def writeDataset(dataset, filename):
    lines = list()
    for (user,item,timestamp) in dataset:
        line = str(user) + '::'  + str(item) + '::' + str(timestamp) + '\n'
        lines.append(line)
    with file(filename, 'a') as outfile:
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

    datasetpath = 'datasets/YouTube'
    since_id = get_since_id(datasetpath)

    tweets, new_since_id =  b.searchTweets('I liked a @YouTube video', since_id)
    dataset = extractDataset(tweets)
    writeDataset(dataset, datasetpath + '/likes.dat')
    writeTweets(tweets,datasetpath + '/tweets_' + str(new_since_id) + '.json')