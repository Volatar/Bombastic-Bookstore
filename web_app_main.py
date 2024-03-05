# Bombastic Bookstore
# Flask Website v1

import secrets
import sqlite3, requests
from Inventory_chart import generate_bar_chart
from flask import Flask, render_template, session, redirect, flash, url_for, request, jsonify
from flask_session import Session
from flask_paginate import Pagination, get_page_args
import re
from forms import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from math import ceil
from payment import CreditCard
# from models import User

app = Flask(__name__)
app.config.from_object(__name__)

app.config['SESSION_TYPE'] = 'filesystem'

# Set the database URI for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

# Generate a secure random key for session security
app.secret_key = secrets.token_hex(16)  # 16 bytes (128 bits) is a common key length

db = SQLAlchemy(app)
migrate = Migrate(app, db)

FLASK_APP = 'web_app_main.py'

# Dictionary to cache generated bar chart images
chart_cache = {}

# create session object
Session(app)


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

def get_inventory_data(offset=0, per_page=10):
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, isbn, price FROM books LIMIT ? OFFSET ?", (per_page, offset))
    inventory_data = cursor.fetchall()
    conn.close()
    return inventory_data


def get_all_inventory_data():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    total_inventory_items = cursor.fetchone()[0]
    conn.close()
    return total_inventory_items

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
        # Pagination logic
        page, per_page, offset = get_page_args()
        total = get_all_inventory_data()  # Assuming you have a function to get total inventory count
        
        # Generate a unique cache key per page
        cache_key = f'inventory_{page}'
        
        # Check if the chart is cached for this page
        if cache_key in chart_cache:
            image_url = chart_cache[cache_key]
        else:
            # Generate bar chart for the current page
            image_url = generate_bar_chart(page=page, items_per_page=per_page)
            chart_cache[cache_key] = image_url
        
        pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='bootstrap4', prev_label='', next_label='')

        # Fetch data for the current page
        current_inventory_data = get_inventory_data(offset=offset, per_page=per_page)
        
        # Calculate total pages
        total_pages = ceil(total / per_page)
        
        return render_template('catalog.html', data_type=data_type, image_url=image_url, inventory_data=current_inventory_data, pagination=pagination, total_pages=total_pages)

    return render_template('catalog.html', data_type=data_type, data=data.get(data_type, ''))


@app.route("/book_details/<title>")
def book_details(title):
    # Fetch book details from your database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book_data = cursor.fetchone()
    conn.close()

    # Using google API due to no description from open lib
    description = ""
    google_books_api_url = f"https://www.googleapis.com/books/v1/volumes?q={title}"  # item contains volume info
    response = requests.get(google_books_api_url)
    if response.status_code == 200:  # only proceed if call is successful
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            book_info = data['items'][0]['volumeInfo']  # Getting first results only. description is in VolumeInfo.
            if 'description' in book_info:
                description = book_info['description']

    return render_template("book_details.html", book_data=book_data, description=description)


# Cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Fetch the book title from the form data
    book_title = request.form.get('title')

    # Debug statement
    print("Book selected:", book_title)

    # Add the book title to the session cart
    if 'cart' not in session:
        session['cart'] = []

    # Append the book title to the cart
    session['cart'].append(book_title)

    # Debug statement
    print("Book added to cart:", book_title)

    # Redirect to the cart page after adding the book to the cart
    return redirect(url_for('cart'))

@app.route('/empty_cart', methods=['POST'])
def empty_cart():
    # Clear the cart in the session
    if 'cart' in session:
        session['cart'] = []

    # Redirect to the cart page after emptying the cart
    return redirect(url_for('cart'))


@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    # Fetch the book title to be removed from the form data
    book_title = request.form.get('title')

    # Remove the book title from the session cart if it exists
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item != book_title]

    # Redirect to the cart page after removing the book from the cart
    return redirect(url_for('cart'))


