from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_customer():  
  if request.method == 'POST':    
    customer_id = request.form['customer_id']
    data = get_customer_data(customer_id)
    return render_template('results.html', data=data)
  return render_template('search.html')

def get_customer_data(customer_id):
  # Read the Excel file using Pandas
  df = pd.read_excel('https://flask-tutorial--enell261.repl.co/static/20230512.xlsx')

  # Filter the data based on the customer identifier
  customer_data = df[df['CustomerID'] == customer_id]

  # Convert the filtered data to a dictionary or any other     desired format
  data = customer_data.to_dict('records')

  return data

if __name__ == '__main__':
  app.run()