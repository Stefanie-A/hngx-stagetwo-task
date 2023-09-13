from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db_password = os.environ["DATABASE_PASSWORD"]
db_host = os.environ["DATABASE_HOST"]
db_user = os.environ["DATABASE_USER"]
db_port = os.environ["DATABASE_PORT"]

var = os.getenv(".env")

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/defaultdb"
db = SQLAlchemy(app)
migate = Migrate(app, db)


class Person(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name


@app.route("/api/", methods=["POST", "GET"])
def handle_user():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            if not "name" in data:
                return {"error": "name parameter required"}, 400
            if not isinstance(data["name"], str):
                return {"error": "name must be a string"}, 400

            exists = (
                db.session.query(Person.id).filter_by(name=data["name"]).first()
                is not None
            )
            if exists:
                return {"error": f"User {data['name']} already exists"}, 400
            new_user = Person(name=data["name"])
            db.session.add(new_user)
            db.session.commit()
            return {
                "message": f"user {new_user.name} has been created successfully."
            }, 201
        else:
            return {"error": "The request payload is not in JSON format"}, 400

    elif request.method == "GET":
        users = Person.query.all()
        results = [{"id": user.id, "name": user.name} for user in users]

        return {"users": results}


@app.route("/api/<user_id>/", methods=["GET", "PUT", "DELETE"])
def handle_users(user_id):
    user = Person.query.filter_by(id=user_id).first()
    if user is None:
        return {"error": f"user with id {user_id} not found"}, 404
    if request.method == "GET":
        response = {"id": user.id, "name": user.name}
        return {"message": "success", "user": response}
    elif request.method == "PUT":
        data = request.get_json()
        if not "name" in data:
            return {"error": "name parameter required"}, 400
        if not isinstance(data["name"], str):
            return {"error": "name must be a string"}, 400
        user.name = data["name"]
        db.session.add(user)
        db.session.commit()
        return {
            "message": f"user {user.name} successfully updated",
        }
    elif request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return {"message": f"user {user.name} successfully deleted."}, 200


if __name__ == "__main__":
    app.run(debug=True)
