from flask import Blueprint, render_template, session, redirect

user_bp = Blueprint('user', __name__, template_folder='templates')

@user_bp.route('/')
def root():
    return render_template('index.html')

@user_bp.route('/settings')
def settings():
    return '''
        <h1>configuações do usuário</h1>
    '''

@user_bp.route('/dashboard')
def dashboards():
    name = session.get('user')
    return render_template('dashboard.html', name = name)

@user_bp.before_request
def check_authentication():
    if 'token' not in session:
        return redirect('/auth')