from flask import Flask, jsonify, request
from flask_cors import CORS  # Enable CORS for React Native
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from blackboard import BlackboardController

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print("Database location:", os.path.abspath(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))

def setup_db():
    with app.app_context():
        db.session.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(120) NOT NULL
            );
        '''))
        db.session.commit()


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


@app.route('/add_user', methods=['GET'])
def add_user():
    password = request.args.get('password')
    email = request.args.get('email')
    with app.app_context():
        # Insert the new user
        db.session.execute(
            text('INSERT INTO users (password, email) VALUES (:password, :email)'),
            {'password': password, 'email': email}
        )
        db.session.commit()


        # Run raw SQL to select all users
        result = db.session.execute(text('SELECT * FROM users'))

        # Convert rows to dicts
        users = [dict(row._mapping) for row in result]

    return jsonify({"result": "success", "DB": users})


'''
Get all posts 
create post store in db
identify 

- delete post 
- comment 

'''

if __name__ == '__main__':
    setup_db()
    app.run(debug=True)
