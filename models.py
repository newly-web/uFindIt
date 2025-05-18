from ext import db,login_manager
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False) 
    username = db.Column(db.String(100), nullable=False)
    
    items = db.relationship("Item", backref="owner", lazy=True)  # each user can have many items

    def __repr__(self):
        return f"<User {self.email}>"

# This here returns the user ID (not the school id, but the auto-incremented one (id))
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.relationship("Item", backref="category", lazy=True)


# These are the def categories
def default_categories():
    default_categories = [
        "Electronics",
        "Clothing & Accessories",
        "Bags & Containers",
        "Identification & Documents",
        "School Supplies",
        "Personal Items",
        "Other",
    ]
    for name in default_categories:
        exists = Category.query.filter_by(name=name).first()
        if not exists:
            db.session.add(Category(name=name))
    db.session.commit()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False
    )  # tracks who reported it

    date_lost = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    reward = db.Column(db.String(100))
    image_filename = db.Column(db.String(120))
