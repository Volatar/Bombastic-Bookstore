# Bombastic Bookstore
# Flask Website v1

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Separate function for home page content
def get_home_content():
    return "Hello World! This is the starter version of our website <h1>HELLO<h1>"

# This function gives us the current "home" page
# This starter version runs locally, and the web browser URL is "http://127.0.0.1:5000/"
@app.route("/")
def home():
    # Render the home page content using the separate function
    content = get_home_content()
    return render_template("Home.html", content=content)

# This function adds a preliminary login ("http://127.0.0.1:5000/login")
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug=True)
