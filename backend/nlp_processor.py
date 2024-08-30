import spacy
from transformers import pipeline

# Load spaCy's English model for basic NLP tasks
nlp = spacy.load('en_core_web_sm')

# Load transformers pipeline for text classification
classifier = pipeline('text-classification')

def process_input(user_input):
    # Use spaCy to parse user input
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Use transformers for intent recognition or sentiment analysis
    classification = classifier(user_input)
    
    response = {
        "entities": entities,
        "classification": classification
    }
    return response
