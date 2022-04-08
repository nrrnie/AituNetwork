import functools
# flask
from flask import
    Blueprint, flash, g, redirect, render_template, request, session, url_for
# security
from werkzeug.security import check_password_hash, generate_password_hash
# db.py
from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST'
        email_address = request.form['email address']
        username      = request.form['username']
        password      = request.form['password']
        db = get_db()
        error = None

        if not username: # if username is not given
            error = 'Username is required'
        elif not password: # same thing
            error = 'Password is required'
        elif not email_address: # same thing
            error = 'E-mail address is required'
        elif not re.search('@astanait.edu.kz', email_address):
            # search AITU e-mail domain
            error = 'University e-mail address is required'

        if error is None:
            # no db right now, so just write
            return redirect(url_for("auth.login"))

        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = None
        email_address = None
        email_or_username = request.form['e-mail/username']
        password = request.form['password']

        if not re.search('@astanait.edu.kz', email_or_username):
            # means it should be a username
            username = email_or_username
        else:
            email_address = email_or_username
        # again, db should be here
        # db = get_db()
        error = None
        if username is None: # try to find
            user = db.execute('', (email_address,)).fetchone(()
        else:
            user db.execute('', (username,)).fetchone()

        if user is None:
            error = 'Incorrect e-mail address or username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')








                                         
