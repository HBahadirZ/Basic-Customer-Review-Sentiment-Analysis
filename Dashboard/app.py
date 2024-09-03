from flask import Flask, render_template, jsonify
from textblob import TextBlob
import pandas as pd

app = Flask(__name__)

# Read the csv file 
df = pd.read_csv(r"C:\Users\bahad\OneDrive\Desktop\NLP\cleaned_file.csv")

# Function to analyze sentiment
def analyze_sentiment(text):
  blob = TextBlob(text)
  return blob.sentiment.polarity

# Prepare data for display
def get_sentiment_data():
  # Check if 'Sentiment_Score' column exists, or analyze sentiment if needed
  if 'Sentiment_Score' not in df.columns:
      df['Sentiment_Score'] = df['Customer_Review'].apply(analyze_sentiment)
  
  # Add sentiment labels
  df["Sentiment_Label"] = df["Sentiment_Score"].apply(
      lambda score: "Positive" if score > 0 else "Negative" if score < 0 else "Neutral"
  )
  return df.to_dict(orient="records")

@app.route("/")
def index():
  data = get_sentiment_data()
  return render_template("index.html", data=data)

@app.route("/api/sentiment")
def sentiment_api():
  data = get_sentiment_data()
  return render_template("index.html", data=data)

@app.route("/sentiment_data")
def sentiment_data():
  data = get_sentiment_data()
  sentiment_counts = {
    "Positive": sum(1 for item in data if item['Sentiment_Label'] == 'Positive'),
    "Negative": sum(1 for item in data if item['Sentiment_Label'] == 'Negative'),
    "Neutral": sum(1 for item in data if item['Sentiment_Label'] == 'Neutral')
}
  return jsonify(sentiment_counts)


if __name__ == "__main__":
  app.run(debug=True)