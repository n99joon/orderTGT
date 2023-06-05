from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, world!')

# Temporary data store for user records
users = []

@app.route('/api/users', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data or 'email' not in data:
            return jsonify(message='Name and email are required.'), 400

        name = data['name']
        email = data['email']

        # Create a new user record
        user = {'name': name, 'email': email}
        users.append(user)

        return jsonify(message='User created successfully.', user=user), 201
    
    elif request.method == 'GET':
        return jsonify(users=users)

@app.route('/api/getUsers', methods=['GET'])
def get_users():
    return jsonify(users=users)

if __name__ == '__main__':
    app.run()