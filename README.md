
# AI Chatbot for Customer Support

Welcome to the AI Chatbot project! This repository contains a chatbot designed to handle customer queries and provide relevant information based on user inputs. Built using state-of-the-art NLP models and custom-trained on a dataset of customer service-related questions, this chatbot is optimized to deliver accurate and contextually appropriate responses.

## Features

- **Intent Classification**: Classify user queries into predefined categories such as store hours, return policies, and order tracking.
- **Entity Recognition**: Identify and extract relevant entities from user inputs using spaCy.
- **Fine-Tuned BERT Model**: Utilizes a fine-tuned BERT model for high-quality intent classification.
- **API Integration**: Provides a REST API for easy integration into web or mobile applications.

## Getting Started

### Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) (for isolated Python environments)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/IMRANDIL/ai-chatbot.git
    cd ai-chatbot
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download or train the model:**

    Follow the instructions in `train_model.py` to train your model or use the pre-trained model available in the repository.

5. **Prepare the dataset:**

    Ensure that your training data is in the `training.csv` file format.

### Usage

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

    The API will be available at `http://localhost:5000`.

2. **Send a POST request to the `/process` endpoint with the user input:**

    Example using `curl`:

    ```bash
    curl -X POST http://localhost:5000/process -H "Content-Type: application/json" -d '{"input": "What are your store hours?"}'
    ```

    Example request body:

    ```json
    {
      "input": "What are your store hours?"
    }
    ```

    Example response:

    ```json
    {
      "entities": [],
      "classification": {
        "label": "store_hours",
        "score": 0.95
      }
    }
    ```

### Model Training

To train the model, use the `train_model.py` script:

```bash
python train_model.py
```

Ensure that `training.csv` is correctly formatted and contains the necessary training data.

### Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- **Hugging Face Transformers** for providing powerful NLP models.
- **spaCy** for robust entity recognition.
- **Flask** for the lightweight API server.

For any questions or support, please reach out to [your email address] or open an issue in the repository.
