from ext import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    school_id = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)  # hashed password
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    items = db.relationship("Item", backref="category", lazy=True)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    name = db.Column(db.String(100), nullable=False)
