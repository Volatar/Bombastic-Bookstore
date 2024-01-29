# Bombastic Bookstore
# Flask Website v1

from flask import Flask

app = Flask(__name__)


# This function gives us the current "home" page
# This starter version runs locally, and the web browser URL is "http://127.0.0.1:5000/"
@app.route("/")
def home():
    return "Hello World! This is the starter version of our website <h1>HELLO<h1>"


if __name__ == "__main__":
    app.run()
