from flask import Flask,render_template,request
import numpy as np
import pickle
app=Flask(__name__)
model=pickle.load(open('modelfffp.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    print(int_features)
    final_features=np.array(int_features).reshape(1,11)
    print(final_features)
    output=model.predict(int_features)
    output=output.item()
    output=round(output,2)
    return render_template('result.html',prediction_text='flight fare is {}'.format(output))

if __name__=='__main__':
    app.run(port=8000)        