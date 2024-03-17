import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from nltk.corpus import stopwords
import re

# Define positive and negative words
positive_words = ["positive", "upward", "best", "buy", "recommended", "better", "bullish", "thrive", "opportunity", "benefit", "positive", "great", "better", "higher", "much", "aggressive", "highly", "recommended"]
negative_words = ["panic", "crashed", "hit", "fall", "overhyped", "corrected", "struggles", "fear", "negative", "pressure", "loss", "pinch", "problems", "caution", "risk", "worry", "struggles", "fear", "negative", "pinch", "problems", "caution", "risk", "worry", "loss"]

# Get the list of stopwords
stopwords_list = set(stopwords.words('english'))

def remove_stopwords(content):
    # Split the content into words
    words = content.split()

    # Remove stopwords not in positive or negative words lists
    filtered_words = [word for word in words if word.lower() not in stopwords_list or word.lower() in positive_words or word.lower() in negative_words]

    # Join the filtered words back into a string
    filtered_content = " ".join(filtered_words)

    # Remove unnecessary spaces
    filtered_content = ' '.join(filtered_content.split())

    # Add space after punctuation marks to maintain readability
    filtered_content = re.sub(r'(?<=[.!?])\s+', '\n', filtered_content)
    filtered_content = re.sub(r"© Reuters.\n", "", filtered_content)

    return filtered_content

# Function to extract text content and title from the URL
def extract_article_content(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the title of the article
        title_element = soup.find('h1', class_='articleHeader')

        # Extract the title text
        if title_element:
            article_title = title_element.text.strip()
        else:
            article_title = "No title found."

        # Find the main content of the article
        article_content = soup.find('div', class_='articlePage')

        # Extract the text content of the article
        if article_content:
            article_text = article_content.get_text(separator='\n')
            return article_title, article_text
    else:
        # If the request was not successful, print an error message
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None, None

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)

    # Perform sentiment analysis
    sentiment_score = blob.sentiment.polarity

    # Classify sentiment
    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_score

def save_article_content(content, filename):
    # Write the content to a file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

# URL of the news article
article_url = "https://www.investing.com/news/stock-market-news/apple-stock-buyback-heres-what-this-analyst-thinks-will-happen-3335921"

# Extract title and text content from the article URL
article_title, article_text = extract_article_content(article_url)

# Remove stopwords not in positive or negative words lists
filtered_content = remove_stopwords(article_text)

# Save the filtered content to a file
save_article_content(filtered_content, "filtered_article_content.txt")

# Perform sentiment analysis on the extracted text
if article_text:
    sentiment, sentiment_score = analyze_sentiment(article_text)
    print("Sentiment:", sentiment)
    print("Sentiment Score:", sentiment_score, "\n")
else:
    print("Failed to retrieve article content.")
print("Title:", article_title)
print("Text:", filtered_content)