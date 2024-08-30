from flask import Flask, request, jsonify
from nlp_processor import process_input

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    user_input = data.get('input')
    
    if user_input:
        response = process_input(user_input)
        return jsonify(response)
    else:
        return jsonify({'error': 'No input provided'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
