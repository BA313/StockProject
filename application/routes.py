from markupsafe import escape
from . import app
from flask import render_template, flash, request, redirect, url_for
from .view.forms import LookUpForm

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

@app.route("/lookup", methods=['GET', 'POST'])
def lookup():
    form = LookUpForm()
    if form.is_submitted():
        print(form.validate())
        if(len(form.errors) < 2):
            form.errors.clear()
            if int(request.form.getlist('radio')[0]) == 1:
                flash(f'The Submitted ticker was {form.ticField.data}', 'Success')
            elif int(request.form.getlist('radio')[0]) == 2:
                flash(f'The Submitted ticker was {form.ticField2.data}', 'Success')
            return redirect(url_for('about'))
    #tickers need to be a list of dictionaries
    return render_template('lookup.html', title='Look Up', form=form)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an int
    return f'Post{post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    #show the subpath after /path/
    return f'Subpath {escape(subpath)}'
