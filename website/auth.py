from flask import Blueprint, render_template, request, make_response, redirect,url_for
from itsdangerous import json
from .models import User, Tasks
from . import db
import sqlite3

from website import models

auth = Blueprint('auth', __name__)

@auth.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.cookies.get('userlog'):
        return redirect('/profile')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email:
            user = User.query.filter_by(Mailbox=email, Password=password).first()
            if user:
                print(user.Login + "   loggined")

                res = redirect('/profile')
                res.set_cookie('userlog', str(user.Id))
                #return redirect('/profile')
                return res

    return render_template('login.html')
    
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
        user_id = request.cookies.get('userlog')
        taskslist = Tasks.query.filter_by(User_id=int(user_id))
        usercach = User.query.filter_by(Id=int(user_id)).first()
        if (usercach.Position == 'Директор'):
            dirstr='isdir'
            print(dirstr)
            req = request.form.get('FIO')
            print(req)
            if(req is not None):
                FIOList = req.split(' ')
                if(len(FIOList) == 3):
                    userfiolist = User.query.filter_by(FirstName=str(FIOList[1]), LastName=str(FIOList[0]), Patronymic=str(FIOList[2])).first()
                    print(userfiolist)
                    if(userfiolist is not None):
                        FIOtasklist = Tasks.query.filter_by(User_id=int(userfiolist.Id))
                        return render_template('profile.html',ftaskslist=FIOtasklist, dirstatus=dirstr)
                else:
                    print('Noooooo')
        else:
            dirstr='isnotdir'
            print(dirstr)
        return render_template('profile.html',taskslist=taskslist, dirstatus=dirstr)
    
    
@auth.route('/logout')
def logout():
    print('123')
    return "<p>Logout</p>"