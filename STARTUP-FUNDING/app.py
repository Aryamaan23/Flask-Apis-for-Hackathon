#from pip._vendor import requests
from flask import Flask,render_template,jsonify,request
import pandas as pd
import numpy as np
import joblib



app=Flask(__name__)
@app.route('/')

def home():
    return "Flask is being used for Development"

@app.route('/predict',methods=['GET','POST'])

def predict():
    if request.method=='POST':
        try:
            NewYork=float(request.form['NewYork'])
            California=float(request.form['California'])
            Florida=float(request.form['Florida'])
            RnDSpend=float(request.form['RnDSpend'])
            AdminSpend=float(request.form['AdminSpend'])
            MarketSpend=float(request.form['MarketSpend'])
            pred_args=[NewYork,California,Florida,RnDSpend,AdminSpend,MarketSpend]
            pred_args_arr=np.array(pred_args)
            pred_args_arr=pred_args_arr.reshape(1,-1)
            mul_reg=open("C:/Users/User/Downloads/multiple_linear_model.pkl","rb")
            ml_model=joblib.load(mul_reg)
            model_prediction=ml_model.predict(pred_args_arr)
            model_prediction=round(float(model_prediction),2)

            



        except ValueError:
            return "Please check if the values are entered correctly"

    return jsonify({'prediction':model_prediction})


    

if __name__=='__main__':
    app.run()

