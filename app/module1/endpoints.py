from app.module1 import bp
from flask import jsonify, request, session

# Import any models you are going to use here
# from app.models.model_file_name import model_name
# ...

# Import any extensions you are going to use here (Bcrypt, CORS, etc)
from app.extensions import db

# Test Route

@bp.route('/module1')
def module1():
    return "<h1>Hello from module 1!</h1>"
