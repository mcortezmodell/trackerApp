from flask import Flask, session, redirect, url_for, render_template, request
from flask_admin import Admin


app = Flask(__name__)

# set up secret key (move secure info to gitignore file later on)
app.secret_key = 'pass01234567'

# # set bootswatch theme
# app.config['FLASK_ADMIN_SWATCH'] = 'journal'

# # initialize an empty admin interface 
# admin = Admin(app, name='Bug Tracker App', template_mode='bootstrap3')

# add modelviews for admin interface via. sqlalchemy - use MySQL or PostgresSQL 

@app.route('/')
def index():
     return render_template("index.html")

if __name__ == "__main__":
    app.run()