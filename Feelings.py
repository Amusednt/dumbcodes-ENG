# Import necessary libraries
from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text.
    
    Parameters:
    text (str): The text to analyze.
    
    Returns:
    str: Sentiment classification (Positive, Negative, or Neutral).
    """
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity score
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
if __name__ == "__main__":
    # Sample texts for sentiment analysis
    sample_texts = [
        "I love this product! It's amazing.",
        "This is the worst experience I've ever had.",
        "It's okay, neither good nor bad.",
        "I'm really happy with the results!"
    ]
    
    # Analyze and print the sentiment of each sample text
    for text in sample_texts:
        sentiment = analyze_sentiment(text)
        print(f"Text: {text}\nSentiment: {sentiment}\n")