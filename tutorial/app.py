from flask import Flask

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifyinfg its behaviour

@app.route('/')
def home():
    return 'This is the home page'

@app.route('/profile/<username>')
def profile(username):
    return "Hey there %s" % username


if __name__ == "__main__":
    app.run()
