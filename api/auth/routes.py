# IMPORTS
from flask import Blueprint, jsonify

# DECLARATION
auth = Blueprint('auth', __name__)

# iNDEX PAGE ROUTE
@auth.route('/home')
def index():    
    return jsonify({'message': 'This is the Sloop API'})