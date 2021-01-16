from flask import Flask,render_template,jsonify,request,redirect
import pickle
import numpy as np
app=Flask(__name__)

loaded_model=pickle.load(open("C:/Users/User/Downloads/finalized_model.sav","rb"))

@app.route("/predict",methods=['GET','POST'])
def home():
    new=''
    if request.method=='POST':
         
        int_features = [float(x) for x in request.form.values()]
        final_features =[np.array(int_features)]
        #final_features=final_features.reshape(1,-1)
        prediction=loaded_model.predict(final_features)
        """
        
        revolvingutilizationofunsecuredlines=int(request.form['revolvingutilizationofunsecuredlines'])
        age=int(request.form['age'])
        numberoftime3059dayspastduenotworse =int(request.form['numberoftime3059dayspastduenotworse '])
        debtratio=int(request.form['debtratio'])
        monthlyincome  =int(request.form['monthlyincome'])
        numberofopencreditlinesandloans=int(request.form['numberofopencreditlinesandloans'])
        numberoftimes90dayslate=int(request.form['numberoftimes90dayslate'])
        numberrealestateloansorlines=int(request.form['numberrealestateloansorlines'])
        numberoftime6089dayspastduenotworse=int(request.form['numberoftime6089dayspastduenotworse'])
        numberofdependents=int(request.form['numberofdependents'])
        pred_args=[revolvingutilizationofunsecuredlines,age,numberoftime3059dayspastduenotworse,debtratio,monthlyincome,numberofopencreditlinesandloans,numberoftimes90dayslate, numberrealestateloansorlines,numberoftime6089dayspastduenotworse,numberofdependents]
        pred_args_arr=[np.array(pred_args)]
        #pred_args_arr=pred_args_arr.reshape(1,-1)
        #loaded_model=pickle.load(open("C:/Users/User/Downloads/finalized_model.sav","rb"))
        #prediction=loaded_model.predict(pred_args_arr)
        #prediction=round(float(prediction),2)
        
        int_features = [int(x) for x in request.form.values()]
        final_features =[np.array(int_features)]
        #final_features=final_features.reshape(1,-1)
        prediction=loaded_model.predict(final_features)
        """
        
        if prediction==1:
           new='Your loan application is selected'
        else:
           new='Your loan application is not selected'

    return jsonify({"Loan Prediction":new})

if __name__=='__main__':
    app.run(debug=True)

