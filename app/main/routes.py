from flask import render_template
from flask_login import login_required
from . import main_bp

@main_bp.route("/")
@login_required
def dashboard():
    return render_template("main/dashboard.html")

@main_bp.route("/")
def home():
    return render_template("main/home.html")

