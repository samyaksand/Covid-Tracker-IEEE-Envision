import requests
import json
from flask import Flask, render_template

app = Flask(__name__)

# API - to access web data

url = 'https://www.mohfw.gov.in/data/datanew.json'

# perform GET request
res = requests.get(url)

# convert data into json
data = res.json()


@app.route('/')
def home_page():
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
