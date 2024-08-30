import pandas as pd
import json
from transformers import BertForSequenceClassification, Trainer, TrainingArguments, BertTokenizer
from datasets import load_dataset, Dataset

# Convert CSV labels to integer labels
def encode_labels(csv_file, encoded_csv_file, label_mapping_file):
    df = pd.read_csv(csv_file)
    labels = df['label'].unique()
    label_to_id = {label: i for i, label in enumerate(labels)}
    df['label'] = df['label'].map(label_to_id)
    df.to_csv(encoded_csv_file, index=False)
    with open(label_mapping_file, 'w') as f:
        json.dump(label_to_id, f)

# Convert string labels to integers and save new CSV
encode_labels('training.csv', 'training_encoded.csv', 'label_mapping.json')

# Load pre-trained tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=len(json.load(open('label_mapping.json'))))  # Update num_labels based on label mapping

# Load and tokenize dataset
dataset = load_dataset('csv', data_files={'train': 'training_encoded.csv'})  # Load your custom dataset

# Tokenize function
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True)

# Apply tokenization to dataset
tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Set format for PyTorch
tokenized_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'label'])

# Define training arguments without evaluation
training_args = TrainingArguments(
    output_dir='./results',
    logging_dir='./logs',  # Optional: directory to save logs
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    evaluation_strategy="no"  # No evaluation
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained('./fine-tuned-model')
tokenizer.save_pretrained('./fine-tuned-model')
