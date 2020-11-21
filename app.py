from os import abort
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('dashboard.html')


@app.route('/info')
def detect():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()
