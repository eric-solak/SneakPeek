from flask import Flask, jsonify, request
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
        db.session.execute(text('''
            CREATE TABLE IF NOT EXISTS posts (
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                image_path VARCHAR(255) NOT NULL,
                identification TEXT, 
                description VARCHAR(255) NOT NULL,
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


@app.route('/identify', methods=['POST'])
def home():
    image = request.files['image']
    image_path = os.path.join("images", image.filename)
    image.save(image_path)
    post_details = request.form["post_details"]

    identification = BlackboardController(image_path, post_details)
    identification.identify()
    result = identification.getresponse()

    db.session.execute(text('''
                INSERT INTO posts (image_path, description, rating, identification) VALUES
                (image_path, post_details, 25, result);
            '''))
        

    return jsonify({"message": result})

@app.route('/get-posts', methods=['GET'])
def add_user():
    add_data_test()
    '''
    sort_type = request.args.get('type')
    if sort_type == "popular":
    '''
    with app.app_context():
        post_query = db.session.execute(text('''
            SELECT p.pid, p.image_path, p.description, p.rating
            FROM posts p 
            ORDER BY p.rating DESC
            LIMIT 10;
        '''))
        rows = post_query.fetchall()

        posts = [
            {
                "pid": row.pid,
                "image_path": row.image_path,
                "description": row.description,
                "rating": row.rating
            }
            for row in rows
        ]

        comment_query = db.session.execute(text('''
            SELECT c.cid, c.body
            FROM comments c
            LEFT JOIN posts p ON c.post_id = p.pid
        '''))


    return jsonify({"posts": posts})

from flask import send_from_directory

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)

def add_data_test():
    try:
        db.session.execute(text('''
            INSERT INTO users (email, password) VALUES
            ('alice@example.com', 'hashed_pw1'),
            ('bob@example.com', 'hashed_pw2'),
            ('charlie@example.com', 'hashed_pw3');
        '''))
        db.session.execute(text('''
            INSERT INTO posts (image_path, description, rating) VALUES
            ('/images/img_1.png', 'Red running shoes', 5),
            ('/images/img.png', 'Black sneakers', 8),
            ('/images/img_1.png', 'White high tops', 3);
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
    app.run(host="0.0.0.0", port=5000, debug=True)