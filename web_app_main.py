# Bombastic Bookstore
# Flask Website v1

import secrets
import sqlite3, requests
from Inventory_chart import generate_bar_chart
from flask import Flask, render_template, session, redirect, flash, url_for, request
from forms import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import User

app = Flask(__name__)

# Set the database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

# Generate a secure random key for session security
app.secret_key = secrets.token_hex(16)  # 16 bytes (128 bits) is a common key length

db = SQLAlchemy(app)
migrate = Migrate(app, db)

FLASK_APP = 'web_app_main.py'

# Dictionary to cache generated bar chart images
chart_cache = {}


# Separate function for home page content
def get_home_content():
    return "Hello World! This is the starter version of our website <h1>HELLO<h1>"


# This function gives us the current "home" page
# This starter version runs locally, and the web browser URL is "http://127.0.0.1:5000/"
@app.route("/")
def home():
    # Connect to database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # limiting query to just 25 for home page
    cursor.execute("SELECT title, author, isbn, price FROM books LIMIT 9")
    books_data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Pass the fetched data to the template for rendering
    return render_template("home.html", books_data=books_data)


# This is the v2 Login function.
# Currently, entering anything in the user and password fields logs in a user.
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


@app.route("/display/<int:page>")
def display(page):
    # only 25 per page
    page_size = 27
    offset = (page - 1) * page_size

    # Connect to database and execute query
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, isbn, price FROM books LIMIT ? OFFSET ?", (page_size, offset))
    books_data = cursor.fetchall()
    conn.close()

    return render_template("display.html", books_data=books_data, current_page=page)


# This functions adds a placeholder display page, accessed by logging in
@app.route("/catalog")
def inventory():
    return render_template('catalog.html', data_type='catalog Page')


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

@app.route("/book_details/<title>")
def book_details(title):
    # Fetch book details from your database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book_data = cursor.fetchone()
    conn.close()

    # Using google API due to no descritpion from open lib
    description = ""
    google_books_api_url = f"https://www.googleapis.com/books/v1/volumes?q={title}" # items contains volumn info
    response = requests.get(google_books_api_url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            book_info = data['items'][0]['volumeInfo']  # Getting first results only. descrition is in VolumeInfo.
            if 'description' in book_info:
                description = book_info['description']

    return render_template("book_details.html", book_data=book_data, description=description)

# Checkout
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Print out the form data for debugging
    print("Form data:", request.form)
    
    # Fetch books_data from the database or wherever it's stored
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books_data = cursor.fetchall()
    conn.close()

    # Retrieve book title index from the button click
    title_index = int(request.form['index'])
    
    # Retrieve book information from the database based on the title index
    book_info = books_data[title_index]
    
    # Debug statement
    print("Book info:", book_info)
    
    # Add the book information to the session cart
    if 'cart' not in session:
        session['cart'] = []
    
    # Append book_info to the end of the list (stack)
    session['cart'].append(book_info)
    
    # Debug statement
    print("Cart:", session['cart'])
    
    # Redirect to the checkout page after adding the book to the cart
    return redirect(url_for('checkout'))


@app.route('/checkout')
def checkout():
    # Retrieve the cart from the session
    cart = session.get('cart', [])
    
    # Create a copy of the cart for display purposes and reverse it
    reversed_cart = cart[::-1]
    
    # Debug statement
    print("Cart in checkout:", cart)

    # Render the checkout page with the reversed cart data
    return render_template('checkout.html', cart=reversed_cart)


if __name__ == "__main__":
    app.run(debug=True)
