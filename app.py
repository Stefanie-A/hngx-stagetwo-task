from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
load_dotenv()

db_password = os.environ['DATABASE_PASSWORD']
db_host = os.environ['DATABASE_HOST']
db_user = os.environ['DATABASE_USER']

var = os.getenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:25060/defaultdb"
db = SQLAlchemy(app)
migate = Migrate(app, db)

class Person(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    gender = db.Column(db.String())

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

@app.route('/api', methods=['POST', 'GET'])
def handle_user():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = Person(first_name=data['first_name'], last_name=data['last_name'], gender=data['gender'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.name} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}
        
    elif request.method == 'GET':
        user= Person.query.all()
        results = [
            {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "gender": user.gender,
            } for users in user]

        return {"users": results}
    
@app.route('/api/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_users(user_id):
    user = Person.query.get_or_404(user_id)
    if request.method == 'GET':
        response = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "gender": user.gender,
        }
        return {"message": "success", "user": response}
    elif request.method == 'PUT':
        data = request.get_json()
        user.first_name = data['first_name']
        user.last_name =data['last_name']
        user.gender = data['gender']
        db.session.add(user)
        db.session.commit()
        return {"message": f"user {user.first_name} {user.last_name} successfully updated"}
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"user {user.first_name}  {user.last_name} successfully deleted."}
if __name__ == "__main__":   
    app.run(debug=True)
