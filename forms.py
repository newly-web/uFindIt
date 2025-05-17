from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, ValidationError, Regexp


def student_number_validator(form, field):
    if len(field.data) != 9:
        raise ValidationError("Oops! Your School ID must have exactly 9 digits.")
    if not field.data.startswith(("30", "20")):
        raise ValidationError("Are you sure this is a uOttawa student number?")


class SignUpForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=5, max=20)]
    )
    student_number = StringField(
        "Student number",
        validators=[DataRequired(), student_number_validator],
    )
    email = StringField(
        "Student email",
        validators=[
            DataRequired(),
            Email(),
            Regexp(
                r"^[a-zA-Z0-9._%+-]+@uottawa\.ca$",
                message="Oops! Your email should end with @uottawa.ca",
            ),
        ],
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3)])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Student email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3)])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
