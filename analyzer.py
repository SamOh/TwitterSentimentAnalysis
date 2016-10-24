from nltk.tokenize import TweetTokenizer

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives="positive-words.txt", negatives="negative-words.txt"):
        """Initialize Analyzer."""
        self.positives = positives
        self.negatives = negatives
        self.sentiment_score = 0
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        self.sentiment_score = 0
        tknzr = TweetTokenizer()
    
        text_list = tknzr.tokenize(text)
        for text in text_list:
            if text in open(self.positives).read():
                self.sentiment_score += 1
            elif text in open(self.negatives).read():
                self.sentiment_score -= 1
        
        return self.sentiment_score
