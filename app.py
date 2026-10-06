"""
Smart Healthcare Management System
Main Flask Application Entry Point
"""

from flask import Flask
from config import Config
from routes.main_routes import main_bp
from routes.prediction_routes import prediction_bp
from routes.blog_routes import blog_bp


def create_app(config_class=Config):
    """Application factory pattern."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(prediction_bp, url_prefix="/predict")
    app.register_blueprint(blog_bp, url_prefix="/blog")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=5000)









