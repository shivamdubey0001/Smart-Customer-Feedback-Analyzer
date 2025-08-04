
# Smart Customer Feedback Analyzer 🤖💬

A Python-based intelligent system that automatically analyzes customer feedback to extract sentiments and categorize topics. This tool helps businesses understand customer opinions and identify key areas for improvement.

## 🎯 Features

- **Sentiment Analysis**: Automatically classifies feedback as Positive, Negative, or Neutral
- **Topic Classification**: Categorizes feedback into relevant topics (Delivery, Product Quality, Customer Service, etc.)
- **Text Preprocessing**: Cleans and prepares text data for accurate analysis
- **JSON Output**: Saves results in a structured, easy-to-read format
- **Summary Reports**: Provides statistical overview of feedback analysis

## 📁 Project Structure

```
project_1/
├── analyzer.py              # Core analysis functions
├── main.py                  # Main execution script
├── feedback_data.csv        # Input customer feedback data
├── analysis_results.json    # Output analysis results
└── README.md               # Project documentation
```

## 🚀 How to Run

1. **Install Required Libraries** (if not already installed):
   ```bash
   pip install pandas nltk textblob
   ```

2. **Download NLTK Data** (first time only):
   ```python
   import nltk
   nltk.download('stopwords')
   nltk.download('punkt')
   ```

3. **Run the Analyzer**:
   ```bash
   python main.py
   ```

## 📊 Input Data Format

The `feedback_data.csv` file should contain:
- `feedback_id`: Unique identifier for each feedback
- `feedback_text`: The actual customer feedback text

Example:
```csv
feedback_id,feedback_text
1,"Great product! Fast delivery and excellent quality."
2,"Poor customer service. Very disappointed."
```

## 📈 Output Format

Results are saved in `analysis_results.json` with the following structure:

```json
[
  {
    "feedback_id": 1,
    "original_text": "Great product! Fast delivery and excellent quality.",
    "cleaned_text": "great product fast deliveri excel qualiti",
    "sentiment": "Positive",
    "topic": "Product Quality"
  }
]
```

## 🔧 Technical Implementation

### Sentiment Analysis
- Uses **TextBlob** library for sentiment polarity calculation
- Threshold-based classification:
  - Positive: polarity > 0.1
  - Negative: polarity < -0.1
  - Neutral: -0.1 ≤ polarity ≤ 0.1

### Topic Classification
- Keyword-based topic detection
- Categories include:
  - Delivery
  - Product Quality
  - Customer Service
  - Pricing
  - Website/App
  - Return Policy
  - Packaging
  - General

### Text Preprocessing
- Converts to lowercase
- Removes punctuation and special characters
- Filters out stopwords
- Applies stemming for word normalization

## 🎯 Use Cases

- **E-commerce**: Analyze product reviews and customer feedback
- **Customer Support**: Identify common complaints and issues
- **Product Development**: Understand customer preferences and pain points
- **Marketing**: Gauge customer satisfaction and brand perception

## 🔮 Future Enhancements

- Web dashboard for visualization
- Real-time feedback processing
- Advanced ML models for better accuracy
- Multi-language support
- Integration with social media APIs

## 📝 Sample Results

When you run the analyzer, you'll see output like:

```
🚀 Starting Smart Customer Feedback Analyzer...
📂 Loading feedback data...
✅ Successfully loaded 15 feedback entries.

🔄 Processing feedbacks...
✅ Processed feedback 1: Positive | Product Quality
✅ Processed feedback 2: Negative | Customer Service

📊 ANALYSIS SUMMARY
💭 Sentiment Distribution:
   Positive: 6 (40.0%)
   Negative: 5 (33.3%)
   Neutral: 4 (26.7%)

🏷️ Topic Distribution:
   Product Quality: 4 (26.7%)
   Customer Service: 3 (20.0%)
   Delivery: 3 (20.0%)
```

## 👨‍💻 Developer

Created with ❤️ as a demonstration of Natural Language Processing and Data Analysis skills.

---
*This project showcases Python programming, data analysis, natural language processing, and machine learning concepts.*
