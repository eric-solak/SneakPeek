from flask import Flask, jsonify, request
from flask_cors import CORS  # Enable CORS for React Native
import os
from backend.blackboard import BlackboardController

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

@app.route('/identify', methods=['POST'])
def home():
    image = request.files['image']
    image_path = os.path.join("images", image.filename)
    image.save(image_path)
    post_details = request.form["post_details"]

    identification = BlackboardController(image_path, post_details)
    identification.identify()
    result = identification.getresponse()
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)
