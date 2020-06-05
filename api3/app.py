from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_user()
    elif request.method == 'GET':
        serve_login_page()

@app.route('/')
def index():
    return 'Index Page'
    

@app.route('/hello')
def say_hello():
    return 'Hello, greetings from a different endpoint'

@app.route('/user/<username>')
def show_user(username):
    return 'Username: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return str(post_id)