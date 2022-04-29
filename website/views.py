from flask import Blueprint, redirect, render_template,redirect
from flask import url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():

    return redirect('/logins')