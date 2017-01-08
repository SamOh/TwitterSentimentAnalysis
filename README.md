# twitter_sentiment_analysis
Currently staff for CS50 class at Harvard. This year, we are offering a new problem set
so as a staff member I tested it out by implementing a solution to it.
Idea/framework for this specific project goes to CS50.

# How it works
Very basic sentiment analysis based on key words. Using the tweets function as such
```
./tweets @handle
```
you can query the 50 most recent tweets of the handle you input and see a sentiment score
of each tweet based on key words provided by researchers (source in positive-words.txt and negative-words.txt)

You can also run the flask application locally and search for a twitter handle and
get a nice pie chart showing the percentage of positive vs. negative vs. neutral for
a specfic person's twitter account.
