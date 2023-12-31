from flask import Flask, render_template, request

app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modifyinfg its behaviour

@app.route('/1')
def home1():
    return 'This is the home page'

@app.route('/profile1/<username>')
def profile1(username):
    return "Hey there %s" % username


@app.route('/post1/<int:post_id>')
def show_post1(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

# Understanding request methods

@app.route('/index1')
def index1():
    return "Method used: %s" % request.method

@app.route("/bacon1", methods=['GET', 'POST'])
def bacon1():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are using GET"


# working with templates
@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)



# mappint two urls in one function

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)



# passing complex objects

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)

if __name__ == "__main__":
    app.run()
