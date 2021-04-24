from flask import Flask, request
import pickle
import numpy as np
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
model = pickle.load(open('model (4).pkl', 'rb'))
@app.route('/')
def hello():
    return '<h1>This is a diabsetes predictor</h1>'

# prediction function   
@app.route('/predict', methods = ['POST'])
@cross_origin() 
def predict(): 
    A = [float(x) for x in request.form.values()]
    model_probability = model.predict_proba([A])
    prediction = "Probability of  this user having Diabetes is %0.2f"%model_probability[0][1]
    return ({"Prediction":prediction})

if __name__ == "__main__":
    app.run(debug=True)