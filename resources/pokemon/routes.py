from flask import request
from uuid import uuid4

from app import app

from db import pokemon

@app.get('/pokemon')
def get_pokemon():
  return {'pokemon': pokemon}

@app.get('/pokemon/<pokemon_id>')
def get_one_pokemon(pokemon_id):
  try:
    mon = pokemon[pokemon_id]
    return mon, 200
  except KeyError:
    return {'message': 'Pokemon not found'}, 400

@app.post('/pokemon')
def create_pokemon():
  pokemon_data = request.get_json()
  pokemon[uuid4().hex] = pokemon_data
  return pokemon_data, 201

@app.put('/pokemon/<pokemon_id>')
def edit_pokemon(pokemon_id):
  pokemon_data = request.get_json()
  if pokemon_id in pokemon:
    mon = pokemon[pokemon_id]
    mon['pokemon'] = pokemon_data['pokemon']
    print(pokemon)
    return mon, 200
  return {'message': 'pokemon not found'}, 400

@app.delete('/pokemon/<pokemon_id>')
def delete_pokemon(pokemon_id):
  try:
    deleted_pokemon = pokemon.pop(pokemon_id)
    return {'message':f'{deleted_pokemon["pokemon"]} deleted'}, 202
  except KeyError:
    return {'message': 'Pokemon not found'}, 400