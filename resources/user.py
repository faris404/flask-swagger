from flask_restful import Resource
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from flask import jsonify,request
from marshmallow import fields
from models import User,db
from schema.user import *

class Users(MethodResource,Resource):


   @marshal_with(UserPostSchema)
   def get(self):
      user_schema = UserSchema(many=True)
      data = User.query.all()
      print(data)
      res = user_schema.dump(data)
 
      return jsonify(res)


   @use_kwargs(UserPostSchema(),location=('json'))
   @use_kwargs({'test':fields.Str()},location=('query'))
   def post(self,**kwargs):
      try:
         
         # data = request.get_json()
         print(kwargs)
         user = User(**kwargs)
         db.session.add(user)
         db.session.commit()
      except Exception as e:
         print(e)
         return 'error'