# IMPORTS
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from werkzeug.security import generate_password_hash
from api.models import User
from api.decorators import admin_required
from api import db,  ACCESS_EXPIRES
import uuid

# DECLARE BLUEPRINT
user = Blueprint('user', __name__)

# CREATE USER
@user.route('/sign-up', methods=['POST'])
def create_user():

    # QUERY IF USER EXISTS
    user = User.query.filter_by(email=request.json['email']).first()

    if not user:

        try:
            # REGISTER THE USER
            username = request.json['username']
            email = request.json['email']
            password = request.json['password']
            password = generate_password_hash(password)

            new_user = User(username=username, email=email, password=password, admin=False, creator=False,  public_id=str(uuid.uuid4()))  

            db.session.add(new_user)
            db.session.commit()

            response = {
                "message" : "You have registered this user successfully!"
            }

            return jsonify(response), 201

        except Exception as e:
            # IF ERROR OCCURED...
            response = {
                "message": str (e)
            }
            return jsonify(response), 400

    else:
        # IF USER ALREADY EXISTS
        response = {
            'message' : 'This user already exists.'
        }
        return jsonify(response), 409



# GET USER BY ID
@user.route('/user/<public_id>', methods=['GET'])
@jwt_required()
@admin_required
def get_user(public_id):

    # GET THE USER
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'User not found'}), 404

    else:
        response = {
            'username' : user.username,
            'email' : user.email,
            'admin' : user.admin,
            'display_name' : user.display_name,
            'creator' : user.creator,
            'public_id' : user.public_id
        }
        return jsonify(response), 200



# GET ALL USERS
@user.route('/users', methods=['GET'])
@admin_required
def get_all_users():

    # GET ALL THE USERS
    users = User.query.all()

    if not users:
        return jsonify({'message' : 'No users found'}), 404

    else:
        response = []
        for user in users:
            response.append({
                'username' : user.username,
                'email' : user.email,
                'display_name' : user.display_name,
                'admin' : user.admin,
                'creator' : user.creator,
                'public_id' : user.public_id
            })
        return jsonify(response), 200



# EDIT USER
@user.route('/user/<public_id>', methods=['PUT'])
@admin_required
def edit_user(public_id):

    # GET THE USER
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'User not found'}), 404

    else:
        try:
            # EDIT THE USER
            username = request.json['username']
            email = request.json['email']

            user.username = username
            user.email = email

            db.session.commit()

            response = {
                "message" : "You have edited this user successfully!"
            }

            return jsonify(response), 201

        except Exception as e:
            # IF ERROR OCCURED...
            response = {
                "message": str (e)
            }
            return jsonify(response), 400



# PROMOTE USER TO CREATOR
@user.route('/user/<public_id>', methods=['PATCH'])
@admin_required
def promote_user(public_id):

    # GET THE USER
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'User not found'}), 404

    else:
        try:
            # EDIT THE USER
            user.creator = True

            db.session.commit()

            response = {
                "message" : "You have promoted this user to creator successfully!"
            }

            return jsonify(response), 201

        except Exception as e:
            # IF ERROR OCCURED...
            response = {
                "message": str (e)
            }
            return jsonify(response), 400



# DELETE USER
@user.route('/user/<public_id>', methods=['DELETE'])
@admin_required
def delete_user(public_id):

    # GET THE USER
    user = User.query.filter_by(public_id=public_id).first()

    if not user:
        return jsonify({'message' : 'User not found'}), 404

    else:
        try:
            # DELETE THE USER
            db.session.delete(user)
            db.session.commit()

            response = {
                "message" : "You have deleted this user successfully!"
            }

            return jsonify(response), 201

        except Exception as e:
            # IF ERROR OCCURED...
            response = {
                "message": str (e)
            }
            return jsonify(response), 400