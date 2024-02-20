# Bombastic Bookstore Config file
# Matt Wilamowski

import os

# assigns base directory for app
basedir = os.path.abspath(os.path.dirname(__file__))

# Config function
# Establishes secret key
# Establishes setup info for SQLAlchemy
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'capstone'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'user.db')
