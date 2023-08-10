from flask import Flask

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifyinfg its behaviour

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username


@app.route('/profile/<int:post_id>')
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

if __name__ == "__main__":
    app.run()
