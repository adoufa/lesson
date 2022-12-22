from flask import Flask
from flask import render_template , url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Buy')
def index2():
    return render_template("index2.html")


@app.route('/holl')
def index3():
    return render_template("index3.html")


if __name__=='__main__':
    app.run(debug=True)