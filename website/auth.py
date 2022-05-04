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
                return res
    return render_template('login.html')
    
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
        selectedTask = False
        user_id = request.cookies.get('userlog')
        taskslist = Tasks.query.filter_by(User_id=int(user_id))
        usercach = User.query.filter_by(Id=int(user_id)).first()
        if (usercach.Position == 'Директор'):
            dirstr='isdir'
            print(dirstr)
            req = request.form.get('FIO')
            if(req is not None):
                print(req)
                FIOList = req.split(' ')
                if(len(FIOList) == 3):
                    userfiolist = User.query.filter_by(FirstName=str(FIOList[1]), LastName=str(FIOList[0]), Patronymic=str(FIOList[2])).first()
                    print(userfiolist)
                    if(userfiolist is not None):
                        FIOtasklist = Tasks.query.filter_by(User_id=int(userfiolist.Id))
                        return render_template('profile.html',ftaskslist=FIOtasklist, dirstatus=dirstr)
                else:
                    print('Noooooo')
            req = request.form.get('tasks')
            if(req is not None):    
                print(int(req))
                TaskID = Tasks.query.filter_by(Id=int(req)).first()
                taskinf= Tasks.query.filter_by(Id=int(req))
                Userinf = User.query.filter_by(Id=int(TaskID.User_id))
                StartDate = str(taskinf.first().StartDate).replace(' ','T')
                FinalDate = str(taskinf.first().StartDate).replace(' ','T')
                return render_template('profile.html', dirstatus=dirstr, Userinfo=Userinf, taskinfo=taskinf, StartDate=StartDate, FinalDate=FinalDate)
            req = request.form.get('EditTask')
            if(req is not None):
                EditFio = str(request.form.get('EditFio'))
                EditStartDate = str(request.form.get('EditStartDate'))
                EditFinalDate = str(request.form.get('EditFinalDate'))
                EditNameTask = str(request.form.get('EditNameTask'))
                EditTaskInfo = str(request.form.get('EditTaskInfo'))
                EditStatus = str(request.form.get('EditStatus'))
                if(EditFio is not None 
                and EditStartDate is not None 
                and EditFinalDate is not None 
                and EditNameTask is not None 
                and EditTaskInfo is not None 
                and EditStatus is not None):

                    # EditFio= EditFio.split(': ')
                    # EditStartDate = EditStartDate.split(': ')
                    # EditFinalDate = EditFinalDate.split(': ')
                    # EditNameTask = EditNameTask.split(': ')
                    # EditTaskInfo = EditTaskInfo.split(': ')
                    # EditStatus = EditStatus.split(': ')

                    # if(len(EditFio) == 2
                    # and len(EditNameTask) == 2
                    # and len(EditTaskInfo) == 2):
                    #     if(User.query.filter_by(LastName=str(EditFio[1]).split(' ')[0]).first()):
                            print(EditFio)
                            print(EditStartDate)
                            print(EditFinalDate)
                            print(EditNameTask)
                            print(EditTaskInfo)
                            print(EditStatus)
                



        else:
            dirstr='isnotdir'
            print(dirstr)
        return render_template('profile.html',taskslist=taskslist, dirstatus=dirstr)
    
    
@auth.route('/logout')
def logout():
    print('123')
    return "<p>Logout</p>"