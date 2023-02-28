import mongoengine as me
from flask_mongoengine import MongoEngine

db = MongoEngine()

# example model
# class Account(me.Document):
#     username = me.StringField(required=True)
#     strategies = me.ListField(default=[])