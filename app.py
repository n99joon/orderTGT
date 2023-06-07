from flask import Flask, jsonify, request   #This is to import the Flask(Main class/application in the flask module that allows for the creation of routes and handling requests) and jsonify(helper function to convert python objects into JSON format allowing data communication in web applications. Also used to generate JSON responses in flask routes)objects from the Flast module,

app = Flask(__name__)   #Creation of an instance of the Flask application with the name of the current module - it is basically representing my flask application
                        #Each flask application is a representation of a seperate running application based on the name of the module that would have been used as an argument to the Flask function
                        #This instance allows for the configuration of database connections and secret keys, rmb its a web application that we want people to be able to access.
                        #The root path to the application can be determined by this instance allowing this app to be run.

@app.route('/api/hello', methods=['GET'])   #This is a decorator and specifies a URL to associate with a specific function
                                            #@app.route is the decorator used to define a route for the flask application
                                            #'/api/hello' is used to specify the endpoint of a route or url route. A specific location that clients can access to interact with my web application
                                            #methods = ['GET'] is an argument specifying the HTTPs method allowed for this route allowing GET requests to be accepted by default
                                            #Get request retrieves data from a specific server and this allows a web browser to send a get request our server and  retrieve resourse that is represented by the url that it then display on the web browser
def hello():
    return jsonify(message='Hello, world!')     #jsonify takes a python object and returns a json response and the python object can be a list, dictionary or string
                                                  #message = Hello World is a key value pair that creates a dictionary upon being passed into the jsonify
                                                #return - returns the JSON respones generated by the jsonify function. Creates a jsonify object with the provided key value pair and sends response to the clien
                                                
    #return 'Hello World!'

# Temporary data store for user records
users = []

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()

    if 'name' not in data or 'email' not in data:
        return jsonify(message='Name and email are required.'), 400                         #400 is an HTTP status code that indicates a bad request and that the server is unable to process the request because of some error originating from the client side-web browser. The error message is embedded in the JSON object
                                                                                            #Returning a different status code will not affect the app's running from a technical standpoint but might cause confusion especially with troubleshooting as there will be contradiction between the actual source of error/request outcome and what is being reported by the https status code.

    name = data['name']
    email = data['email']

    # Create a new user record
    user = {'name': name, 'email': email}
    users.append(user)

    return jsonify(message='User created successfully.', user=user), 201

# this function should return the names of all users in the array users.
# Finish this code.
@app.route('/api/getUsers', methods=['GET'])
def user():
    print(users)
    names = [user['name'] for user in users]
    return jsonify(names=names)

if __name__ == '__main__':      #Used to check if the name of the current module is equal to main and if true, the current script will be run as the main entry point
                                #You will find script that will only be run if the current module is being run as the main script and when the script is being run directly and not when it has been imported as a module
    app.run()                   #Used to start the flask development server(built in serve provided by flask) and run your flask application locally on your machine
                                #This automatically associates the development server to the IP address 127.0.0.1(local host) and a port number of 5000 allowing your flask app to be accessible at that address
                                #Once the server starts, it will listen in for any HTTPS requests on port 5000 and will forward any requests to my FLASK application for processing allowing the app to generate a response as per configuration and then sending it back to the server for it be relayed to the client/web browser
                                #Process is repeated

# QUESTION 1
#So basic procedure is 1. Import the modules and the classes you need for making a Web App. 2. Create the app instance using the module of interest. 3. Define the route to the app together with the access url and default http function to be associated with that url. 4. Define a function that dictates what the app is going to do when accessed. 5. Conditional statement to allow the app to run if the current module is the main module
#http://localhost:5000/api/hello means that your own local computer is housing the flask development server and therefore our app is sitting on our local machine and thus we are able to access it on port 5000
#local address is valid only for the local machine and other people will not be able to access my app because if they type in localhost on their machines, it will be referring to their own machines and not mine.
#I would need to provide them with the network IP address of my machine for them to access the app thus allowing incoming connections from the internet.

#QUESTION 2:
# return Jsonify returns {"message":"Hello, world!"} on a black background
# return hello world returns the string hello world
#HTTP(HyperText Transfer Protocol) is a protocol used for web communication between a server and a client and this protocol defines the structure and format of the communication
#HTTP Request is sent by the client to the server to retrieve data or manipulate resources
#HTTP Response is sent by the server back to the client to respond to a request
#Jsonify should be used when there is need to transmit structured data between client and server and situations where API will be in use and a string should be used when the web page is a simple one that is returning an information text


#QUESTION 3:
#You'll get the following error: Method Not Allowed "The method is not allowed for the requested URL"
#This is because when you type in a url in a browser, the browser by default sends a GET request
#Few differences between post and get! Get is for retrieving data from a server and navigating between pages, data is visible in the url, can be bookmarked in browser, data is sent in the url parameters
#For a post function, it submits data to be processed by the server and usually modifies the resource in question, data is sent in the body of the request and not visible in the URL, cannot be bookmarked and reloading the page will prompt a resubmission of the POST request, secure and used for submitting forms

#Question 4:
#JSON payload is data transmitted between systems or applications using the JSON format which is a light weight data interchange format that is widely used for structured data representation
#JSON consists of a collection of  key-value pairs where the keys are strings and the values can be various data types like stings, numbers, booleans and arrays.
#JSON payload represents the actuad data that is being sent e.g user info and config settings
#You need to use postman or curl to send post data to our server. curl is preinstalled on my mac
#curl --help is the command that will give you info on all the availabe options you have 
#curl --data <data> url is basically the format that you use if you want to send data to our server
#Initially got an error saying the name request is not defined so I will import it from the flask module



#Question 5:
#Managed to return a list of all the names created by using the get function
