import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # TODO
        self.pwords=set()
        self.nwords=set()

        pfile=open(positives,"r")
        for line in pfile:
            if not line.startswith(";" or " "):
                self.pwords.add(line.strip())
        pfile.close()

        nfile=open(negatives,"r")
        for line in nfile:
            if not line.startswith(";" or " "):
                self.nwords.add(line.strip())
        nfile.close()


    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # TODO
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)

        total=0

        for word in tokens:
            if word.lower() in self.pwords:
                total+=1
            elif word.lower() in self.nwords:
                total-=1

        return total
