from flask import Flask,render_template
from forms import SignUpForm, LoginForm
app = Flask(__name__)
# this needs to be an ENV variable after
app.config['SECRET_KEY'] = '8393b6e6a5d2b2a673bebdcbe2af3b88' 


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/signup")
def signUp():
    form = SignUpForm()
    return render_template('signup.html', title='Sign Up', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
