from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=['GET'])
def welcome():
    return render_template('index.html')

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route("/submit",methods=['GET','POST']) #this is /submit which will execute because in html action="/submit"
def submit():
    return f"fhhgeprgherger"

if __name__ == "__main__":
    app.run(debug=True)