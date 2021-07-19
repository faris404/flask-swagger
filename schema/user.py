from models import User,ma
from marshmallow_sqlalchemy import fields
from marshmallow import fields, Schema

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class UserPostSchema(ma.SQLAlchemyAutoSchema):
   name = fields.Str(required=True)
   mobile = fields.Str(required=True)
   gender = fields.Str(required=True)