from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(64))
    LastName = db.Column(db.String(64))
    Patronymic = db.Column(db.String(64))
    Login = db.Column(db.String(128))
    Password = db.Column(db.String(128))
    Position = db.Column(db.String(64))
    Mailbox = db.Column(db.String(128))

class Tasks(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    User_id = db.Column(db.Integer, db.ForeignKey(User.Id))
    Task_name = db.Column(db.String(128))
    Task = db.Column(db.String(1000))
    StartDate = db.Column(db.DateTime(timezone = True), default=func.now())
    FinalDate = db.Column(db.DateTime(timezone = True), default=func.now())
    Status = db.Column(db.String(64))