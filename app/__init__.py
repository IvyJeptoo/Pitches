from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_simplemde import SimpleMDE
import os
from flask_uploads import UploadSet, configure_uploads, IMAGES


# app initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pitch.db'


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


# flask extensions initialization
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
simple = SimpleMDE(app)

photos = UploadSet('photos', IMAGES)

app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT='587',
MAIL_USE_TLS=True,
MAIL_USERNAME=os.environ.get('EMAIL_USER'),
MAIL_PASSWORD=os.environ.get('EMAIL_PASS')
)

def create_app(config_name):
    # app configurations
    app.config.from_object(config_options[config_name])
    
    
    
    #mail instance
    
    
    
    #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app


# def create_database(app):
#     if not path.exists('app/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')
