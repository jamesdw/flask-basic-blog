from flask import Blueprint

# auth_bp = Blueprint("auth", __name__, 
#                 template_folder="templates/",
#                 static_folder="static", static_url_path="assets")

auth_bp = Blueprint("auth", __name__, 
                template_folder="templates/")

from . import routes

