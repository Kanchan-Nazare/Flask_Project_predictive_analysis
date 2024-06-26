from flask import Flask,render_template,request
import sklearn
import pickle
import sys
print(sys)

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data=request.form
    print(data)
    load_model=pickle.load(open('iris.pkl','rb'))
    print(load_model)


    user_data=[[float(data['x1_sepal_length']),
                float(data['x2_sepal_width']),
                float(data['x3_petal_length']),
                float(data['x4_petal_width'])
                ]]
    print(user_data)

    result=load_model.predict(user_data)
    print(result)

    target=['setosa', 'versicolor', 'virginica']

    print(f"Prediction= {target[result[0]]}")

    return target[result[0]]

app.run(host='0.0.0.0',debug=False,port=8080)
    
