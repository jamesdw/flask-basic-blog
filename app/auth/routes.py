from flask import request, redirect, url_for, flash, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.utils import db
from . import auth_bp
from app.auth.forms import RegisterForm, LoginForm
import uuid
import os


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        display_name = form.display_name.data
        password = form.password.data

        # Generate salt and hash
        salt = os.urandom(16).hex()
        hashed_password = generate_password_hash(password + salt)

        # Create user record
        new_user = User(
            id=str(uuid.uuid4()),
            username=username,
            email=email,
            display_name=display_name,
            pass_hash=hashed_password,
            pass_salt=salt
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash("Registered and logged in successfully!", "success")
        return redirect(url_for('main.dashboard'))

    return render_template('auth/register.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            password_input = form.password.data
            if check_password_hash(user.pass_hash, password_input + user.pass_salt):
                login_user(user)
                flash("Logged in successfully!", "success")
                return redirect(url_for('main.dashboard'))
            else:
                flash("Incorrect password.", "danger")
        else:
            flash("User not found.", "danger")

    return render_template('auth/login.html', form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("auth.login"))
