from flask import request,jsonify
from app.models import db
from app.models.user import User
from main import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

@app.route("/register",methods=["POST"])
def register():
    data = request.get_json()

    if data is None:
        return jsonify({"msg":"Invalid credentials"}),400
    
    email = data["email"]
    password = data["password"]
    user_type = data["user_type"]

    if email.strip() == "" or password.strip() == "" or user_type.strip() == "":
        return jsonify({"msg": "Invalid credentials"}),400
    
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"


    if re.match(pattern,email) is None:
        return jsonify({"msg":"Invalid credentials"}),400
    
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"msg":"the user already exists"}),409
    
    password_hashed = bcrypt.generated_password_hash(password).decode("utf-8")

    new_user = User(name=None,email = email, password = password_hashed, user_type= user_type,last_login_at = None, avatar_url = False, email_verified_at = None,bio = None)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg":"The user registered successfully"}),201
    
