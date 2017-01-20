bl_info = {
    "name": "Calc Required Env-Map Resolution",
    "author": "Robert Hildebrandt",
    "version": (1, 0),
    "blender": (2, 75, 0),
    "location": "Properties > Data (Camera Only) > Required Env-Map Resolution",
    "description": "Creates a Panel guessing the minimum environment map resolution",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
    }

import bpy
from mathutils import *
from math import *

class HdrResPanel(bpy.types.Panel):
    """Creates a Panel guessing the minimum environment map resolution"""
    bl_label = "Required Env-Map Resolution"
    bl_idname = "OBJECT_PT_hello"
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
        min_env_resolution_x = int(ceil(render_resolution.x * 2. * pi / camera.data.angle_x))
        min_env_resolution_y = int(ceil(render_resolution.y * 1. * pi / camera.data.angle_y))

        row = layout.row()
        row.label(text="Required Env-Map Resolution: {}x{}".format(min_env_resolution_x, min_env_resolution_y), icon='WORLD_DATA')
        


def register():
    bpy.utils.register_class(HdrResPanel)


def unregister():
    bpy.utils.unregister_class(HdrResPanel)


if __name__ == "__main__":
    register()
