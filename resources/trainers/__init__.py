from flask_smorest import Blueprint
#       args =    name,   dunder, (third optional arg)
bp = Blueprint('trainers', __name__, description='Ops on trainers')

from . import routes, auth_routes