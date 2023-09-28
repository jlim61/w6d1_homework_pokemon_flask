from app import db
from datetime import datetime

class PokemonModel(db.Model):

    __tablename__ = 'pokemon'

    id = db.Column(db.Integer, primary_key=True)
    pokemon_species = db.Column(db.String, nullable = False)
    caught = db.Column(db.String, default=datetime.utcnow)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.id'), nullable = False)

    def __repr__(self):
        return f'<Pokemon: {self.pokemon_species}>'
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()