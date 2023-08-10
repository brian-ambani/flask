from flask import Flask, request

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifyinfg its behaviour

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

# Understanding request methods

@app.route('/index')
def index():
    return "Method used: %s" % request.method

@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"

if __name__ == "__main__":
    app.run()
