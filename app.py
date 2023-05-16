import flask
from flask import Flask, render_template, flash, redirect, request, session, abort
import os

#initiate app flask incident
app = Flask(__name__)
#provide route
@app.route('/')
#define a function
def hello_world():
  return render_template('home.html')

@app.route('/login', methods=['POST','GET'])
def login():
  if request.method=="POST":
    #Get the submitted m-number
    m_number = request.form.get('m-number')
    #Check m-number against approved m-numbers
    #Add logic here
    #Redirect user to the next page (UCN page)
    return redirect(url_for('dashboard'))
  return render_template('login.html')
@app.route('/dashboard')
def dashboard():
  return render_template('dashboard.html')
    
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)