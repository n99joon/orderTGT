from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, world!')

# Temporary data store for user records
users = []

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if 'name' not in data or 'email' not in data:
        return jsonify(message='Name and email are required.'), 400

    name = data['name']
    email = data['email']

    # Create a new user record
    user = {'name': name, 'email': email}
    users.append(user)

    return jsonify(message='User created successfully.', user=user), 201

@app.route('/api/getUsers', methods=['GET'])
def get_users():
    if len(users) == 0:
        return jsonify(message='No users found.')
    
    user_names = [user['name'] for user in users]
    return jsonify(users=user_names)

if __name__ == '__main__':
    app.run()
