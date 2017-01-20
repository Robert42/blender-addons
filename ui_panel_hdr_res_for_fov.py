bl_info = {
    "name": "Required Env-Map Resolution",
    "author": "Robert Hildebrandt",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "Properties > Data (Camera Only) > Required Env-Map Resolution",
    "description": "Creates a Panel guessing the minimum environment map resolution",
    "warning": "The formula is more a rough estimate than scientific prooven.",
    "wiki_url": "",
    "tracker_url": "https://github.com/Robert42/blender-addons/issues",
    "category": "Object",
    }

import bpy
from mathutils import *
from math import *

class HdrResPanel(bpy.types.Panel):
    """Creates a Panel guessing the minimum environment map resolution"""
    bl_label = "Required Env-Map Resolution"
    bl_idname = "OBJECT_PT_envmap_resolution_for_fov"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    
    @classmethod
    def poll(self, context):
        return context.camera

    def draw(self, context):
        layout = self.layout

        obj = context.object
        
        camera = obj
        render_resolution = Vector((context.scene.render.resolution_x, context.scene.render.resolution_y)) * context.scene.render.resolution_percentage / 100.
        
        fov_h = camera.data.angle_x
        fov_v = camera.data.angle_y
    
        layout.label(text="Required Env-Map Resolution", icon='WORLD_DATA')
        
        min_env_resolution_x = int(ceil(render_resolution.x * 2. * pi / fov_h))
        min_env_resolution_y = int(ceil(render_resolution.y * 1. * pi / fov_v))
        
        layout.label(text=" {}x{}".format(min_env_resolution_x, min_env_resolution_y))
                


def register():
    bpy.utils.register_class(HdrResPanel)


def unregister():
    bpy.utils.unregister_class(HdrResPanel)


if __name__ == "__main__":
    register()
