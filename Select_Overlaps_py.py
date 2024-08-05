import unreal

unreal.SystemLibrary.begin_transaction('SelectOverlaps', "Desc", None)

locations = []
actors = []
names = []
seen = set()
dupes = []

ELL = unreal.EditorLevelLibrary
EAS = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
selection = EAS.get_selected_level_actors()

for actor in selection:
    EAS.set_actor_selection_state(actor, False)
    actorLoc = actor.get_actor_location()
    actorLoc2 = round((actorLoc.x - actorLoc.y + actorLoc.z), 2)
    locations.append(actorLoc2)
    #name = actor.get_actor_label()
    actors.append(actor)
    #names.append(name)


for x in locations:
    #print(x, '  X')
    if x in seen:
        dupes.append(x)
        #print("1 SEEN IS  ==  ", seen)
    else:
        seen.add(x)
        #print("2 SEEN IS  ==  ", seen)

#print("NAMES  ", names)
#print ("LOCATIONS  ", locations)
print ("DUPLICATES  ", dupes)
#print ("DUPLICATES NAMES  ", names.index())

for dupe in dupes:
    actorToSelect = actors[locations.index(dupe)]
    EAS.set_actor_selection_state(actorToSelect, True)

unreal.SystemLibrary.end_transaction()