from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS  # Enable CORS for React Native
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
import json
from blackboard import BlackboardController

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print("Database location:", os.path.abspath(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))

@app.route('/createpost', methods=['POST'])
def create_post():
    image = request.files['image']
    image_path = os.path.join("images", image.filename)
    image.save(image_path)
    post_description = request.form["post_description"]
    post_title = request.form["post_title"]

    identification = BlackboardController(image_path, post_description)
    identification.identify()
    result = identification.getresponse()
    result_json = json.dumps(result)

    db.session.execute(text('''
                INSERT INTO posts (image_path, description, rating, identification, title) VALUES
                (:image_path, :description, 0, :result, :title);
            ''').bindparams(image_path=image_path, description=post_description, result=result_json, title=post_title))
    db.session.commit()

    return jsonify({"message": result})

@app.route('/get-posts', methods=['GET'])
def get_posts():
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

@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)