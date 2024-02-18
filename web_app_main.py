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
    # Change the file to see the changes in the file on the server
    return render_template("home.html", content=content)


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

# This functions adds a placeholder display page, accessed by logging in
@app.route("/display")
def display():
    return render_template('display.html')

# This functions adds a placeholder display page, accessed by logging in
@app.route("/Catalog")
def inventory():
    return render_template('Catalog.html', data_type='Catalog Page')

@app.route('/Catalog/<data_type>')
def show_inventory(data_type):
    data = {
        'sells': 'This is the sells data.',
        'inventory': 'This is the inventory data.',
        'order': 'This is the Order page.',
        'storge': 'This is some storge data.'
    }
    return render_template('Catalog.html', data_type=data_type, data=data.get(data_type, ''))


if __name__ == "__main__":
    app.run(debug=True)
