# analyzer.py
# Smart Customer Feedback Analyzer – Human-Style Code with 💬 Explanations

import pandas as pd
import os
import sys
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from textblob import TextBlob

# --------- Step 0: Required Downloads ---------
# Make sure these NLTK resources are downloaded (only once)
nltk.download('stopwords')
nltk.download('punkt')  # required by TextBlob

# Create global stemmer and stopword list
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# --------- Step 1: Load Feedback Data ---------

def load_data(file_path='feedback_data.csv'):
    """
    Safely loads customer feedback data from a CSV file.

    Args:
        file_path (str): The path of the CSV file. Default is 'feedback_data.csv'.

    Returns:
        DataFrame or None: Returns a pandas DataFrame if successful, else None.
    """
    if not os.path.exists(file_path):
        print(f"\n⚠️ File not found: '{file_path}'\nPlease make sure the file exists in the project folder.")
        return None

    try:
        data = pd.read_csv(file_path)

        # Check if required columns are present
        if 'feedback_id' not in data.columns or 'feedback_text' not in data.columns:
            print("\n❌ Required columns not found in the file.")
            print("Make sure your CSV file has at least two columns: 'feedback_id' and 'feedback_text'.")
            return None

        # Drop any rows where feedback_text is missing
        data.dropna(subset=['feedback_text'], inplace=True)
        data.reset_index(drop=True, inplace=True)

        print(f"\n✅ Successfully loaded {len(data)} feedback entries.\n")
        return data

    except Exception as e:
        print(f"\n❌ Error while reading the file: {str(e)}")
        return None

# --------- Step 2: Preprocess Text ---------

def preprocess_text(text):
    """
    Cleans and simplifies the customer feedback text to make it easy to analyze.

    Steps:
    1. Lowercase the text
    2. Remove punctuation, special characters, emojis, and numbers
    3. Remove common stopwords (like 'the', 'is', etc.)
    4. Stem the remaining words (e.g., "running" → "run")

    Args:
        text (str): Raw feedback text.

    Returns:
        str: Cleaned and simplified text.
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove punctuation, emojis, numbers, special characters
    text = re.sub(r'[^a-z\s]', '', text)

    # Step 3: Tokenize and remove stopwords
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]

    # Step 4: Stemming
    stemmed_words = [stemmer.stem(word) for word in filtered_words]

    # Final cleaned text
    cleaned_text = ' '.join(stemmed_words)
    return cleaned_text

# --------- Step 3: Analyze Sentiment ---------

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given cleaned feedback text.

    Sentiment Polarity Range:
        -1.0 = Very Negative
         0.0 = Neutral
        +1.0 = Very Positive

    Args:
        text (str): Cleaned feedback text (should already be preprocessed).

    Returns:
        str: Sentiment label – 'Positive', 'Neutral', or 'Negative'
    """
    if not isinstance(text, str) or not text.strip():
        return "Neutral"

    try:
        blob = TextBlob(text)
        score = blob.sentiment.polarity

        # Thresholds can be adjusted based on sensitivity
        if score > 0.1:
            return "Positive"
        elif score < -0.1:
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"⚠️ Sentiment analysis failed for text: {text} | Error: {str(e)}")
        return "Neutral"

# --------- Step 4: Run Module (for Testing) ---------

if __name__ == "__main__":
    print("📂 Loading Customer Feedback Data...")
    feedback_data = load_data()

    if feedback_data is None:
        print("🚫 Cannot proceed without valid data. Exiting...")
        sys.exit()

    print("🔍 Sample Feedbacks (Raw):")
    print(feedback_data.head())

    # Optional: Show cleaned + sentiment output for top 5
    print("\n🧪 Analyzing Sample Feedbacks:\n")
    for i in range(min(5, len(feedback_data))):
        raw = feedback_data.loc[i, 'feedback_text']
        cleaned = preprocess_text(raw)
        sentiment = analyze_sentiment(cleaned)
        print(f"🔸 Raw: {raw}")
        print(f"🧽 Cleaned: {cleaned}")
        print(f"💡 Sentiment: {sentiment}\n")
