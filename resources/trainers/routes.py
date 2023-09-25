from flask import request
from uuid import uuid4

from app import app

from db import trainers, pokemon

@app.get('/trainers')
def get_trainers():
    return {'trainers': trainers},200

@app.get('/trainers/<trainer_id>')
def get_trainer(trainer_id):
    try:
        trainer = trainers[trainer_id]
        return trainer, 200
    except KeyError:
        return {'message': 'trainer not found'}, 400

@app.post('/trainers')
def create_trainer():
    trainer_data = request.get_json()
    trainers[uuid4().hex] = trainer_data
    return trainer_data, 201

@app.put('/trainers/<trainer_id>')
def update_trainer(trainer_id):
    trainer_data = request.get_json()
    try:
        trainer = trainers[trainer_id]
        trainer['name'] = trainer_data['name']
        return trainer, 200
    except KeyError:
        return {'message': 'trainer not found'}, 400

@app.delete('/trainers/<trainer_id>')
def delete_trainer(trainer_id):
  try:
    deleted_trainer = trainers.pop(trainer_id)
    return {'message':f'{deleted_trainer["name"]} deleted'}, 202
  except KeyError:
    return {'message': 'Trainer not found'}, 400


@app.get('/trainers/<trainer_id>/pokemon')
def get_trainer_pokemon(trainer_id):
    if trainer_id not in trainers:
        return {'message': 'trainer not found'}, 400
    trainer_pokemon = [pokemon for pokemon in pokemon.values() if pokemon['trainer_id'] == trainer_id]
    return trainer_pokemon, 200