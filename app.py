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

@app.route('/login', methods=['POST'])
def login():
  return render_template('login.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)