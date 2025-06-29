from flask import Flask
from instance.config import Config
from app.models import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate= Migrate(app,db,render_as_batch=False)
    from app.routes.users import auth
    app.register_blueprint(auth)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)