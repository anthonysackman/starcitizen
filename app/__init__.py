from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

class User(Resource):
    def get(self, user_id):
        # return all users if no user_id
        return {user_id: "user_id_test"}

    def post(self, sc_username, discord_username):
        new_user = {
            "sc_username": sc_username,
            "discord_username": discord_username
        }
        # add user to db
        return new_user

api.add_resource(User, '/<string:user_id>')

class System(Resource):
    def get(self, system_name):
        return system_name
    
    def post(self, system_name, poi, system_type):
        new_system = {
            "system_name": system_name,
            "system_type": system_type,
            "poi": [poi]
        }
        return new_system 

api.add_resource(System, '/<string:todo_id>')

class Vehicle(Resource):
    def get(self, sehicle_name):
        return sehicle_name

api.add_resource(TodoSimple, '/<string:todo_id>')

class Item(Resource):
    def get(self, item_name):
        return item_name

api.add_resource(TodoSimple, '/<string:todo_id>')

class Commodity(Resource):
    def get(self, commodity_name):
        return commodity_name

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)