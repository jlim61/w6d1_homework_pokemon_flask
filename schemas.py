from marshmallow import Schema, fields

class PokemonSchema(Schema):
    # when we make id, we get id. if we are requesting info, id not required
    id = fields.Str(dumps_only=True)
    pokemon_species = fields.Str(required=True)
    trainer_id = fields.Str(required=True)

class TrainerSchema(Schema):
    id = fields.Str(dumps_only=True)
    pc_name = fields.Str(required=True)
    hometown = fields.Str(required=True)
    pc_password = fields.Str(required=True)
    # taking an optional first name, last name
    first_name = fields.Str()
    last_name = fields.Str()

class UpdateTrainerSchema(Schema):
  pc_name = fields.Str()
  hometown = fields.Str()
  pc_password = fields.Str(required = True)
  new_pc_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class DeleteTrainerSchema(Schema):
   pc_name = fields.Str(required=True)
   pc_password = fields.Str(required=True)