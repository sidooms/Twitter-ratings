Twitter-Ratings and Score In Social site
===============

A collection of Python scripts to download and extract rating datasets from Twitter as described in an article accepted for publication in the [MSM 2014 workshop](http://www.kde.cs.uni-kassel.de/ws/msm2014/) co-located with the [WWW 2014 conference](http://www2014.kr). Please cite the corresponding paper if you make use of this work. The presented slides can be found on [slideshare](http://www.slideshare.net/simondooms/static-mining-cross-domain-rating-datasets-from-structured-data-on-twitter).

    @conference{Dooms14msm,
    author = {Dooms, Simon and De Pessemier, Toon and Martens, Luc},
    title = {Cross-Domain Rating Datasets from Structured Data on Twitter},
    booktitle = {Workshop on Modeling Social Media: Mining Big Data in Social Media and the Web (MSM), at WWW 2014},
    year = {2014}
    }

This project targets all websites that offer an automated way of posting ratings to the Twitter platform, see [the MovieTweetings project] (https://github.com/sidooms/MovieTweetings) for more information specific to the IMDb (movie ratings) use case.     

The exact scripts and datasets that were described in the paper are archived in the `MSM-experiment-code-datasets` folder. Since some twitter user ids are present in multiple datasets, the combination of the the datasets in the `MSM-experiment-code-datasets` folder can be used as **a true cross-domain rating dataset**.
    
##Prerequisites
1. Python installation, this project was tested with 2.7.2.
1. The [Twitter module](https://pypi.python.org/pypi/twitter)
1. A set of Twitter API keys (API key, API secret, Access token, Access token secret). They can be obtained through the [Twitter dev website](https://apps.twitter.com/app).

##How it works

The `backbone.py` Python file is the backbone of this project. It connects to the Twitter API and downloads all tweets matching a given query. The other files (e.g. `goodreads.py`) build upon the backbone functionality to collect rating datasets for specific websites. Every time ratings are collected, the corresponding tweets are also saved in a file with the naming structure `tweets_xxx.json`. This json file contains the processed tweets and the xxx in the file name refers to the most recent tweet id collected. Before a script connects to Twitter it checks these tweet ids to make sure only more recent tweets are collected. The scripts can thus be started as many times as desired, with every run only new tweets will be collected.

##How to use it

To automatically collect your own dataset, follow these simple steps:

1. Complete `backbone.py` with your own Twitter API keys (replace the xxx references).
2. Execute the Python file corresponding to the target website e.g. `pandora.py`

        python pandora.py
        
3. Automate the previous step by means of Cron (on Linux) or Task Scheduler (on Windows) to run at fixed time intervals.

Every time the script is run, new tweets will be downloaded, saved, filtered for ratings and finally saved in a rating dataset file.

##Other datasets?

For some websites the scripts are available. But other websites/services can be integrated easily by starting from the e.g. `pandora.py` file and slightly modifying the code. You will need to change the search query to select the right tweets, and define your own process of sanitizing and extracting the interesting data fields from the tweet text. [Contact me](https://twitter.com/sidooms) if you need any help or run into problems.

##Possible problems

From my own experience, what are potential problems you might run into?

- Twitter API limitations. The use of the Twitter API is free but not unlimited. You need to limit yourself to a certain amount of queries that can be requested in a certain time slot. See the [Twitter API documentation](https://dev.twitter.com/docs/rate-limiting/1.1) for the latest info.
- Frequency of data collection. How often do you need to schedule your data collection processes? Run it every day? Every week? Every minute? The answer depends on the target website and more importantly the number of tweets originating from the website. Focus on YouTube and you might collect 200,000 ratings per day, focus on Pandora and you might get only 100 per day. With the above mentioned Twitter API limitations in mind, you need to set the frequency of data collection in a way that it is frequent enough to collect all new ratings but without surpassing the Twitter API limits. Another observation to note here is that the Twitter API also limits how far back in time tweets can be searched on. At the time of writing this was a couple of weeks. So be sure to collect your data more frequently if you do not want to lose any tweets. For reference, here are the time intervals used in the data collection experiment described in the paper: Goodreads every 30m, Pandora every 10m, YouTube every 5m, Lastfm every 30m.

That's it! Remember to [follow me on Twitter](http://twitter.com/sidooms) and tell me how much you like this. By the way, if you liked this you might also like my other Github projects: [MovieTweetings](https://github.com/sidooms/MovieTweetings) and [Recsys-frontend](https://github.com/sidooms/Recsys-frontend).
