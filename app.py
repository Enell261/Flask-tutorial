from flask import Flask, render_template, redirect, request,url_for

username_1 = 'm5388392'
password_1 = '1234567'

#initiate app flask incident
app = Flask(__name__)
#provide route
@app.route('/', methods = ['GET','POST'])
#define a function
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    if username == username_1 and password == password_1:
      return redirect(url_for('search'))
    else:
      return render_template('login.html', error = 'Invalid login credentials')
      
  return render_template('login.html')
@app.route('/search')
def search():
  return render_template('search.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)