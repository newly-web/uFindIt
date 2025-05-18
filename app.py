from flask import Flask, render_template, flash, redirect, url_for, request
from forms import SignUpForm, LoginForm,LostItemForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
from sqlalchemy.exc import IntegrityError
from flask_login import login_required, login_user, logout_user, current_user
from models import User, Category, Item, default_categories


from ext import db, login_manager

# Load environment variables
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///site.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "login"  # this is name of the login route (function name), basically redirect to this route if user is not logged i

    # Import routes and models after app and db are ready
    with app.app_context():
        db.create_all()
        default_categories() #this is the function that initializes all our default categories in the categories db

    # ALL the routes go here
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return render_template("about.html", title="About")

    @app.route("/signup" , methods=["GET", "POST"])
    def signUp():
        form = SignUpForm()
        if form.validate_on_submit():
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                flash("Email already registered. Try logging in.", "danger")
                return redirect(url_for("login"))

            hashed_password = generate_password_hash(form.password.data)
            new_user = User(
                email=form.email.data,
                school_id=form.student_number.data,
                username=form.username.data,
                password=hashed_password,
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash(f"Account created for {form.username.data}!", "success")
                return redirect(url_for("login"))
            except IntegrityError:
                db.session.rollback()  # Undo the failed insert
                flash(
                    "That school ID is already registered. Please log in or use another one.",
                    "danger",
                )
                return redirect(url_for("signUp"))
        else:
            if request.method == "POST":
                print(form.errors)
        return render_template("signup.html", title="Sign Up", form=form)

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash(f"Welcome back, {user.username}!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid email or password.", "danger")
        return render_template("login.html", title="Login", form=form)

    # ^ ONCE USER IS LOGGED IN

    @app.route("/dashboard")
    @login_required 
    def dashboard():
        return render_template("dashboard.html")

    # for users to report their lost object

    @app.route("/report-lost", methods=["GET", "POST"])
    @login_required
    def report_lost():
        form = LostItemForm()
        form.category.choices = [(c.id, c.name) for c in Category.query.all()]

        if form.validate_on_submit():
            new_item = Item(
                name=form.item_name.data,
                category_id=form.category.data,
                user_id=current_user.id,  #  links item to the current user
                date_lost=form.date_lost.data,
                location=form.location.data,
                description=form.description.data,
                reward=form.reward.data,
                image_filename=None,  # Handle image upload later
            )
            db.session.add(new_item)
            db.session.commit()
            print("Form loaded:", form)
            print("Category choices:", form.category.choices)

            flash("Lost item reported successfully!", "success")
            return redirect(url_for("dashboard"))  #! change this
        return render_template("report.html", form=form)
    # for ppl to be able to view all the items from a specific category
    @app.route("/category/<int:category_id>")
    def view_category(category_id):
        category = Category.query.get_or_404(category_id)
        items = Item.query.filter_by(category_id=category.id).all()
        return render_template("category_items.html", category=category, items=items)

    # for people to be able to click a category and see the items under it
    @app.route("/categories")
    def all_categories():
        categories = Category.query.all()
        return render_template("categories.html", categories=categories)


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
