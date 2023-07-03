from flask import Flask, jsonify, request
import os
import psycopg2

app = Flask(__name__)

# Establish a connection to the Heroku Postgres database
db_url = os.environ.get('DATABASE_URL')
db = psycopg2.connect(db_url)

# Create a cursor to interact with the database
cursor = db.cursor()

# Create the users table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
)
'''
cursor.execute(create_table_query)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, world!')

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if 'name' not in data or 'email' not in data:
        return jsonify(message='Name and email are required.'), 400

    name = data['name']
    email = data['email']

    # Insert the new user into the database
    insert_query = 'INSERT INTO users (name, email) VALUES (%s, %s)'
    values = (name, email)
    cursor.execute(insert_query, values)
    db.commit()

    # Get the inserted user's ID
    cursor.execute('SELECT lastval()')
    user_id = cursor.fetchone()[0]

    # Create a new user record
    user = {'id': user_id, 'name': name, 'email': email}

    return jsonify(message='User created successfully.', user=user), 201

@app.route('/api/getUsers', methods=['GET'])
def get_users():
    # Retrieve all users from the database
    select_query = 'SELECT * FROM users'
    cursor.execute(select_query)
    result = cursor.fetchall()

    if len(result) == 0:
        return jsonify(message='No users found.')

    # Extract user names from the result
    user_names = [user[1] for user in result]

    return jsonify(users=user_names)

if __name__ == '__main__':
    app.run()
