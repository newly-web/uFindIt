from flask import Flask,render_template, flash, redirect, url_for
from forms import SignUpForm, LoginForm
app = Flask(__name__)
# this needs to be an ENV variable after
app.config['SECRET_KEY'] = '8393b6e6a5d2b2a673bebdcbe2af3b88' 


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/signup", methods=["GET", "POST"])
def signUp():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    else:
        print(form.errors)  # Print errors to debug if validation fails
    return render_template("signup.html", title="Sign Up", form=form)


@app.route("/login",methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # ? don't forget to remove the hard coded data
        if form.email.data == 'admin@uottawa.ca' and form.password.data == '12345678':
            flash('WE ARE INNNN', "success")
            return redirect(url_for('home'))
        else:
            flash("this aint u lol.", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
