from flask import render_template,redirect,url_for,flash,request
from . import pitch
from ..models import Pitch,User
from flask_login import login_required,login_user,logout_user,current_user
from .forms import PitchForm,LoginForm,RegistrationForm
from ..email import mail_message
from .. import db



@pitch.route('/')
def index():
    return render_template('index.html')

@pitch.route('/pitches')
def pitches():
    all_pitches = Pitch.query.all()
    return render_template('pitches.html', all_pitches = all_pitches)

@pitch.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            

        flash('Invalid username or Password')

    title = "pitch login"
    return render_template('login.html',form = form)

@pitch.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    # if form.validate_on_submit():
    user = User(email = form.email.data, username = form.username.data,password = form.password.data)
    db.session.add(user)
    db.session.commit()

    if user.email:
        mail_message("Welcome to pitches","email/welcome_user",user.email,user=user)
        return redirect(url_for('login'))

    return render_template('register.html',form = form)


@pitch.route('/addpitch',methods = ["GET","POST"])
def add_pitch():
    form = PitchForm()
    # if form.validate_on_submit():
    print (form.product.data)
    product = Pitch(product = form.product.data, price = form.price.data, market = form.market.data,
    product_info = form.product_info.data, votes = 0)
    db.session.add(product)
    db.session.commit()
        
    
    title = "New Pitch"
    return render_template('addPitch.html',form = form)

