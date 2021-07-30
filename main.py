'''
The main flask app.
:author: Mikey Lau
Website <https://mikeylau.uk>
GitHub <https://github.com/MikeyJL>
'''

# -----------------
# Set-up
# -----------------

from flask import Flask, render_template, request
from models import UserModel, PostModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HelloWorld123'
is_logged_in = False

# -----------------
# Routes
# -----------------

@app.route('/', methods=['GET'])
def index ():
    return render_template('home.html', is_logged_in = is_logged_in, posts = PostModel().get_all())

@app.route('/login', methods=['GET', 'POST'])
def login ():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        is_logged_in = UserModel().getUser(
            request.form['email'],
            request.form['password']
        )
        return render_template('home.html', is_logged_in = is_logged_in, posts = PostModel().get_all())

@app.route('/register', methods=['GET', 'POST'])
def register ():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        is_logged_in = UserModel().create(
            request.form['first-name'],
            request.form['last-name'],
            request.form['email'],
            request.form['password']
        )
        return render_template('home.html', is_logged_in = is_logged_in, posts = PostModel().get_all())

@app.route('/logout', methods=['GET'])
def logout ():
    if request.method == 'GET':
        is_logged_in = False
        return render_template('home.html', is_logged_in = is_logged_in, posts = PostModel().get_all())

@app.route('/posts', methods=['GET', 'POST'])
def posts ():
    if request.method == 'GET':
        posts = PostModel().get_all()
        print(posts)
    elif request.method == 'POST':
        PostModel().create(
            request.form['title'],
            request.form['caption']
        )
        return render_template('home.html', is_logged_in = is_logged_in, posts = PostModel().get_all())