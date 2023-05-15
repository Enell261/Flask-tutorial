from flask import Flask, render_template
#initiate app flask incident
app = Flask(__name__)
#provide route
@app.route('/')
#define a function
def hello_world():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)