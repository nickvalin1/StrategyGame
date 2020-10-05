from model import gamemap, unit, party

petus = unit.Unit("Petus", None, {"move": 5})
rhea = unit.Unit("Rhea", None, {"move": 5})

party = party.Party([petus, rhea], leader=petus)

prologue = gamemap.GameMap("../assets/model_map.json")

for i in range(prologue.units):
    party.units[i].reposition(*prologue.starting_positions[i], prologue.grid)

options = rhea.get_movement_options(prologue)
