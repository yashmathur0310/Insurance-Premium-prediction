from flask import Flask,render_template,request
import pickle
model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        age=int(request.form['age'])
        sex=request.form['Sex']
        if(sex=='female'):
            sex=0
        else:
            sex=1
        bmi=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        if(smoker=='no'):
            smoker=0
        else:
            smoker=1
        region=request.form['region']
        if(region=='northeast'):
            region_northeast=1	
            region_northwest=0	
            region_southeast=0	
            region_southwest=0
        elif(region=='northwest'):
            region_northeast=0	
            region_northwest=1	
            region_southeast=0	
            region_southwest=0
        elif(region=='southeast'):
            region_northeast=0	
            region_northwest=0	
            region_southeast=1	
            region_southwest=0
        elif(region=='southwest'):
             region_northeast=0	
             region_northwest=0	
             region_southeast=0	
             region_southwest=1
        else:
             region_northeast=0	
             region_northwest=0
             region_southeast=0	
             region_southwest=0

        prediction=model.predict([[age,sex,bmi,smoker,children,region_northeast,region_northwest,region_southeast,region_northwest]])
        return render_template('result.html',prediction_text=prediction)







if __name__=='__main__':
    app.run(debug=True)