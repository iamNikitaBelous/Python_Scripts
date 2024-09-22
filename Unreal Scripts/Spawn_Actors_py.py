import unreal

def spawnReflections() :
    selection = unreal.EditorLevelLibrary.get_selected_level_actors()
    spawnable = unreal.SphereReflectionCapture()
    imgTime = '' # image time postfix '_Day' or '_Night'

    try:
        for actor in selection:
            actorIndex = actor.get_component_by_class(unreal.TextRenderComponent).get_editor_property('Text')
            actorIndex = str(actorIndex).split('Index_', 1)[-1]
            actorLoc = actor.get_actor_location()
            actorRot = actor.get_actor_rotation()
            spawned = unreal.EditorLevelLibrary.spawn_actor_from_object(spawnable, actorLoc, actorRot)

            spawned.set_actor_label(('SphereReflectionCapture_') + actorIndex + imgTime)

            spawnedChild = spawned.get_component_by_class(unreal.SphereReflectionCaptureComponent)
            spawnedChild.set_editor_property('ReflectionSourceType', unreal.ReflectionSourceType.SPECIFIED_CUBEMAP) #RS_SpecifiedCubemap
            spawnedChild.set_editor_property('InfluenceRadius', 700.0)

            cubemap = unreal.EditorAssetLibrary.load_asset('/Game/Blueprints/Cubemaps/Cubemap_' + actorIndex + imgTime)

            spawnedChild.set_editor_property('Cubemap', cubemap)
            
            unreal.log('All Spawned! ')
    except:
        unreal.log('Failed to Spawn! ')

spawnReflections()


unreal.log("End! ")
