from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/practica1db'

mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    #atrapando los datos de request
    if username and email and password:
        #por ahora validando que hay datos
        hashed_password = generate_password_hash(password)
        #escondiendo la contrasena
        id = mongo.db.users.insert_one({'username': username, 'email': email, 'password': hashed_password})
        #guardando los datos del request
        response = {
            'id': str(id),
            'username': username,
            'email': email,
            'password': hashed_password
        }
        return response
    else:
    #    return {'message': 'not received'}
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = jsonify({
    'message': 'Resource Not Found: ' + request.url,
    'status': '404'
    })
    message.status_code=404
    return message
if __name__=="__main__":
	app.run(debug=True)