from app import db

from werkzeug.security import generate_password_hash, check_password_hash

registering_trainers = db.table('registering_trainers',
    db.Column('registering_id', db.Integer, db.ForeignKey('trainers.id')),
    db.Column('registered_id', db.Integer, db.ForeignKey('trainers.id'))
    )

class TrainerModel(db.Model):

    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key = True)
    pc_user = db.Column(db.String, unique = True, nullable = False)
    hometown = db.Column(db.String)
    pc_password_hash = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    owned_pokemon = db.relationship('PokemonModel', backref='trainer', lazy='dynamic', cascade='all, delete')
    trainers_registered = db.relationship('TrainerModel',
        secondary=registering_trainers,
        primaryjoin = registering_trainers.c.registering_id == id,
        secondaryjoin = registering_trainers.c.registered_id == id,
        backref = db.backref('registered', lazy='dynamic'),
        lazy='dynamic'
    )


    def __repr__(self):
        return f'<Trainer: {self.pc_name}'
    
    def hash_pc_password(self, pc_password):
        self.pc_password_hash = generate_password_hash(pc_password)

    def check_pc_password(self, pc_password):
        return check_password_hash(self.pc_password_hash, pc_password)
    
    def from_dict(self, dict):
        pc_password = dict.pop('pc_password')
        self.hash_pc_password(pc_password)
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def is_registered(self,trainer):
        return self.trainers_registered.filter(trainer.id == registering_trainers.c.registered_id).count() > 0

    def register_trainer(self, trainer):
        if not self.is_registered(trainer):
            self.trainers_registered.append(trainer)
            self.save()

    def unregister_trainer(self,trainer):
        if self.is_registered:
            self.trainers_registered.remove(trainer)
            self.save()