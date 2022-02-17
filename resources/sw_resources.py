from flask import jsonify,request
from flask_restful import Resource
from app import db
from models.sw_models import SoftwareModel,sws_schema,sw_schema


def check_object(name):
        software = SoftwareModel.query.filter_by(name=name).first()
        if software is not None:
            return software
        else:
            return {"Error":"Not found"},401


class ProductSoftware(Resource):
    def get(self,name):
        software = check_object(name)
        serialized_result = jsonify(sw_schema.dump(software))
        return serialized_result

    def post(self):
        data = request.get_json()
        name = data["name"]
        description = data["description"]
        price = data["price"]
        user_id = data["user_id"]
        new_software = SoftwareModel(name=name,description=description,price=price,user_id=user_id)
        db.session.add(new_software)
        db.session.commit()
        return sw_schema.jsonify(new_software)

    def put(self,name):
        software = check_object(name)
        data = request.get_json()
        software.name = data["name"]
        software.description = data["description"]
        software.price = data["price"]

        db.session.commit()
        return sw_schema.jsonify(software)

    def delete(self,name):
        software = check_object(name = name)
        db.session.delete(software)
        db.session.commit()
        return {"deleted":"done"},200

class SoftwareList(Resource):
    def get(self):
        software_list = SoftwareModel.query.all()
        serialized_result = sws_schema.dump(software_list)
        return jsonify(serialized_result)




