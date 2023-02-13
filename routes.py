from flask import Blueprint

api = Blueprint('api', __name__) 

# add new endpoints like this:
# @api.route('/whatever')
# def whatever():
#     return "whatever"