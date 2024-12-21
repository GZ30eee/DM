import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

# Step 1: Load Data
data = pd.read_csv("cleaned_data.csv")

# Step 2: Preprocess Text
def clean_text(text):
    if isinstance(text, str):  # Ensure the input is a string
        text = re.sub(r"http\S+", "", text)  # Remove URLs
        text = re.sub(r"@\w+", "", text)    # Remove mentions
        text = re.sub(r"#\w+", "", text)    # Remove hashtags
        text = re.sub(r"[^\w\s]", "", text) # Remove punctuation
        return text.strip().lower()         # Normalize case and trim spaces
    return ""  # Return an empty string for non-string values

data['cleaned_text'] = data['text'].apply(clean_text)

# Remove rows with empty 'cleaned_text'
data = data[data['cleaned_text'] != ""]

# Step 3: Sentiment Analysis
def analyze_sentiment(text):
    if text.strip():  # Only analyze non-empty text
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
    return "Neutral"  # Default to Neutral for empty or invalid text

data['Sentiment'] = data['cleaned_text'].apply(analyze_sentiment)

# Step 4: Visualize Sentiment Distribution
sentiment_counts = data['Sentiment'].value_counts()

# Pie Chart
plt.figure(figsize=(8, 6))
sentiment_counts.plot.pie(
    autopct='%1.1f%%', 
    colors=['lightgreen', 'gold', 'red'], 
    startangle=140, 
    labels=sentiment_counts.index
)
plt.title("Sentiment Distribution")
plt.ylabel("")  # Remove default ylabel
plt.show()

# Bar Graph
plt.figure(figsize=(8, 6))
sentiment_counts.plot(
    kind='bar', 
    color=['lightgreen', 'gold', 'red'], 
    edgecolor='black'
)
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Posts")
plt.xticks(rotation=0)
plt.show()

# Step 5: Output Sample Data
print(data.head())
