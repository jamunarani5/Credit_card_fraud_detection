from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_tree.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        normalizedAmount = int(request.form['normalizedAmount'])
   
        prediction=model.predict([[normalizedAmount]])
        
        if prediction<0:
            return render_template('index.html',prediction_texts="fraud")
        else:
            return render_template('index.html',prediction_text="not fraud")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)