@app.route('/remove_one_book', methods=['POST'])
def remove_one_book():
    # Fetch the book title to be removed from the form data
    book_title = request.form.get('title')

    # Remove one instance of the book title from the session cart if it exists
    if 'cart' in session and book_title in session['cart']:
        session['cart'].remove(book_title)

    # Redirect to the cart page after removing one book from the cart
    return redirect(url_for('cart'))


@app.route('/add_one_book', methods=['POST'])
def add_one_book():
    # Fetch the book title to be added from the form data
    book_title = request.form.get('title')

    # Add one instance of the book title to the session cart
    if 'cart' in session:
        session['cart'].append(book_title)

    # Redirect to the cart page after adding one book to the cart
    return redirect(url_for('cart'))


@app.route('/cart')
def cart():
    # Retrieve the cart from the session
    cart_titles = session.get('cart', [])

    # Count occurrences of each book title in the cart
    cart_count = {}
    for title in cart_titles:
        cart_count[title] = cart_count.get(title, 0) + 1

    # Fetch book details for each unique title in the cart
    cart_details = []
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    for title, count in cart_count.items():
        cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        book_info = cursor.fetchone()
        if book_info:
            cart_details.append((book_info, count))
    conn.close()

    # Render the cart page with the cart data
    return render_template('cart.html', cart=cart_details)

# Checkout
@app.route('/checkout')
def checkout():
    cart_titles = session.get('cart', [])
    cart_count = {}
    for title in cart_titles:
        cart_count[title] = cart_count.get(title, 0) + 1

    cart_details = []
    total_of_all_books = 0

    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    for title, count in cart_count.items():
        cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        book_info = cursor.fetchone()
        if book_info:
            price_str = re.sub(r'[^\d.]', '', book_info[6])
            price = float(price_str)
            cart_details.append((book_info, count, price * count))
            total_of_all_books += price * count
    conn.close()

    # Round up the total to the nearest cent
    total_of_all_books = round(total_of_all_books, 2)

    # Store cart details in session
    session['cart_details'] = cart_details

    return render_template('checkout.html', cart=cart_details, total_of_all_books=total_of_all_books)


# Payment
@app.route('/process_payment', methods=['POST'])
def process_payment():
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    card_holder_name = request.form['card_holder_name']

    # Convert card_number to integer for validation
    try:
        card_number = int(card_number)
    except ValueError:
        # Invalid card number format
        return jsonify({"passOrFail": "Fail"})

    # Check if the credit card number is valid using CreditCard class
    if CreditCard.isValid(card_number):
        # Card is valid, proceed with payment processing
        passOrFail = 'Pass'
    else:
        # Card is invalid
        passOrFail = 'Fail'

    return jsonify({"passOrFail": passOrFail})

# Receipt Route
@app.route('/receipt', methods=['POST'])
def receipt():
    cart_titles = session.get('cart', [])
    cart_count = {}
    for title in cart_titles:
        cart_count[title] = cart_count.get(title, 0) + 1

    cart_details = []
    total_of_all_books = 0

    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    for title, count in cart_count.items():
        cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        book_info = cursor.fetchone()
        if book_info:
            price_str = re.sub(r'[^\d.]', '', book_info[6])
            price = float(price_str) if price_str else 0
            cart_details.append((book_info, count, price * count))
            total_of_all_books += price * count
    conn.close()

    # Round up the total to the nearest cent
    total_of_all_books = round(total_of_all_books, 2)

    # Store cart details in session
    session['cart_details'] = cart_details
    
    # Extract data from the form
    book_titles_with_quantity = request.form.get('book_titles_with_quantity')
    card_holder_name = request.form.get('card_holder_name')  # Corrected variable name
    street = request.form.get('street')
    city = request.form.get('city')
    state = request.form.get('state')
    postal_code = request.form.get('postal_code')
    
    # Pass the data to the receipt template
    return render_template('receipt.html', book_titles_with_quantity=book_titles_with_quantity,
                           total_of_all_books=total_of_all_books, card_holder_name=card_holder_name,
                           street=street, city=city, state=state, postal_code=postal_code,
                           cart_details=cart_details)



if __name__ == "__main__":
    app.run(debug=True)