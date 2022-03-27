from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash #para hashear la contrasena
from bson import json_util #para convertir la respuesta desde mongo en un json
from bson.objectid import ObjectId #para buscar en mongo con el id pasando de string a object

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/practica1db'

mongo = PyMongo(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    #return response si retorno asi se envia en formato string, abajo tiene formato json
    return Response(response, mimetype='application/json')

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({'messsage': ' User ' + id + ' was delete'})
    return response

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    if username and email and password:
        #por ahora validando que hay datos
        hashed_password = generate_password_hash(password)
        #escondiendo la contrasena
        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set':{
            'username': username,
            'password': hashed_password,
            'email': email
        }})
        response = jsonify({'messsage': ' User ' + id + ' was updated'})
        return response
    else:
        return not_found()

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