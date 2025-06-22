from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Initialize tools
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    # Tokenize and lowercase
    tokens = word_tokenize(text.lower())
    # Remove punctuation and stopwords
    cleaned = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word.isalnum() and word not in stop_words
    ]
    return cleaned