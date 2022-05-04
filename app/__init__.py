from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from app.models import user_account
from flask_migrate import Migrate
from app.models import db
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

db.init_app(app)
migrate = Migrate(app, db)

class User(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('sc_username', type=str, help='Star Citizen Username')
        self.parser.add_argument('dc_username', type=str, help='Discord Username')

    def get(self, user_id):
        # return all users if no user_id
        logging.info("get user")
        return {"user_id_test": user_id}

    def post(self):
        logging.debug(request.json)
        args = self.parser.parse_args()
        sc_user = request.json['sc_username']
        dc_user = request.json['dc_username']
        # add user to db
        created_user = user_account(sc_username=sc_user, dc_username=dc_user)
        logging.info('Created User: ', created_user)
        return created_user



class System(Resource):
    def get(self, system_name):
        return {"system_name": system_name}
    
    def post(self, system_name, poi, system_type):
        new_system = {
            "system_name": system_name,
            "system_type": system_type,
            "poi": [poi]
        }
        return new_system 


class Vehicle(Resource):
    def get(self, vehicle_name):
        return {"vehicle_name": vehicle_name}

class Item(Resource):
    def get(self, item_name):
        return {"item_name": item_name}

class Commodity(Resource):
    def get(self, commodity_name):
        return {"commodity_name": commodity_name}

api.add_resource(Commodity, '/commodity/<string:commodity_name>')
api.add_resource(Item, '/item/<string:item_name>')
api.add_resource(Vehicle, '/vehicle/<string:sehicle_name>')
api.add_resource(System, '/system/<string:system_name>')
api.add_resource(User, '/user/<int:user_id>', '/user/create')

if __name__ == '__main__':
    app.run(debug=True)