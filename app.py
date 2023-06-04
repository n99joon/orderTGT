from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, world!')
    #return print("hello, world")

# # Temporary data store for user records
# users = []

# @app.route('/api/users', methods=['POST'])
# def create_user():
#     data = request.get_json()

#     if 'name' not in data or 'email' not in data:
#         return jsonify(message='Name and email are required.'), 400

#     name = data['name']
#     email = data['email']

#     # Create a new user record
#     user = {'name': name, 'email': email}
#     users.append(user)

#     return jsonify(message='User created successfully.', user=user), 201

#this function should return the names of all users in the array users.
#Finish this code.
@app.route('/api/getUsers', methods=['GET'])
def user():
    return
if __name__ == '__main__':
    app.run()