from flask import Flask
from flask_admin import Admin


app = Flask(__name__)

# set bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'journal'

# initialize an empty admin interface 
admin = Admin(app, name='microblog', template_mode='bootstrap3')

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

if __name__ == "__main__":
    app.run()