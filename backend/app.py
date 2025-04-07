from flask import Flask, jsonify, request, send_file, send_from_directory
from flask_cors import CORS  # Enable CORS for React Native
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os, json, uuid

from sqlalchemy.engine import row

from blackboard import BlackboardController
from PIL import Image

app = Flask(__name__)
CORS(app)  # Allow requests from React Native

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print("Database location:", os.path.abspath(app.config['SQLALCHEMY_DATABASE_URI'].replace('sqlite:///', '')))


@app.route('/createpost', methods=['POST'])
def create_post():
    # Getting form data from POST
    uploaded_image = request.files['image']
    post_description = request.form["post_description"]
    post_title = request.form["post_title"]

    # Formatting image for saving
    image = Image.open(uploaded_image).convert("RGB")
    image.thumbnail((800, 800), Image.Resampling.LANCZOS)
    unique_filename = f"{uuid.uuid4()}.png"
    image_path = os.path.join("images", unique_filename)
    image_path_url = image_path.replace(os.sep, "/")
    image.save(image_path, format="PNG")

    identification_request = BlackboardController(image_path, post_description)
    identification_request.identify()
    result = identification_request.getresponse()


    db.session.execute(text('''
                INSERT INTO posts (image_path, description, rating, identification, title, link) VALUES
                (:image_path, :description, 0, :result, :title, :link);
            ''').bindparams(image_path=image_path_url, description=post_description, result=result["identification"],
                            title=post_title, link=result["purchase_link"]))
    db.session.commit()
    result_json = json.dumps(result)

    return jsonify({"message": result})


@app.route('/get-posts', methods=['GET'])
def get_posts():

    with app.app_context():
        post_query = db.session.execute(text('''
            SELECT p.pid, p.image_path, p.description, p.rating
            FROM posts p 
            ORDER BY p.time DESC
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

    return jsonify({"posts": posts})


@app.route('/images/<path:filename>')
def get_image(filename):
    return send_from_directory('images', filename)


@app.route('/get-comments', methods=['GET'])
def get_comments():
    post_id = request.args.get('pid')

    with app.app_context():
        comment_query = db.session.execute(text('''
            SELECT c.cid, c.body
            FROM comments c
            WHERE c.post_id = :post_id
        ''').bindparams(post_id=post_id))

        rows = comment_query.fetchall()

        comments = [
            {
                "cid": row.cid,
                "body": row.body
            }
            for row in rows
        ]

    return jsonify({"comments": comments})

@app.route('/get-identification', methods=['GET'])
def get_identification():
    pid = request.args.get('pid')
    with app.app_context():
        identification_query = db.session.execute(text('''
            SELECT p.identification
            FROM posts p
            WHERE p.pid = :post_id
        ''').bindparams(post_id=pid))

        row = identification_query.fetchone()

    if row is None:
        return jsonify({"error": f"No post found with id {pid}"}), 404

    identification = row[0]
    return jsonify({"identification": identification})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
