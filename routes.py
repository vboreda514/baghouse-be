from flask import Blueprint, request
from models import Account

api = Blueprint('api', __name__) 

# add new endpoints like this:
# @api.route('/whatever')
# def whatever():
#     name = request.args.get("name")
#     return "whatever"