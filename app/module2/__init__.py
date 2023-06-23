# This file is usually not modified. 
# It is used to initialize the module and import the endpoints.

from flask import Blueprint

# Creating a Blueprint
bp = Blueprint('module2', __name__)

# Importing the endpoints
from app.module2 import endpoints