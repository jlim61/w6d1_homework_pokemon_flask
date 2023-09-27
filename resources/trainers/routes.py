from flask import request
from flask.views import MethodView
from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from schemas import TrainerSchema, UpdateTrainerSchema, PokemonSchema, DeleteTrainerSchema
from . import bp
from .TrainerModel import TrainerModel
from db import trainers, pokemon

@bp.route('/trainers')
class TrainerList(MethodView):
    # get all trainers
    @bp.response(200, TrainerSchema(many=True))
    def get(self):
        return TrainerModel.query.all()
    
    # create trainer
    @bp.arguments(TrainerSchema)
    @bp.response(201, TrainerSchema)
    def post(self, trainer_data):
        trainer = TrainerModel()
        trainer.from_dict(trainer_data)
        try:
            trainer.save()
            return trainer_data
        except IntegrityError:
            abort(400, message='PC Name already taken')

    # delete trainer
    @bp.arguments(DeleteTrainerSchema)
    def delete(self, trainer_data):
        trainer = TrainerModel.query.filter_by(pc_user=trainer_data['pc_name']).first()
        if trainer and trainer.check_pc_password(trainer_data['pc_password']):
            trainer.delete()
            return {'message': f'{trainer_data["pc_name"]} deleted'}, 202
        abort(400, message='PC Name or PC Password Invalid')


@bp.route('/trainers/<trainer_id>')
class Trainer(MethodView):

    # get a trainer
    @bp.response(200, TrainerSchema)
    def get(self, trainer_id):
        trainer = TrainerModel.query.get_or_404(trainer_id, description='User Not Found')
        return trainer

    # edit a trainer
    @bp.arguments(UpdateTrainerSchema)
    @bp.response(200, TrainerSchema)
    def put(self, trainer_data, trainer_id):
        trainer = TrainerModel.query.get_or_404(trainer_id, description='User Not Found')
        if trainer and trainer.check_pc_password(trainer_data['pc_password']):
            try:
                trainer.from_dict(trainer_data)
                trainer.save()
            except IntegrityError:
                abort(400, message='PC Name already taken')

@bp.get('/trainers/<trainer_id>/pokemon')
@bp.response(200, PokemonSchema(many=True))
def get_trainer_pokemon(trainer_id):
    if trainer_id not in trainers:
        return {'message': 'trainer not found'}, 400
    trainer_pokemon = [pokemon for pokemon in pokemon.values() if pokemon['trainer_id'] == trainer_id]
    return trainer_pokemon, 200

@bp.route('/user/register/<registering_id>/<registered_id>')
class RegisterTrainer(MethodView):

    # register trainer
    @bp.response(200, TrainerSchema(many=True))
    def post(self,registering_id,registered_id):
        trainer = TrainerModel.query.get(registering_id)
        trainer_to_register = TrainerModel.query.get(registered_id)
        if trainer and trainer_to_register:
            trainer.register_trainer(trainer_to_register)
            return trainer.trainers_registered.all()
        abort(400, message='Invalid Trainer Info')

    # unregister trainer
    @bp.response(200, TrainerSchema(many=True))
    def post(self,registering_id,registered_id):
        trainer = TrainerModel.query.get(registering_id)
        trainer_to_unregister = TrainerModel.query.get(registered_id)
        if trainer and trainer_to_unregister:
            trainer.unregister_trainer(trainer_to_unregister)
            return {'message': f'Trainer: {trainer_to_unregister.pc_user} unregistered'}, 202
        abort(400, message='Invalid Trainer Info')