# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
import os
#SDL_SetHint(SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS,"1");
os.environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
bl_info = {
    "name" : "Blendercontroller",
    "author" : "HorseyTime",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}
from . HorseyTime_Settings import  TESTADDON_PT_TestPanel, TESTADDON_PT_sub_panel
from . HorseyTime_Settings import MyMaterialProps, MyFloatProp, AxisProps
from . HorseyTimeCloseWindowButton import CloseWindowOperator
from . HorseyTimeSpawnController import SpawnButtonsOperator
classes = {TESTADDON_PT_TestPanel, CloseWindowOperator, SpawnButtonsOperator}

def register():
    import os
    os.environ['SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
    bpy.utils.register_class(AxisProps)
    bpy.utils.register_class(MyMaterialProps)
    #1bpy.utils.register_class(MyFloatProp)
    bpy.types.Scene.my_custom_props= bpy.props.CollectionProperty(type=MyMaterialProps)
    bpy.types.Scene.my_axis= bpy.props.CollectionProperty(type=AxisProps)
    #bpy.types.Object.my_settings = bpy.props.CollectionProperty(type=MyFloatProp)
    
    
    for c in classes:
        print(f"Register ~~~~~~~~~~~~~~~ {c}")
        bpy.utils.register_class(c)
    bpy.utils.register_class(TESTADDON_PT_sub_panel)
#bpy.context.object.my_settings.add()




def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.my_custom_props
    del bpy.types.Scene.my_axis
    #del bpy.types.Object.my_settings 
    bpy.utils.unregister_class(TESTADDON_PT_sub_panel)
    
    bpy.utils.unregister_class(MyMaterialProps)
    bpy.utils.unregister_class(AxisProps)
