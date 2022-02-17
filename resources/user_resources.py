from app import db
from flask_restful import Resource,request
from flask import jsonify
from models.user_models import *


class PlatformUser(Resource):
    def get(self,name):
        user = UserModel.query.filter_by(user_name=name).first()
        serialized_result = jsonify(user_schema.dump(user))
        return serialized_result
    def post(self):
        data = request.get_json()
        user_name = data["username"]
        user_type = data["usertype"]
        user_description=data["description"]
        new_user = UserModel(user_name=user_name,user_type=user_type,user_description=user_description)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.jsonify(new_user)
    def put(self,name):
        user = UserModel.query.filter_by(user_name=name).first()
        data = request.get_json()
        user.user_name = data["username"]
        user.user_type = data["usertype"]
        user.user_description = data["description"]
        db.session.commit()
        return user_schema.jsonify(user)

    def delete(self,name):
        user = UserModel.query.filter_by(user_name=name).first()
        db.session.delete(user)
        db.session.commit()
        return {"deleted":"done"},200



class UserList(Resource):
    def get(self):
        users_list = UserModel.query.all()
        serialized_result = users_schema.dump(users_list)
        return serialized_result
