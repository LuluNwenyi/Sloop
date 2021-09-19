###########################################
################ IMPORTS ##################
###########################################

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_manager
from .config import config, DevelopmentConfig, ProductionConfig
from flask_mail import Mail
from datetime import timedelta


# TOKEN EXPIRY TIME
ACCESS_EXPIRES = timedelta(hours=24)

# APP CONFIG
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
jwt = JWTManager(app)
mail = Mail(app)

# APP FACTORY
def create_app(config_name):

    # INIT APP CONFiG IN APP
    app.config.from_object(config[config_name])

    # INIT APP IN MANAGERS
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)
    mail.init_app(app)

    # REGISTRATION OF BLUEPRINTS
    from api.views import default as default_blueprint
    from api.authentication.routes import auth as auth_blueprint
    from api.user.routes import user as user_blueprint
    from api.creator.routes import creator as creator_blueprint

    app.register_blueprint(default_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(creator_blueprint)

    return app
