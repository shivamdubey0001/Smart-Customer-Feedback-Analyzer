#!/usr/bin/env python3
# main.py
# Main script to run the Smart Customer Feedback Analyzer

import json
import pandas as pd
from analyzer import load_data, preprocess_text, analyze_sentiment

def main():
    """
    Main function to run the complete feedback analysis pipeline
    """
    print("🚀 Starting Smart Customer Feedback Analyzer...")
    print("=" * 50)

    # Step 1: Load the data
    print("\n📂 Loading feedback data...")
    data = load_data('feedback_data.csv')

    if data is None:
        print("❌ Cannot proceed without data. Exiting...")
        return

    # Step 2: Process each feedback
    print("\n🔄 Processing feedbacks...")
    results = []

    for index, row in data.iterrows():
        feedback_id = row['feedback_id']
        raw_text = row['feedback_text']

        # Clean the text
        cleaned_text = preprocess_text(raw_text)

        # Analyze sentiment
        sentiment = analyze_sentiment(cleaned_text)

        # Determine topic based on keywords
        topic = determine_topic(raw_text.lower())

        # Store results
        result = {
            'feedback_id': int(feedback_id),
            'original_text': raw_text,
            'cleaned_text': cleaned_text,
            'sentiment': sentiment,
            'topic': topic
        }
        results.append(result)

        print(f"✅ Processed feedback {feedback_id}: {sentiment} | {topic}")

    # Step 3: Save results to JSON
    print(f"\n💾 Saving results to analysis_results.json...")
    with open('analysis_results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # Step 4: Show summary
    show_summary(results)

    print("\n🎉 Analysis complete! Check 'analysis_results.json' for detailed results.")

def determine_topic(text):
    """
    Simple topic classification based on keywords
    """
    text = text.lower()

    if any(word in text for word in ['delivery', 'shipping', 'dispatch', 'arrived', 'delayed']):
        return 'Delivery'
    elif any(word in text for word in ['quality', 'defect', 'excellent', 'poor', 'damaged']):
        return 'Product Quality'
    elif any(word in text for word in ['service', 'support', 'staff', 'representative', 'help']):
        return 'Customer Service'
    elif any(word in text for word in ['price', 'money', 'cost', 'value', 'expensive', 'cheap']):
        return 'Pricing'
    elif any(word in text for word in ['website', 'navigate', 'interface', 'app']):
        return 'Website/App'
    elif any(word in text for word in ['return', 'refund', 'policy']):
        return 'Return Policy'
    elif any(word in text for word in ['packaging', 'package', 'box']):
        return 'Packaging'
    else:
        return 'General'

def show_summary(results):
    """
    Display a summary of the analysis results
    """
    print("\n📊 ANALYSIS SUMMARY")
    print("=" * 30)

    # Sentiment distribution
    sentiment_counts = {}
    topic_counts = {}

    for result in results:
        sentiment = result['sentiment']
        topic = result['topic']

        sentiment_counts[sentiment] = sentiment_counts.get(sentiment, 0) + 1
        topic_counts[topic] = topic_counts.get(topic, 0) + 1

    print("\n💭 Sentiment Distribution:")
    for sentiment, count in sentiment_counts.items():
        percentage = (count / len(results)) * 100
        print(f"   {sentiment}: {count} ({percentage:.1f}%)")

    print("\n🏷️ Topic Distribution:")
    for topic, count in topic_counts.items():
        percentage = (count / len(results)) * 100
        print(f"   {topic}: {count} ({percentage:.1f}%)")

    print(f"\n📈 Total Feedbacks Analyzed: {len(results)}")

if __name__ == "__main__":
    main()
