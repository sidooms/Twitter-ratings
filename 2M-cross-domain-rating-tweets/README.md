2 Million Cross-Domain Rating Tweets
===============

Using the scripts from the [Twitter-ratings Github project](https://github.com/sidooms/Twitter-ratings) I collected 2 million tweets containing preference data (ratings or implicit feedback) originating from 5 different online services: Amazon, LastFM, MyJam, Pandora and Spotify. All tweets are posted between 30/01/2014 and 28/11/2014. As [previous experiments](http://www.slideshare.net/simondooms/static-mining-cross-domain-rating-datasets-from-structured-data-on-twitter) indicated, users may have tweeted across multiple services which makes this an potentially interesting dataset for e.g., cross-domain  recommender systems research.

The total number of collected tweets is nearly 2 million (1,992,756 to be exact). The number of tweets collected per online service is:

+ Spotify: 1,702,653 (Twitter Search API query: "#nowplaying on spotify")
+ MyJam: 194,292 (Twitter Search API query: "t.thisismyjam.com")
+ LastFM: 41,831 (Twitter Search API query: "I'm listening to via @lastfm")
+ Amazon: 38,861 (Twitter Search API query: "i just bought via @amazon") 
+ Pandora: 15,119 (Twitter Search API query: "I am listening to by on Pandora #pandora")

The corresponding files contain one tweet per line with the following structure: <Time of collection>,<Tweet metadata>. Here's an example of what a single line in the Amazon dataset may look like:

> 1417178821,{"contributors": null, "truncated": false, "text": "I just bought: 'Avalon Organics Scalp... Reply w/ #AmazonWishList to add this via @amazon #BlackFriday #BF2014 http://t.co/b9Nshf9XpM", "in_reply_to_status_id": null, "id": 538312291758776320, "favorite_count": 0, "source": "<a href=\"https://dev.twitter.com/docs/tfw\" rel=\"nofollow\">Twitter for Websites</a>", "retweeted": false, "coordinates": null, "entities": {"symbols": [], "user_mentions": [{"id": 20793816, "indices": [82, 89], "id_str": "20793816", "screen_name": "amazon", "name": "Amazon"}], "hashtags": [{"indices": [50, 65], "text": "AmazonWishList"}, {"indices": [90, 102], "text": "BlackFriday"}, {"indices": [103, 110], "text": "BF2014"}], "urls": [{"url": "http://t.co/b9Nshf9XpM", "indices": [111, 133], "expanded_url": "http://www.amazon.com/dp/B000IZ8KZ4/ref=cm_sw_r_tw_asp_Qr4SI.0455RA3", "display_url": "amazon.com/dp/B000IZ8KZ4/…"}]}, "in_reply_to_screen_name": null, "in_reply_to_user_id": null, "retweet_count": 0, "id_str": "538312291758776320", "favorited": false, "user": {"follow_request_sent": false, "profile_use_background_image": true, "profile_text_color": "3C3940", "default_profile_image": false, "id": 80471951, "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme4/bg.gif", "verified": false, "profile_location": null, "profile_image_url_https": "https://pbs.twimg.com/profile_images/763863072/1808411_normal.jpg", "profile_sidebar_fill_color": "95E8EC", "entities": {"url": {"urls": [{"url": "https://t.co/9FZIA8syIA", "indices": [0, 23], "expanded_url": "https://www.facebook.com/kyuha.yoo", "display_url": "facebook.com/kyuha.yoo"}]}, "description": {"urls": []}}, "followers_count": 150, "profile_sidebar_border_color": "5ED4DC", "id_str": "80471951", "profile_background_color": "0099B9", "listed_count": 2, "is_translation_enabled": false, "utc_offset": 32400, "statuses_count": 1192, "description": "Seoul, S. KOREA", "friends_count": 279, "location": "http://ykh5903.cyworld.com/", "profile_link_color": "004DB8", "profile_image_url": "http://pbs.twimg.com/profile_images/763863072/1808411_normal.jpg", "following": false, "geo_enabled": true, "profile_background_image_url": "http://abs.twimg.com/images/themes/theme4/bg.gif", "name": "Kyuha Yoo", "lang": "ko", "profile_background_tile": false, "favourites_count": 9, "screen_name": "beautyguy11", "notifications": false, "url": "https://t.co/9FZIA8syIA", "created_at": "Wed Oct 07 02:38:40 +0000 2009", "contributors_enabled": false, "time_zone": "Seoul", "protected": false, "default_profile": false, "is_translator": false}, "geo": null, "in_reply_to_user_id_str": null, "possibly_sensitive": false, "lang": "en", "created_at": "Fri Nov 28 12:43:46 +0000 2014", "in_reply_to_status_id_str": null, "place": null, "metadata": {"iso_language_code": "en", "result_type": "recent"}}

Please cite the corresponding paper if you make use of this data:

    @conference{Dooms14msm,
    author = {Dooms, Simon and De Pessemier, Toon and Martens, Luc},
    title = {Cross-Domain Rating Datasets from Structured Data on Twitter},
    booktitle = {Workshop on Modeling Social Media: Mining Big Data in Social Media and the Web (MSM), at WWW 2014},
    year = {2014}
    }

That's it! Remember to [follow me on Twitter](http://twitter.com/sidooms) and tell me if you like this. By the way, if you liked this, you might also like my other Github projects: [MovieTweetings](https://github.com/sidooms/MovieTweetings) and [Recsys-frontend](https://github.com/sidooms/Recsys-frontend).
