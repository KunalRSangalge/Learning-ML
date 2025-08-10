from flask import Flask
# Creating an instance of Flask class which will act as
# WSGI(web server gateway interface) app
app = Flask(__name__)

@app.route("/") #when user hits this in url , this route will be called
def welcome():
    return "Welcome to the Flask App,Im kunal!"

@app.route("/index") #when user hits this in url , this route will be called
def index():
    return "Welcome to the index of the flask app!"
if __name__ == "__main__":
    app.run(debug=True) #debug = True will reload the server automatically
