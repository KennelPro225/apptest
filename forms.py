from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,EmailField,BooleanField,SubmitField
from wtforms.validators import DataRequired, Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Nom d'utilisateur",
                            validators=[DataRequired(), Length(min=2, max=20)])
    
    email = EmailField('Email',
                        validators=[DataRequired(),Email()])

    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmartion Mot de passe',
                                        validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("S'inscrire")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])

    password = PasswordField('Mot de passe', validators=[DataRequired()])
    remember =  BooleanField('Me garder connecter')
    submit = SubmitField('Se connecter')




