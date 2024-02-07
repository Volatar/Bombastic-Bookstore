# Bombastic Bookstore
# Flask Website v1

from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)
