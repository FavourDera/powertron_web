from functools import wraps
from flask import session, redirect, url_for

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('loginpage'))
        return f(*args, **kwargs)
    return decorated_function

def is_lecturer(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session or session['user'].get('category') != 'lecturer':
            return redirect(url_for('loginpage'))
        return f(*args, **kwargs)
    return decorated_function 