from flask import Flask
from config import Config

# This is the heart of the application factory pattern, our entry point to the application
# This is where we initialize the Flask application and all the Flask extensions
# This file will import all other files and packages; No other file can import from this file.
# This is to avoid circular imports

from app.extensions import db

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config) # Loading the config file

    # Initializing Flask extensions here

    # Flask SQLAlchemy
    db.init_app(app)

    # Creating the database tables (if not present)

    # Import your models here
    # from app.models.model_filename import model_name
    # ...
    
    with app.app_context():
        db.create_all()
    

    # Registering the blueprints here

    from app.module1 import bp as module1_bp
    app.register_blueprint(module1_bp)

    from app.module2 import bp as module2_bp
    app.register_blueprint(module2_bp)

    from app.module3 import bp as module3_bp
    app.register_blueprint(module3_bp)
    
    # Register any extra modules/blueprints created here
    # ...
    
    @app.route('/')
    def home():
        return '<h1>This application was bootstrapped using Flask-Application-Factory-Pattern-Template!</h1>'

    return app