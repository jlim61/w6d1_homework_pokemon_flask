from flask_smorest import Blueprint
#      args =   name,     dunder,      url_prefix
bp = Blueprint('pokemon', __name__, url_prefix='/pokemon')

from . import routes