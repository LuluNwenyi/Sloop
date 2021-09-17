# IMPORTS
from flask import Blueprint, jsonify

# DECLARATION
default = Blueprint('default', __name__)

# iNDEX PAGE ROUTE
@default.route('/')
def index():    
    return jsonify({'message': 'This is the Sloop API'})