import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request,jsonify

application = Flask(__name__)
app = application

ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata',methods=['GET','POST'])
def predictdata():
    if request.method == "POST":
        Temparature = float(request.form.get('Temparature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        data_scaled = standard_scaler.transform([[Temparature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(data_scaled)

        return render_template('home.html',results = result[0])
    else:
        return render_template('home.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)