from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class TrainerModel(db.Model):

    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key = True)
    pc_name = db.Column(db.String, unique = True, nullable = False)
    hometown = db.Column(db.String)
    pc_password_hash = db.Column(db.String, nullable = False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)

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