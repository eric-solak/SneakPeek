from flask import Flask
from flask_cors import CORS  # Enable CORS for React Native
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
from blackboard import BlackboardController

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def setup_db():
    with app.app_context():
        db.session.execute(text('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email VARCHAR(50) NOT NULL UNIQUE,
                password VARCHAR(120) NOT NULL
            );
        '''))
        db.session.execute(text('''
            CREATE TABLE IF NOT EXISTS posts (
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255) NOT NULL,
                image_path VARCHAR(255) NOT NULL,
                identification TEXT, 
                description TEXT,
                rating INTEGER NOT NULL DEFAULT 0,
                time DATE
            );
        '''))
        db.session.execute(text('''
                CREATE TABLE IF NOT EXISTS comments (
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    post_id INTEGER NOT NULL,
                    body TEXT NOT NULL,
                    FOREIGN KEY (post_id) REFERENCES posts(pid)
                    );
                '''))
        db.session.commit()
    print("Tables created successfully.")

def add_data_test():
    with app.app_context():
        try:
            db.session.execute(text('''
                INSERT INTO users (email, password) VALUES
                ('alice@example.com', 'hashed_pw1'),
                ('bob@example.com', 'hashed_pw2'),
                ('charlie@example.com', 'hashed_pw3');
            '''))

            db.session.execute(text('''
                INSERT INTO posts (image_path, description, title) VALUES
                ('/images/testing1.png', 'What is the make of this shoe?', 'Running Shoe'),
                ('/images/testing2.png', 'Where can I buy this shoe', 'Basketball Shoe'),
                ('/images/testing3.png', 'This is my favourite shoe', 'White High Tops');
            '''))

            db.session.execute(text('''
                INSERT INTO comments (post_id, body) VALUES
                (1, 'These are sick! 🔥'),
                (1, 'I love the color.'),
                (2, 'They look super comfy.'),
                (3, 'Not really my style.'),
                (2, 'Bought these last week, amazing quality!');
            '''))

            db.session.commit()
        except Exception as e:
            print(f"Error: {e}")




'''
Get all posts 
create post store in db
identify 

- delete post 
- comment 

'''

if __name__ == '__main__':
    setup_db()
    #add_data_test()