from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

from .chat import Chat, ChatMenssage
from .comentary import Comentary
from .data_source import DataSource
from .favorite import Favorite
from .notification import Notification
from .product import Product, ProductCategory, ProductDataSource,ProductImage,MarketCategory
from .rating import Rating
from .reaction import Reaction
from .survey import Survey, SurveyQuestion, SurveyAnswer
from .suscription import Suscription, Payment
from .trend_analysis import TrendAnalysis
from .user import User 