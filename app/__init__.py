from flask import Flask
from .utils import db, login_manager
from .auth import auth_bp
from .main import main_bp
from config import get_config
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

def create_app(conf):
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    #setup config
    #env_allowed = {"local", "test", "prod" }
    #env_current = get_config()
    app.config.from_object(get_config())
    #app.config.from_object(config_map[conf])

    # Init extensions
    db.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    return app