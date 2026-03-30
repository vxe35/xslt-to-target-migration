from flask import Blueprint, render_template

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/login')
def login():
    return render_template('login.html')

@home_bp.route('/register')
def register():
    return render_template('register.html')