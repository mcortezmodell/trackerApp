from flask import Flask, redirect, render_template, request, url_for
from flask_admin import Admin, BaseView, expose

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')

app = Flask(__name__)

# initialize admin interface views 
admin = Admin(app)
# Add administrative views here
admin.add_view(MyView(name='Admin', endpoint='test1', category='Manage'))
admin.add_view(MyView(name='Developers', endpoint='test2', category='Manage'))
admin.add_view(MyView(name='Switch to User View', endpoint='test3', category='Manage'))

# consider switching to modelviews for admin interface via. sqlalchemy - use MySQL or PostgresSQL 

# set up secret key (move secure info to gitignore file later on)
# app.secret_key = 'pass01234567'

@app.route('/', methods=["POST", "GET"])
def index():
     return render_template("index.html")

@app.route('/login', methods=["POST", "GET"])
def login():
     return render_template("login.html")

if __name__ == "__main__":
    app.run()