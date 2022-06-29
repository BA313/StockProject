from flask import Flask
from markupsafe import escape
from decouple import config


#get env vars
#sqlPass = config('SQLPASS')
#app = Flask(__name__)
#config MySQL DB
#username and password for database followed by url where it is hosted w/ name
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{sqlPass}@localhost/stockdata'

@app.route("/")
def index():
    return "<p>Index Page</p>"

@app.route("/hello")
def hello():
    return "<p>Hello World</p>"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an int
    return f'Post{post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'

