from flask import render_template, redirect, url_for
from . import main
from ..models import User
from .. import db

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    title= "About us"

    return render_template('aboutus.html', title=title)

@main.route('/user/<username>')
def user(username):
    user= User.query.filter_by(username=username).first_or_404()
    posts=[
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
        
    ]
    return render_template('user.html', user=user, posts=posts)
