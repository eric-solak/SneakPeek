from flask import Flask, jsonify
from flask_cors import CORS  # Enable CORS for React Native

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

@app.route('/agent1', methods=['GET'])
def home():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True)
