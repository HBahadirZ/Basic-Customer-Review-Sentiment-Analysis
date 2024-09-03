import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string


lemmatizer = WordNetLemmatizer()

# Preprocessing function
def preprocess_text(text):
        text = text.lower()  # Convert to lowercase
        text = text.translate(str.maketrans("", "", string.punctuation))  # Remove punctuation
        tokens = word_tokenize(text)  # Tokenize the text
        stop_words = set(stopwords.words("english"))  # Get English stop words
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]  # Remove stop words and lemmatize
        return " ".join(tokens)  # Rejoin tokens into a string

# File paths
file_path = r'C:\Users\bahad\OneDrive\Desktop\NLP\Sample_Customer_Reviews.csv'
output_path = r'C:\Users\bahad\OneDrive\Desktop\NLP\cleaned_file.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Apply preprocessing
df['Customer_Review'] = df['Customer_Review'].apply(preprocess_text)

# Save the cleaned data
df.to_csv(output_path, index=False)

print("Preprocessing complete. Cleaned data saved to 'cleaned_file.csv'.")
