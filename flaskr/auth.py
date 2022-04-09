import mysql.connector, functools
from flask import Blueprint, flash, g, redirect, render_template,
    request, session, url_for
from werkzeug.security import
    check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        email    = request.form['e-mail address']
        username = request.form['username']
        password = request.form['password']
        error = None

        if not email:
            error = 'E-mail address is required'
        elif not re.search('@astanait.edu.kz', email):
            error = 'University e-mail (astanait.edu.kz) is required'
        elif not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'

        
        db = mysql.connector.connect(user='', database='')
        cursor = db.cursor()
        # add user
        cursor.execute("INSERT INTO ...", (email, userame, generate_password_hash,))

        if error is None:
            return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET','POST'))
def login():
    if request.method == 'POST':
        email_or_username   = request.form['e-mail or username']
        password            = request.form['password']
        error = None;

        # emptiness check
        if not email_or_username:
            error = 'E-mail or username are required'
        elif not password:
            error = 'Password is required'

        db = mysql.connector.connect(user='', database='')
        cursor = db.cursor()
        
        # email or username check
        if not re.search('@astanait.edu.kz', email_or_username)
            # assume it is username
            db_request = '' #SELECT USERNAME ...
        else:
            # assume it is email
            db_request = '' #SELECT EMAIL ...

        user = cursor.execute(db_request, (email_or_username,)).fetchone()

        if user is None:
            error = 'Incorrect e-mail address or username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session[''] = user['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')

