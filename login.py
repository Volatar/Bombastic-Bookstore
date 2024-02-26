# This is version 2.2 of the login system
# Now in its own file to hopefully prevent a circular import error
# M.Wilamowski

from flask import render_template, redirect, url_for, flash
from web_app_main import app
from forms import LoginForm
from flask_login import current_user, login_user, logout_user
import sqlalchemy as SQLAlchemy
from web_app_main import db
from models import User

# this is the first attempt at resolving the circular import issue with models
# it currently does not work
# its commented out for now so it doesn't cause even more issues

#@app.route('/login', methods=['GET', 'POST'])
#def login():
    #if current_user.is_authenticated:
        #return redirect(url_for('profile'))
    #form = LoginForm()
    #if form.validate_on_submit():
        #user = db.session.scalar(
            #SQLAlchemy.select(User).where(User.username == form.username.data))
        #if user is None or not user.check_password(form.password.data):
            #flash('Invalid username or password')
            #return redirect(url_for('login'))
        #login_user(user, remember=form.remember_me.data)
        #return redirect(url_for('profile'))
    #return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))