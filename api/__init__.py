from flask import Flask
from flask_cors import CORS
from config import Config

from .routes.user_bp import users_bp
from .routes.servidor_bp import servidor_bp
from .routes.canal_bp import canal_bp
from .routes.mensaje_bp import mensaje_bp
from .routes.auth_bp import auth_bp
from .database import DatabaseConnection

def init_app():
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(users_bp, url_prefix = '/users')
    app.register_blueprint(servidor_bp, url_prefix = '/servidor')
    app.register_blueprint(canal_bp, url_prefix = '/canal')
    app.register_blueprint(mensaje_bp, url_prefix = '/mensaje')
    app.register_blueprint(auth_bp, url_prefix = '/auth')

    return app