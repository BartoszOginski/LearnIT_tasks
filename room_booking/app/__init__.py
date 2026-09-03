from flask import Flask
from app.extensions import db


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # Blueprint dashboardu
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app