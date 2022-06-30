from markupsafe import escape
from decouple import config
from . import app
from flask import render_template

#get env vars
#sqlPass = config('SQLPASS')
#config MySQL DB
#username and password for database followed by url where it is hosted w/ name
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{sqlPass}@localhost/stockdata'

@app.route("/")
def index():
    user = {'username': 'Default'}
    return render_template('index.html', title='Home', user=user)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an int
    return f'Post{post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'
