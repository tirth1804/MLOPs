from flask import Flask, jsonify, request
from your_model import predict  # Import your model's prediction function

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def prediction():
    data = request.get_json(force=True)
    result = predict(data)  # Use your model to make predictions
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)
