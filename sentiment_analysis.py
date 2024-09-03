from textblob import TextBlob
import pandas as pd

def analyze_sentiment(text):
  blob = TextBlob(text)
  sentiment_score = blob.sentiment.polarity # Polarity score ranges from -1 to 1
  return sentiment_score


file_path = r'C:\Users\bahad\OneDrive\Desktop\NLP\cleaned_file.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Apply sentiment analysis
df['Sentiment_Score'] = df['Customer_Review'].apply(analyze_sentiment)

# Save the results
df.to_csv("sentiment_scores.csv", index=False)

print("Sentiment analysis complete. Results saved to 'sentiment_scores.csv'.")