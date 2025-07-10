from flask import Flask,render_template,session,request,redirect
from db import *
import requests
app=Flask(__name__)
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
API_URL2 = "https://api-inference.huggingface.co/models/dslim/bert-base-NER"
headers = {
    "Authorization": 123456#HuggingFace Token  #https://huggingface.co/settings/tokens
}
app.secret_key = "keysecrethai1234" #Secured  session
dbo=DataBase()
@app.route('/')
def login():
   return  render_template('index.html')
@app.route('/register') 
def register():
  return render_template('register.html')
@app.route('/login_process',methods=['get','post'])
def home(): 
   email=request.form.get('email')
   password=request.form.get('password')
   response=dbo.Search(email,password)
   if response:
      session['email'] = email
      return render_template('/home.html')
   else:
      return render_template('/index.html',message='Incorrect Email/Password')

@app.route('/register_process',methods=['get','post'])
def register_process(): #Perform Registration
   name=request.form.get('name')
   email=request.form.get('email')
   password=request.form.get('password')
   if dbo.insert(name,email,password):
      return render_template('index.html',message='Registration Succesfull!Kindly Login To Proceed')
   else:
      return render_template('register.html',message='Email Already Exists')
@app.route('/sentiment')  #Render Sentiment Page
def sentiment():
   if 'email' in session:
    return render_template('sentiment.html')
   else:
    return render_template('home.html')
@app.route('/perform_sentiment',methods=['get','post'])
def perform_sentiment():
  result = None
  label_map = {
    "LABEL_0": "NEGATIVE",
    "LABEL_1": "NEUTRAL",
    "LABEL_2": "POSITIVE"
}

  if request.method == 'POST':
    user_text = request.form.get('user_text', '')

    if user_text.strip():  
        response = requests.post(API_URL, headers=headers, json={"inputs": user_text})

        if response.status_code == 200:
            raw_result = response.json()[0][0]
            result = {
                "label": label_map.get(raw_result["label"], raw_result["label"]),
                "score": round(raw_result["score"] * 100, 2)
            }
        else:
            result = {"label": "Error", "score": 0.0}

  return render_template("sentiment.html", result=result)
@app.route('/ner')
def ner():
   if 'email' in session:
    return render_template('ner.html')
@app.route('/perform_ner',methods=['get','post'])
def perform_ner():
    result = []
    user_text = ""
    
    if request.method == 'POST':
        user_text = request.form.get('user_text', '')

        if user_text:
            
            headers = {
                "Authorization": "Bearer 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"
            }
            payload = {"inputs": user_text}
            response = requests.post(API_URL2, headers=headers, json=payload)

            if response.status_code == 200:
                result = response.json()
            else:
                result = [{"word": "API error", "entity_group": "Error", "score": 0}]
    
    return render_template('ner.html', result=result, user_text=user_text)

app.run(debug=True)