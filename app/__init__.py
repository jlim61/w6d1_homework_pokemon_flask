from flask import Flask, request
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)

from resources.trainers import bp as trainer_bp
api.register_blueprint(trainer_bp)

from resources.pokemon import bp as pokemon_bp
api.register_blueprint(pokemon_bp)

from resources.trainers import routes
from resources.pokemon import routes

from resources.trainers.TrainerModel import TrainerModel
from resources.pokemon.PokemonModel import PokemonModel