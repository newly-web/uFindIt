from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, Regexp
# <!-- the validation doesnt work properly -->


class SignUpForm(FlaskForm):
    # Here im thinking about maybe making a first name, last name and username, to make sure we can have a list of students if needed and then make the name visibility optional
    username = StringField('Username', validators=[DataRequired(),Length(min=5, max=20)])

    student_number = StringField('Student number', validators=[DataRequired(),
        Length(min=9, max=9, message="Oops! Your School ID must have exactly 9 digits")])

    email = StringField(
        "Student email",
        validators=[
            DataRequired(),
            Email(),
            Regexp(r'^[a-zA-Z0-9._%+-]+@uottawa\.ca$',message="Oops! Your email should end with @uottawa.ca"),
        ],
    )
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3)])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField(
        "Student email", validators=[DataRequired(), Email()]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3)])
    remember = BooleanField('Remember Me')
    submit = SubmitField("Login")
