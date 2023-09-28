from marshmallow import Schema, fields

class PokemonSchema(Schema):
    # when we make id, we get id. if we are requesting info, id not required
    id = fields.Str(dumps_only=True)
    pokemon_species = fields.Str(required=True)
    trainer_id = fields.Int(required=True)
    caught = fields.Str(dump_only=True)

class TrainerSchema(Schema):
    id = fields.Str(dumps_only=True)
    pc_user = fields.Str(required=True)
    trainer_type = fields.Str()
    hometown = fields.Str()
    pc_password = fields.Str(required=True, load_only = True)
    # taking an optional first name, last name
    first_name = fields.Str()
    last_name = fields.Str()


class TrainerPokedex(TrainerSchema):
   pc = fields.List(fields.Nested(TrainerSchema), dump_only=True)
   registered_pokemon = fields.List(fields.Nested(PokemonSchema), dump_only=True)

class UpdateTrainerSchema(Schema):
  pc_user = fields.Str()
  hometown = fields.Str()
  pc_password = fields.Str(required = True, load_only = True)
  new_pc_password = fields.Str()
  first_name = fields.Str()
  last_name = fields.Str()

class DeleteTrainerSchema(Schema):
   pc_user = fields.Str(required=True)
   pc_password = fields.Str(required=True, load_only = True)
