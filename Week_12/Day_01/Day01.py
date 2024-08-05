# Entity Recognition using SpaCy
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking at buying U.K. startup for $1 billion"

# Process the text
doc = nlp(text)

# Print entities in the text
for entity in doc.ents:
    print(entity.text, entity.label_)

# Sentiment Analysis using TextBlob
from textblob import TextBlob

# Sample text
text = "I love this product! It works wonderfully."

# Create a TextBlob object
blob = TextBlob(text)

# Get the sentiment
sentiment = blob.sentiment
print(f"Sentiment: {sentiment}")
