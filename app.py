import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from ML Flask app!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json or {}
    # placeholder: your model inference would be here
    result = {"prediction": "positive", "input_received": data}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
