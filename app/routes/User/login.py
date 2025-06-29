from flask import request,jsonify
from app.models import db
from app.models.user import User
from main import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()



@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()