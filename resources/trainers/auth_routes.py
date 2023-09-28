from flask_smorest import abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token

from schemas import AuthTrainerSchema, TrainerSchema
from . import bp
from .TrainerModel import TrainerModel

@bp.post('/initiate')
@bp.arguments(TrainerSchema)
@bp.response(200, TrainerSchema)
def initiate_trainer(trainer_data):
    trainer = TrainerModel()
    trainer.from_dict(trainer_data)
    try:
        trainer.save()
        return trainer
    except IntegrityError:
        abort(400, message='PC Name already taken')

@bp.post('/login')
@bp.arguments(AuthTrainerSchema)
def login(login_info):
    if 'pc_user' not in login_info:
        abort(400, message='Please include pc_user')
    if 'pc_user' in login_info:
        trainer = TrainerModel.query.filter_by(pc_user=login_info['pc_user']).first()
    if trainer and trainer.check_pc_password(login_info['pc_password']):
        access_token = create_access_token(identity=trainer.id)
        return {'access_token': access_token}
    abort(400, message='Invalid PC User or Password')