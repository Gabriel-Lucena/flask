
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
#from flask_moment import Moment
#from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
#moment = Moment(app)

@app.route('/')
def index():
    return render_template('base.html')

#@app.route('/user/<name>')
#def name(name):
#    return render_template('user.html', name=name)