from datetime import  datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dd5b595d3b354e31adc2f934df7210b0'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# la class pour la base de donnée pour l'enrgistrement de l'utilisateur
class User(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20),nullable=False, default='default.jpg')
    password = db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

# la class pour la base de donnée pour l'enrgistrement des publications
class Post(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    title = db.Column(db.String(100),unique=True, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow())
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Publié par('{self.title}', '{self.date_posted}')"

# la route qui  va vers la page 'accueil
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# la route qui va vers la page  de connexion
@app.route('/login',methods=['GET','POST'])
def log():
    form = LoginForm()
    # condition de validation des information saisies à la connexion 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('Vous êtes maintenant connecté','success')
            # si la connexxion est parfaite, l'utilisateur sera redirigé vers une nouvelle page
            return redirect(url_for('home'))
        else:
            # sinon un message d'erreur va s'afficher
            flash("Erreur de connexion, S'il vous plaît vérifier si votre Email et votre Mot de passe sont correctes", 'danger')
    return render_template('login.html',title='Connexion',form=form)

# la route qui va vers la page d'inscription
@app.route('/signup',methods=['GET','POST'])
def sign_up():
    form =RegistrationForm()
    # condition de validation des information saisies à la connexion
    if form.validate_on_submit():
        flash('Compte créé pour {}!'.format(form.username.data),'success')
        # si l'inscription est validé l'utilisateur sera redirigé vers la page de connexion pour verifier  qu'il est vraiment connecté
        return redirect(url_for('log'))
    form =RegistrationForm()
    return render_template('signup.html',title='Inscription',form=form)
# la route qui va vers la page de base
@app.route('/layout')
def layout():
    return render_template('layout.html')
    

