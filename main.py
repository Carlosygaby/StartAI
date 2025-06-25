from flask import Flask
from instance.config import Config
from flask_sqlalchemy import SQLAlchemy
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from app.models.models import User,Product,MarketCategory,ProductCategory,DataSource,ProductDataSource,Survey,SurveyQuestion,SurveyAnswer,Chat,ChatMenssage,Comentary,Reaction,ProductImage,Favorite,Notification,Rating,Suscription,Payment
        db.create_all()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)