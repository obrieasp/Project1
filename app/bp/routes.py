from flask import Blueprint, render_template
from app import db
from app.models import User

bp = Blueprint('bp', __name__)

@bp.route('/users')
def users():
    users = db.session.query(User).all()
    return '<br>'.join([f'User {user.id}: {user.name}' for user in users])

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/index')
def index():
    return render_template('index.html')

