# init file for program
# Flask uses this a starting point for loading resources

from flask import Flask
from flask_session import Session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import secrets

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['search'] = "search"
app.secret_key = secrets.token_hex(16)
chart_cache = {}

Session(app)

# if __name__ == "__main__":
#    app.run(debug=True)


from app import routes, models
# this import statement is placed at the bottom to avoid circular import issues
