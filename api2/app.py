from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Nicholas",
        "age": 42,
        "occupation": "Network Engineer"
    },
    {
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    },
]

# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''

class User(Resource):

    # See if user is in the system and return 
    def get(self, name):
        for user in users:
            if (name == user['name']):
                return user, 200
            else:
                return "User not found", 404

    # Hold parameter variables and if user not in users add to users
    # ADDS NEW USERS
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parser_args()

        for user in users:
            if (name == user['name']):
                return "User with name {} already exists".format(name), 400
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        users.append(user)
        return user, 201

    # Hold parameter variables and if name matches UPDATE the user
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parser_args()

        for user in users:
            if (name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, "/user/<string:name>")
app.run(debug=True)