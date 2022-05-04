from flask import Blueprint, render_template, request, make_response, redirect,url_for
from itsdangerous import json
from .models import User, Tasks
from . import db
import sqlite3, os.path

from website import models

auth = Blueprint('auth', __name__)

@auth.route('/logins', methods=['GET', 'POST'])
def logins():
    if request.cookies.get('userlog'):#Поиск куки с аккаунтом
        return redirect('/profile')
    if request.method == 'POST':
        email = request.form.get('email')#Если куки нету берет логин и пароль, что ввели 
        password = request.form.get('password')
        if email:
            user = User.query.filter_by(Mailbox=email, Password=password).first()#Ищет их в базе данных
            if user:
                print(user.Login + "   loggined")
                res = redirect('/profile')#Если авторизация пройдена, открывает профиль
                res.set_cookie('userlog', str(user.Id))
                return res
    return render_template('login.html')
@auth.route('/profile', methods=['GET', 'POST'])
def profile():
        user_id = request.cookies.get('userlog')
        taskslist = Tasks.query.filter_by(User_id=int(user_id))
        usercach = User.query.filter_by(Id=int(user_id)).first()#Получаем должность из бд
        if (usercach.Position == 'Директор'):
            dirstr='isdir'#Записываем должность в переменную

            print(dirstr)

            NewUser = request.form.get('NewUser')#Принимает нажатие на кнопкку добавления пользователя
            if (NewUser is not None and NewUser == "NewUser"):
                AddUserInfo = 'NewUsers'
                return render_template('profile.html', dirstatus=dirstr, AddUser=AddUserInfo)

            AddUserInfo = request.form.get('AddUserButt')
            if(AddUserInfo is not None and AddUserInfo == "AddUserButt"):
                print(AddUserInfo)
                if(request.form.get('AddUserFio') is not None and request.form.get('AddUserFio') != ""   #---------------------------------##########
                and request.form.get('AddUserLogin') is not None and request.form.get('AddUserLogin') != ""                                         #
                and request.form.get('AddUserPosition') is not None and request.form.get('AddUserPosition') != ""                                   #
                and request.form.get('AddUserMailbox') is not None and request.form.get('AddUserMailbox') != ""                                     #
                and request.form.get('AddUserPassword') is not None and request.form.get('AddUserPassword') != ""):                                 #
                    AddUserInfoFIO = str(request.form.get('AddUserFio'))
                    AddUserFirstName = str(AddUserInfoFIO.split(' ')[1])    
                    AddUserLastName = str(AddUserInfoFIO.split(' ')[0])
                    AddUserPatronymic = str(AddUserInfoFIO.split(' ')[2])
                    AddUserLogin = str(request.form.get('AddUserLogin'))
                    AddUserPassword = str(request.form.get('AddUserPassword'))
                    AddUserPosition = str(request.form.get('AddUserPosition'))
                    AddUserMailbox = str(request.form.get('AddUserMailbox'))
                    if (AddUserFirstName is not None and
                        AddUserLastName is not None and
                        AddUserPatronymic is not None and                                               #Проверка, на пустые ячейки, и правильность написания данных
                        AddUserLogin is not None and
                        AddUserPassword is not None and
                        AddUserPosition is not None and
                        AddUserMailbox is not None):
                            print(AddUserFirstName)
                            print(AddUserLastName)
                            print(AddUserPatronymic)                                                                                                #
                            print(AddUserLogin)                                                                                                     #
                            print(AddUserPassword)                                                                                                  #
                            print(AddUserPosition)                                                                                                  #
                            print(AddUserMailbox)#---------------------------------------------------------------------------------------------######
                            directory = os.getcwd()
                            print(f"{directory}\website\database.db")
                            conn = sqlite3.connect((directory + '\website\database.db'))




                            cursor = conn.cursor()#-------------------------------------Добавление пользователя в бд----------------------------#####
                            sql_update_query = f"""INSERT INTO User(Id,FirstName,LastName,Patronymic,Login,Password,Position,Mailbox)
                                                   VALUES("{str(int(User.query.all()[-1].Id)+1)}",
                                                   "{str(AddUserFirstName)}",
                                                   "{str(AddUserLastName)}",
                                                   "{str(AddUserPatronymic)}",
                                                   "{str(AddUserLogin)}",
                                                   "{str(AddUserPassword)}",
                                                   "{str(AddUserPosition)}",
                                                   "{str(AddUserMailbox)}")"""
                            cursor.executescript(sql_update_query)#--------------------------------------------------------------------------#########
                            conn.commit()
                            conn.close()




            NewTask  = request.form.get('NewTask')  # Нажатие на кнопку Добавления задачи
            if(NewTask is not None and NewTask == 'NewTask'):
                print(NewTask)
                return render_template('profile.html',NewTask=NewTask, dirstatus=dirstr)
            AddTaskButt = request.form.get('AddTaskButt')
            if(AddTaskButt is not None and AddTaskButt == 'AddTaskButt'):
                print('AddTaskButt')                                                                                        #############################
                if(request.form.get('AddTaskFio') is not None and request.form.get('AddTaskFio') != ""
                and request.form.get('AddTaskName') is not None and request.form.get('AddTaskName') != ""
                and request.form.get('AddTask') is not None and request.form.get('AddTask') != ""
                and request.form.get('AddTaskStartDate') is not None and request.form.get('AddTaskStartDate') != ""
                and request.form.get('AddTaskFinalDate') is not None and request.form.get('AddTaskFinalDate') != ""):
                    print(1)
                    AddTaskFio = str(request.form.get('AddTaskFio'))
                    AddTaskFirstName = str(AddTaskFio.split(' ')[1])    
                    AddTaskLastName = str(AddTaskFio.split(' ')[0])                                   #Проверка перемнных на правильность формата и конвертация
                    AddTaskPatronymic = str(AddTaskFio.split(' ')[2])
                    AddTaskName = str(request.form.get('AddTaskName'))
                    AddTask = str(request.form.get('AddTask'))
                    AddTaskStartDate = str(request.form.get('AddTaskStartDate').replace('T', ' ')+ ':00')
                    AddTaskFinalDate = str(request.form.get('AddTaskFinalDate').replace('T', ' ')+ ':00')
                    AddTaskStatus = str('В разработке')                                                                      ############################
                    if (AddTaskFirstName is not None and
                        AddTaskLastName is not None and
                        AddTaskPatronymic is not None and
                        AddTaskName is not None and
                        AddTask is not None and
                        AddTaskStartDate is not None and
                        AddTaskFinalDate is not None and
                        AddTaskStatus is not None):
                            print(AddTaskFio)
                            print(AddTaskFirstName)
                            print(AddTaskLastName)
                            print(AddTaskPatronymic)
                            print(AddTaskName)
                            print(AddTask)
                            print(AddTaskStartDate)
                            print(AddTaskFinalDate)
                            print(AddTaskStatus)
                            print(Tasks.query.all()[-1].Id +1)
                            if (User.query.filter_by(FirstName=str(AddTaskFirstName), LastName=str(AddTaskLastName), Patronymic=str(AddTaskPatronymic)).first()):
                                print(User.query.filter_by(FirstName=str(AddTaskFirstName), LastName=str(AddTaskLastName), Patronymic=str(AddTaskPatronymic)).first())
                                directory = os.getcwd()
                                print(f"{directory}\website\database.db")
                                conn = sqlite3.connect((directory + '\website\database.db'))                
                                cursor = conn.cursor()     #-------------------------------------------------------------------Запись Новой задачи в БД
                                sql_update_query = f"""INSERT INTO Tasks(Id,User_id,Task_name,Task,StartDate,FinalDate,Status)  
                                                        VALUES("{str(int(Tasks.query.all()[-1].Id) +1)}",
                                                        "{str(User.query.filter_by(FirstName=str(AddTaskFirstName), LastName=str(AddTaskLastName), Patronymic=str(AddTaskPatronymic)).first().Id)}",
                                                        "{str(AddTaskName)}",
                                                        "{str(AddTask)}",
                                                        "{str(AddTaskStartDate)}",
                                                        "{str(AddTaskFinalDate)}",
                                                        "{str(AddTaskStatus)}")"""
                                cursor.executescript(sql_update_query)
                                conn.commit()               #------------------------------------------------------------------------------------------
                                conn.close()



            req = request.form.get('FIO')                   #-----------------------------------------Поиск пользователей в окне поиска
            if(req is not None):    
                print(req)
                FIOList = req.split(' ')
                if(len(FIOList) == 3):
                    userfiolist = User.query.filter_by(FirstName=str(FIOList[1]), LastName=str(FIOList[0]), Patronymic=str(FIOList[2])).first()
                    print(userfiolist)
                    if(userfiolist is not None):
                        FIOtasklist = Tasks.query.filter_by(User_id=int(userfiolist.Id))
                        return render_template('profile.html',ftaskslist=FIOtasklist, dirstatus=dirstr)  #------------------------------




            req = request.form.get('tasks')    #--------------------------------------------------нажатие на задачу и выдача данных для Редактирования на сайт
            if(req is not None):
                print(int(req))
                TaskID = Tasks.query.filter_by(Id=int(req)).first()
                taskinf= Tasks.query.filter_by(Id=int(req))
                Userinf = User.query.filter_by(Id=int(TaskID.User_id))
                StartDate = str(taskinf.first().StartDate).replace(' ','T')[:-3]
                FinalDate = str(taskinf.first().StartDate).replace(' ','T')[:-3]
                return render_template('profile.html', dirstatus=dirstr, Userinfo=Userinf, taskinfo=taskinf, StartDate=StartDate, FinalDate=FinalDate)





            req = request.form.get('EditTask')                                      #------------------------------Сохранения отредактированного задания при нажатии на кнопкут
            if(req is not None):
                EditFio = str(request.form.get('EditFio'))
                EditStartDate = str(request.form.get('EditStartDate'))
                EditFinalDate = str(request.form.get('EditFinalDate'))
                EditNameTask = str(request.form.get('EditNameTask'))
                EditTaskInfo = str(request.form.get('EditTaskInfo'))
                EditStatus = str(request.form.get('EditStatus'))
                TaskSelected = str(request.form.get('TaskSelected'))
                if(EditFio is not None 
                and EditStartDate is not None 
                and EditFinalDate is not None 
                and EditNameTask is not None 
                and EditTaskInfo is not None 
                and EditStatus is not None):
                    if(len(EditFio.split(' '))==3
                    and User.query.filter_by(LastName=(EditFio.split(' '))[0]).first()
                    and User.query.filter_by(FirstName=(EditFio.split(' '))[1]).first()
                    and User.query.filter_by(Patronymic=(EditFio.split(' '))[2]).first()):

                        TaskCommit = Tasks.query.filter_by(Id=int(TaskSelected)).first()
                        print(TaskCommit)
                        print(TaskCommit.User_id)
                        TaskCommit.User_id = User.query.filter_by(LastName=(EditFio.split(' '))[0],FirstName=(EditFio.split(' '))[1],Patronymic=(EditFio.split(' '))[2]).first().Id
                        print(TaskCommit.User_id)
                        TaskCommit.Task_name = EditNameTask
                        TaskCommit.Task = EditTaskInfo
                        TaskCommit.Status = EditStatus
                        TaskCommit.FinalDate=(EditFinalDate.replace('T', ' '))+ ':00'
                        TaskCommit.StartDate=(EditStartDate.replace('T', ' '))+ ':00'
                        
                        directory = os.getcwd()
                        print(f"{directory}\website\database.db")
                        conn = sqlite3.connect((directory + '\website\database.db'))
                        cursor = conn.cursor()                                  #------------------------------Добавление в бд
                        sql_update_query = f"""Update Tasks set Task = "{str(TaskCommit.Task)}" Where Id = {str(TaskSelected)};
                                            Update Tasks set User_id = "{str(TaskCommit.User_id)}" Where Id = {str(TaskSelected)};
                                            Update Tasks set Task_name = "{str(TaskCommit.Task_name)}" Where Id = {str(TaskSelected)};
                                            Update Tasks set StartDate = "{str(TaskCommit.StartDate)}" Where Id = {str(TaskSelected)};
                                            Update Tasks set FinalDate = "{str(TaskCommit.FinalDate)}" Where Id = {str(TaskSelected)};
                                            Update Tasks set Status = "{str(TaskCommit.Status)}" Where Id = {str(TaskSelected)}"""
                        cursor.executescript(sql_update_query)
                        conn.commit()
                        conn.close()
            req = request.form.get('SendReport')
            if(req is not None):
                print('Report')
        else:
            dirstr='isnotdir'# ---  ---------------------------------       -------------Запуск профиля рабочего
            print(dirstr)
        return render_template('profile.html',taskslist=taskslist, dirstatus=dirstr)
    
    
@auth.route('/logout')      #Выход
def logout():
    return "<p>Logout</p>"