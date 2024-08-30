# Project Overview

This project is a comprehensive natural language processing (NLP) system designed to classify user inputs into predefined intents and extract relevant entities. The system leverages the power of fine-tuned BERT models for intent classification and spaCy for entity recognition.

# Key Features

1. **Intent Classification**: The system can classify user inputs into predefined intents using a fine-tuned BERT model. This allows for accurate identification of user goals and enables the system to respond accordingly.
2. **Entity Recognition**: Utilizing spaCy, the system can extract entities such as names, locations, and organizations from user inputs. This feature enhances the system's ability to understand the context and provide more personalized responses.
3. **Label Mapping**: The project includes a label mapping system that converts numerical labels to human-readable labels, making it easier to understand the classification results.
4. **Modular Design**: The system is designed with modularity in mind, allowing for easy integration of new models, tokenizers, or NLP tools as needed.

# Technical Details

* **Backend**: The project uses Python as the primary programming language.
* **NLP Models**: The system leverages fine-tuned BERT models for intent classification and spaCy for entity recognition.
* **Tokenization**: The project utilizes the Hugging Face Transformers library for tokenization.
* **Label Mapping**: The label mapping system is implemented using JSON files for easy maintenance and updates.

# Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Ensure you have the necessary NLP models and tokenizers installed.
4. Run the project using your preferred method (e.g., using a Python IDE or command line).

# Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes.
4. Submit a pull request.

# License

This project is licensed under the MIT License.
