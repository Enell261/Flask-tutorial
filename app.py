from flask import Flask

#initiate app flask incident
app = Flask(__name__)
#provide route
@app.route('/')
#define a function
def hello_world():
  return "Hi Senhle"

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)