bl_info = {
    "name": "Required Env-Map Resolution",
    "author": "Robert Hildebrandt",
    "version": (0, 5),
    "blender": (2, 75, 0),
    "location": "Properties > Data (Camera Only) > Required Env-Map Resolution",
    "description": "Creates a Panel guessing the minimum environment map resolution",
    "warning": "The results of this add-on need to be validated by a test.",
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
        
        fov_h = camera.data.angle_x
        fov_v = camera.data.angle_y
    
        layout.label(text="Required Env-Map Resolution", icon='WORLD_DATA')
        
        min_env_resolution_x = int(ceil(render_resolution.x * 2. * pi / fov_h))
        min_env_resolution_y = int(ceil(render_resolution.y * 1. * pi / fov_v))
        
        layout.label(text="Required resolution, when you never roll the camera:")
        layout.label(text=" {}x{}".format(min_env_resolution_x, min_env_resolution_y))
        
        fov = min(fov_h, fov_v)
        min_env_resolution_x = int(ceil(render_resolution.x * 2. * pi / fov))
        min_env_resolution_y = int(ceil(render_resolution.y * 1. * pi / fov))
        layout.label(text="Required resolution, when potentially roll the camera:")
        layout.label(text=" {}x{}".format(min_env_resolution_x, min_env_resolution_y))
                


def register():
    bpy.utils.register_class(HdrResPanel)


def unregister():
    bpy.utils.unregister_class(HdrResPanel)


if __name__ == "__main__":
    register()
