from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import spacy
import json

# Load the fine-tuned model and tokenizer
model_name = './fine-tuned-model'
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
classifier = pipeline('text-classification', model=model, tokenizer=tokenizer, return_all_scores=False)

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Load label mapping
with open('label_mapping.json', 'r') as f:
    label_mapping = json.load(f)

# Inverse label mapping for conversion
id_to_label = {v: k for k, v in label_mapping.items()}

def process_input(user_input):
    # Use spaCy for entity recognition
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Use fine-tuned BERT model for intent classification
    classification = classifier(user_input)
    
    # Map label IDs to human-readable labels
    if classification:
        # Extract the top classification
        label = classification[0]['label']
        confidence = classification[0]['score']
        label_id = int(label.replace('LABEL_', ''))  # Convert LABEL_28 to 28
        label_name = id_to_label.get(label_id, 'unknown')  # Map ID to label name
        classification_result = {
            'label': label_name,
            'score': confidence
        }
    else:
        classification_result = {
            'label': 'unknown',
            'score': 0.0
        }

    response = {
        "entities": entities,
        "classification": classification_result
    }
    return response
