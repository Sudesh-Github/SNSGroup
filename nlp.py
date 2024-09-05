import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data files (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to preprocess and tokenize text with edge case handling
def preprocess_and_tokenize(text):
    # Convert text to lowercase to handle case sensitivity
    text = text.lower()

    # Remove all non-alphabetic characters (punctuation, numbers, special chars)
    # This also ensures we handle punctuations like ".", "!", "?", etc.
    text = re.sub(r'[^a-z\s]', '', text)
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords and filter out empty tokens (if any)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and word != '']
    
    # Lemmatize the tokens to handle different forms of the words
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens

# Example usage
text_data = "Hello! Is this the NLP preprocess? Yes, it's awesome!"
tokens = preprocess_and_tokenize(text_data)
print(tokens)
