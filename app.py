import requests, json
from flask import Flask, render_template

app=Flask(__name__)


url = 'https://www.mohfw.gov.in/data/datanew.json'

res = requests.get(url)

data = res.json()

@app.route('/')
def home_page():
    return render_template('index.html', data = data)

if __name__=="__main__":
    app.run(debug=True)