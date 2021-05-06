from flask import Flask, render_template

app=Flask(__name__)

# web scarping...

data = {

    'total': 300,
    'active': 200,
    'recover': 100,

}

@app.route('/')
def home_page():
    return render_template('index.html', data = data)

if __name__=="__main__":
    app.run(debug=True)