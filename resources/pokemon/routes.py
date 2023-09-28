from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from flask_jwt_extended import get_jwt_identity, jwt_required, get_jwt

from resources.trainers.TrainerModel import TrainerModel

from sqlalchemy.exc import IntegrityError
from schemas import PokemonSchema
from .PokemonModel import PokemonModel
from . import bp
from db import pokemon

@bp.route('/')
class PokemonList(MethodView):

    # get all pokemon
  @jwt_required()
  @bp.response(200, PokemonSchema(many=True))
  def get(self):
    return PokemonModel.query.all()
  
  # create pokemon
  @jwt_required()
  @bp.arguments(PokemonSchema)
  @bp.response(200, PokemonSchema)
  def post(self, pokemon_data):
      trainer_id = get_jwt_identity()
      p = PokemonModel(**pokemon_data, trainer_id = trainer_id)
      try:
          p.save()
          return p
      except IntegrityError:
          abort(400, message='Invalid Trainer ID')

@bp.route('/<pokemon_id>')
class Pokemon(MethodView):

    # get one pokemon
  @jwt_required()
  @bp.response(200, PokemonSchema)
  def get(self, pokemon_id):
    p = PokemonModel.query.get(pokemon_id)
    if p:
      return p
    abort(400, message='Invalid Pokemon ID')

# edit/evolve a pokemon
  @jwt_required()
  @bp.arguments(PokemonSchema)
  @bp.response(200, PokemonSchema)
  def put(self, pokemon_data, pokemon_id):
    p = PokemonModel.query.get(pokemon_id)
    if p and pokemon_data['pokemon_species']:
      trainer_id = get_jwt_identity()
      if p.trainer_id == trainer_id:
        p.pokemon_species = pokemon_data['pokemon_species']
        p.save()
        return p
      else:
        abort(401, message='That\'s not your Pokemon!')
    abort(400, message='Invalid Pokemon Data')

# release/delete a pokemon
  @jwt_required()
  def delete(self, pokemon_id):
    trainer_id = get_jwt_identity()
    p = PokemonModel.query.get(pokemon_id)
    if p:
      if p.trainer_id == trainer_id:
        p.delete()
        return {'message': 'Pokemon was released'}, 202
      abort(400, message='You can\'t release another trainer\'s Pokemon!')
    abort(400, message='Invalid Pokemon ID')