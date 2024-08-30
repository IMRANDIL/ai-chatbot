from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_name = "bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def classify_intent(text):
    classifier = pipeline('text-classification', model=model, tokenizer=tokenizer)
    return classifier(text)
