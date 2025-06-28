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
    user_role = data["user_role"]

    if email.strip() == "" or password.strip() == "" or user_role.strip() == "":
        return jsonify({"msg": "Invalid credentials"}),400
    
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"


    if re.match(pattern,email) is None:
        return jsonify({"msg":"Invalid credentials"}),400
    
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"msg":"the user already exists"}),409
    
    password_hashed = bcrypt.generated_password_hash(password).decode("utf-8")

    new_user = User()
    
