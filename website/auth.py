from flask import Blueprint, render_template, request, make_response, redirect
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.cookies.get('user'):
        return redirect('/profile')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email:
            user = User.query.filter_by(Mailbox=email, Password=password).first()
            if user:
                print(user.Login + "   loggined")
                res = make_response("Setting a cookie")
                res.set_cookie('user', user.Login, max_age=60*60*24)
                return redirect('/profile')

    return render_template('login.html')
    
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')
    
    
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"