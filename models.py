from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from sqlalchemy import Enum
import os
import enum

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 


#  setting app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BASE_DIR, 'db.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Simple Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/doc/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/docs/'  # URI to access UI of API Doc
})

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
docs = FlaskApiSpec(app)
api =  Api(app)


#  creating models
class User(db.Model):

   # class GenderEnum(enum.Enum):
   #    male='male'
   #    female='female'


   id = db.Column(db.Integer,primary_key=True,autoincrement=True)
   name = db.Column(db.String(100))
   mobile = db.Column(db.String(10),unique=True)
   gender = db.Column(db.String(10))
