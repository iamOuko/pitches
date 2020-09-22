from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail



login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

bootstrap = Bootstrap()
db = SQLAlchemy()

mail = Mail()

def create_app(config_name):
    app = Flask(__name__)

    
    

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    config_options[config_name].init_app(app)
    


    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # Registering the blueprint
    from .pitch import pitch as pitch_blueprint
    app.register_blueprint(pitch_blueprint)

    return app
