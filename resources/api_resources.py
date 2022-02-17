from flask_restful import Resource
from flask import request,jsonify
from app import db
from models.api_models import *


def check_object(name):
    api = APIModel.query.filter_by(name=name).first()
    if api is not None:
        return api
    else:
        return {"Error": "Not found"}, 401




class ProductAPI(Resource):
    def get(self, name):
        api = check_object(name)
        serialized_result = jsonify(api_schema.dump(api))
        return serialized_result

    def post(self):
        data = request.get_json()
        name = data["name"]
        description = data["description"]
        price = data["price"]
        url_context = data["url_context"]
        end_points = data["end_points"]
        user_id = data["user_id"]
        new_api = APIModel(name=name, description=description, price=price,url_context=url_context,end_points=end_points,user_id=user_id)
        db.session.add(new_api)
        db.session.commit()
        return api_schema.jsonify(new_api)

    def put(self, name):
        api = check_object(name)
        data = request.get_json()
        api.name = data["name"]
        api.description = data["description"]
        api.price = data["price"]
        api.url_context = data["url_context"]
        api.end_points = data["end_points"]
        db.session.commit()
        return api_schema.jsonify(api)

    def delete(self, name):
        api = check_object(name=name)
        db.session.delete(api)
        db.session.commit()
        return {"deleted": "done"}, 200



class APIList(Resource):
    def get(self):
        api_list = APIModel.query.all()
        serialized_result = apis_schema.dump(api_list)
        return jsonify(serialized_result)