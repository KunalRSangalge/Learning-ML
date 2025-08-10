from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def display():
    return "<html><h1>Hi im kunal, this is my first web display using HTML</h1></html>"

@app.route("/amazon")
def amazon():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)