# routes file for Bombastic Login (at least)
# This handles the different urls for the app

from flask import render_template, flash, redirect, url_for, request, session, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from urllib.parse import urlsplit
from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm
from flask_paginate import Pagination, get_page_args
from app.Inventory_chart import generate_bar_chart
from math import ceil
from app.payment import CreditCard
import sqlite3
import requests
import re

chart_cache = {}


@app.route("/")
def home():
    # Connect to database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Fetching books data from the database
    cursor.execute("SELECT title, author, isbn, price, quantity FROM books LIMIT 9")
    books_data = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Read BooksWithNoCover.txt file with 'utf-8' encoding
    file_path = url_for('static', filename='data/BooksWithNoCover.txt')
    with open('app' + file_path, 'r', encoding='utf-8') as file:  # Add 'app' before the file path
        books_with_no_cover = [line.strip() for line in file]

    # Pass the fetched data and BooksWithNoCover list to the template for rendering
    return render_template("home.html", books_data=books_data, BooksWithNoCover=books_with_no_cover)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', titel='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template('user.html', user=user)

@app.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 1:
        return render_template('admin.html')
    else:
        flash('Admin access required. Sorry, loser!')
        return redirect(url_for('home'))

@app.route("/display/<int:page>")
def display(page):
    page_size = 27  # number of books on one page
    offset = (page - 1) * page_size

    # Connect to database and execute query
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, author, isbn, price, quantity FROM books LIMIT ? OFFSET ?", (page_size, offset))
    books_data = cursor.fetchall()
    conn.close()

    # Read BooksWithNoCover.txt file with 'utf-8' encoding
    file_path = url_for('static', filename='data/BooksWithNoCover.txt')
    with open('app' + file_path, 'r', encoding='utf-8') as file:  # Add 'app' before the file path
        books_with_no_cover = [line.strip() for line in file]

    return render_template("display.html", books_data=books_data, current_page=page, BooksWithNoCover=books_with_no_cover)
@app.route("/admin")
def display_admin():
    return render_template("admin.html")


# This functions adds a placeholder display page, accessed by logging in.
# login req added
@app.route("/catalog")
@login_required
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

        pagination = Pagination(page=page, total=total, per_page=per_page, css_framework='bootstrap4', prev_label='',
                                next_label='')

        # Fetch data for the current page
        current_inventory_data = get_inventory_data(offset=offset, per_page=per_page)

        # Calculate total pages
        total_pages = ceil(total / per_page)

        return render_template('catalog.html', data_type=data_type, image_url=image_url,
                               inventory_data=current_inventory_data, pagination=pagination, total_pages=total_pages)

    return render_template('catalog.html', data_type=data_type, data=data.get(data_type, ''))


@app.route("/book_details/<title>")
def book_details(title):
    # Fetch book details from your database
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book_data = cursor.fetchone()
    conn.close()

    # Read BooksWithNoCover.txt file with 'utf-8' encoding
    file_path = url_for('static', filename='data/BooksWithNoCover.txt')
    with open('app' + file_path, 'r', encoding='utf-8') as file:  # Add 'app' before the file path
        books_with_no_cover = [line.strip() for line in file]

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

    return render_template("book_details.html", book_data=book_data, description=description, BooksWithNoCover=books_with_no_cover)


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


@app.route('/checkout')
@login_required
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
    empty_cart()
    
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


def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn


# Search Request
@app.route('/search')
def search():
    query = request.args.get('query')
    search_type = request.args.get('search_type')

    if not query or not search_type:
        return render_template('SearchPage.html')

    conn = get_db_connection()
    cursor = conn.cursor()
    # Can add more variables to the search bar here
    if search_type == 'title':
        cursor.execute("SELECT * FROM books WHERE Title LIKE ?", ('%' + query + '%',))
    elif search_type == 'author':
        cursor.execute("SELECT Title FROM books WHERE Author LIKE ?", ('%' + query + '%',))
    elif search_type == 'genre':
        cursor.execute("SELECT Title FROM books WHERE Genre LIKE ?", ('%' + query + '%',))

    results = cursor.fetchall()

    conn.close()

    # may need to change to redirect to inventory page
    return render_template('SearchResults.html', results=results, search_query=query)
