from flask import Flask, jsonify #imports the Flask class (a web application framework for Python that allows developers to build web applications in a flexible and modular way through a range of tools and utilities for handling HTTP requests and responses, routing requests to the appropriate functions, and managing application state. ) and the jsonify function (that allows developers to easily convert Python objects to JSON format, which can be sent as a response to client requests) from the Flask module/library)

app = Flask(__name__) #creates a new instance of the Flask class and assigns it to the variable "app".

@app.route('/api/hello', methods=['GET'])  #defines a route for the Flask application using the @app.route() decorator. The route is specified as "/api/hello" and the HTTP method used to access the route is defined as "GET".
def hello():
    return jsonify(message='Hello, world!')   #defines a function named "hello" that returns a JSON response using the jsonify function provided by the Flask web application framework.
    #return 'Hello World!'

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
# @app.route('/api/getUsers', methods=['GET'])
# def user():
#     return

if __name__ == '__main__':
    app.run()  #starts the Flask web application if the script is executed directly, rather than imported as a module.                    