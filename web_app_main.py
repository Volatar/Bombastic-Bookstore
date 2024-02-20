# Bombastic Bookstore
# Flask Website v1

from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)


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


# This function adds a preliminary login ("http://127.0.0.1:5000/login")
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid'
        else:
            return redirect(url_for('profile'))
    return render_template('login.html', error=error)


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


if __name__ == "__main__":
    app.run(debug=True)
