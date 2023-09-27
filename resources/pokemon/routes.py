from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort
from resources.pokemon import PokemonModel
from resources.trainers import TrainerModel

from schemas import PokemonSchema
from . import bp
from app import app
from db import pokemon

@bp.route('/')
class PokemonList(MethodView):
    # get all pokemon
  @bp.resposne(200, PokemonSchema(many=True))
  def get_pokemon(self):
    return PokemonModel.query.all()
  
  # create pokemon
  @bp.arguments(PokemonSchema)
  @bp.response(200, PokemonSchema)
  def post(self, pokemon_data):
    p = PokemonModel(**pokemon_data)
    t = TrainerModel.query.get(pokemon_data['trainer_id'])
    if t:
      p.save()
      return p
    else:
      abort(400, message='Invalid Trainer ID')

@bp.route('/<pokemon_id>')
class Pokemon(MethodView):

    # get one pokemon
  @bp.response(200, PokemonSchema)
  def get(self, pokemon_id):
    p = PokemonModel.query.get(pokemon_id)
    if p:
      return p
    abort(400, message='Invalid Pokemon ID')

# edit/evolve a pokemon
  @bp.arguments(PokemonSchema)
  @bp.response(200, PokemonSchema)
  def put(self, pokemon_data, pokemon_id):
    p = PokemonModel.query.get(pokemon_id)
    if p and pokemon_data['pokemon_species']:
      if p.trainer_id == pokemon_data['trainer_id']:
        p.pokemon_species = pokemon_data['pokemon_species']
        p.save()
        return p
      abort(400, message='Invalid Pokemon Data')

# release/delete a pokemon
  def delete(self, pokemon_id):
    request_data = request.get_json()
    trainer_id = request_data['trainer_id']
    pokemon_name = request_data['pokemon_species']
    p = PokemonModel.query.get(pokemon_id)
    if p:
      if p.trainer_id == trainer_id:
        p.delete()
        return {'message': f'{pokemon_name} was released'}
      abort(400, message='You can\'t release another trainer\'s Pokemon!')
    abort(400, message='Invalid Pokemon ID')