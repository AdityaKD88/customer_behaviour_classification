from flask import Flask, render_template, request
from joblib import load
import numpy as np
app = Flask(__name__)

load_model = load('app/static/model.pk')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        age = request.form.get('age')
        inc = request.form.get('inc')
        score = request.form.get('score')
        #print(age,inc,score)
        inp=np.array([age,inc,score]).reshape(1,-1)
        pred=load_model.predict(inp)[0]
        #print(pred)
        if pred==0:
            output='Customers with low income & low spenditure'
        elif pred==1:
            output='Customers with high income & high spenditure'
        elif pred==2:
            output='Customers with medium income & medium spenditure'
        elif pred==3:
            output='Customers with high income & low spenditure'
        elif pred==4:
            output='Customers with low income & high spenditure'
        return render_template('index.html',output=output)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)