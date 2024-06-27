from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    # Register blueprints
    from app.routes.main_bp import main_bp
    app.register_blueprint(main_bp)

    # Additional setup can go here (e.g., error handlers, CLI commands)

    return app

# Import models to ensure they are registered with SQLAlchemy
from app import models