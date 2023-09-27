from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from schemas import PokemonSchema
from . import bp
from app import app
from db import pokemon

@bp.route('/')
class PokemonList(MethodView):
    # get all pokemon
  def get_pokemon(self):
    return {'pokemon': pokemon}
  
  # create pokemon
  @bp.arguments(PokemonSchema)
  def post(self, pokemon_data):
    pokemon[uuid4().hex] = pokemon_data
    return pokemon_data, 201

@bp.route('/<pokemon_id>')
class Pokemon(MethodView):

    # get one pokemon
  def get(self, pokemon_id):
    try:
      mon = pokemon[pokemon_id]
      return mon, 200
    except KeyError:
      abort(404, message='Pokemon Not Found')

# edit a pokemon
  @bp.arguments(PokemonSchema)
  def put(self, pokemon_data, pokemon_id):
    if pokemon_id in pokemon:
      mon = pokemon[pokemon_id]
      if pokemon_data['trainer_id'] != mon['trainer_id']:
        abort(400, message='That\'s not your Pokemon!')
      mon['pokemon_species'] = pokemon_data['pokemon_species']
      return mon, 200
    abort(404, message='Pokemon Not Found')

# release/delete a pokemon
  def delete(self, pokemon_id):
    try:
      deleted_pokemon = pokemon.pop(pokemon_id)
      return {'message':f'{deleted_pokemon["pokemon_species"]} was released!'}, 202
    except KeyError:
      abort(404, message='Pokemon Not Found')