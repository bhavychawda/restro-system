from ensurepip import bootstrap
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('main.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='127.0.0.1', port=8000)