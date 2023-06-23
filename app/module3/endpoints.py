from app.module3 import bp
from flask import jsonify, request, session

# Import any models you are going to use here
# from app.models.model_file_name import model_name
# ...

# Import any extensions you are going to use here (Bcrypt, CORS, etc)
from app.extensions import db

# Test Route

@bp.route('/module3')
def module3():
    return "<h1>Hello from module 3!</h1>"
