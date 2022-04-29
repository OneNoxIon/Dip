from flask import Blueprint, render_template, request
#from flask_login import login_user, login_required,logout_user, current_user
from .models import User
#from werkzeug import generate_password_hash, check_password_hash      #In progress
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email:
            user = User.query.filter_by(Mailbox=email, Password=password).first()
            if user:
                print(user.Login + "   loggined")
                #login_user(user, remember=True)
                #in progress        if check_password_hash(User.password, password):
    #data = request.form
    #print(data)
    return render_template('login.html')
    
    
    
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"