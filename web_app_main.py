# Bombastic Bookstore
# Flask Website v1

from Inventory_chart import generate_bar_chart
from flask import Flask, render_template, redirect, flash, url_for, request
from forms import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import User

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

FLASK_APP = 'web_app_main.py'

# Separate function for home page content
def get_home_content():
    return "Hello World! This is the starter version of our website <h1>HELLO<h1>"


# This function gives us the current "home" page
# This starter version runs locally, and the web browser URL is "http://127.0.0.1:5000/"
@app.route("/")
def home():
    # Render the home page content using the separate function
    content = get_home_content()
    # Change the file to see the changes in the file on the server
    return render_template("home.html", content=content)


# This is the v2 Login function.
# Currently entering anything in the user and password fields logs in a user.
# Leaving either/both fields blank gives an error message.
# Returning to the login page after having logged in shows the flash message.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Logged In! {}, remember_me={}'.format(
            form.username.data, form.remember_me))
        return redirect(url_for('profile'))
    return render_template('login.html', title='Sign In', form=form)


# This functions adds a placeholder profile page, accessed by logging in
@app.route("/profile")
def profile():
    return render_template('profile.html')

# This functions adds a placeholder display page, accessed by logging in
@app.route("/display")
def display():
    return render_template('display.html')

# This functions adds a placeholder display page, accessed by logging in
@app.route("/catalog")
def inventory():
    return render_template('catalog.html', data_type='catalog Page')

# Dictionary to cache generated bar chart images
chart_cache = {}

@app.route('/catalog/<data_type>')
def show_inventory(data_type):
    data = {
        'sales': 'This is the sales data.',
        'order': 'This is the Order page.',
        'inventory': 'This is the inventory data.'
    }
    if data_type == 'inventory':
        # Check if the chart is cached
        if 'inventory' in chart_cache:
            image_url = chart_cache['inventory']
        else:
            image_url = generate_bar_chart()
            chart_cache['inventory'] = image_url
        return render_template('catalog.html', data_type=data_type, image_url=image_url)

    return render_template('catalog.html', data_type=data_type, data=data.get(data_type, ''))

if __name__ == "__main__":
    app.run(debug=True)
