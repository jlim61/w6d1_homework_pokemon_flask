# connecting to db
# in terminal run:
# flask db init
# flask db migrate -m "message"
# flask db upgrade

trainers = {
    '1':{
        'pc_name': 'Brock\'s PC',
        'trainer_type': 'Gym Leader',
        'hometown': 'Pewter City',
        'pc_password': 'rockpokemon'
    },
    '2':{
        'pc_name': 'Misty\'s PC',
        'trainer_type': 'Gym Leader',
        'hometown': 'Cerulean City',
        'pc_password': 'misty123'
    },
    '3':{
        'pc_name': 'Gary\'s PC',
        'trainer_type': 'Researcher, former trainer',
        'hometown': 'Pallet Town',
        'pc_password': 'smellyalater'
    }
}

pokemon = {
    '1':{
        'pokemon_species': 'Onix',
        'trainer_id': '1'
    },
    '2':{
        'pokemon_species': 'Geodude',
        'trainer_id': '1'
    },
    '3':{
        'pokemon_species': 'Starmie',
        'trainer_id': '2'
    },
    '4':{
        'pokemon_species': 'Togepi',
        'trainer_id': '2'
    },
    '5':{
        'pokemon_species': 'Blastoise',
        'trainer_id': '3'
    },
    '6':{
        'pokemon_species': 'Umbreon',
        'trainer_id': '3'
    }
}