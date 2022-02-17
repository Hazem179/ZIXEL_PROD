from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


######### APP CONFIGRATIONS #########
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:251hazem179@localhost/zixel_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
db = SQLAlchemy(app)
Migrate(app,db,render_as_batch=True)
api = Api(app)
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

######### PRODUCT SOFTWARE ENDPOINTS #########
from resources.sw_resources import *
api.add_resource(ProductSoftware,'/software/<string:name>','/software')
api.add_resource(SoftwareList,'/software_list')

######### PRODUCT API ENDPOINTS #########
from resources.api_resources import *
api.add_resource(ProductAPI,'/api/<string:name>','/api')
api.add_resource(APIList,'/api_list')


######### USER ENDPOINTS #########
from resources.user_resources import *
api.add_resource(PlatformUser,'/user/<string:name>','/user')
api.add_resource(UserList,'/user_list')


if __name__ == '__main__':
    app.run()

