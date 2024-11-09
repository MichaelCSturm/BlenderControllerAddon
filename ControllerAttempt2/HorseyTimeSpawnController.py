import bpy
import os
os.environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
import pygame

class SpawnButtonsOperator(bpy.types.Operator):
    bl_idname = "wm.ayo"
    bl_label = "Minimal Operator"

    def execute(self, context):
        print("Hello World")
        bpy.context.object.my_custom_props.clear()
        
        iiii = 0
        NumButtonIlist = []
        while iiii < pygame.joystick.Joystick(0).get_numbuttons():
            NumButtonIlist.append(iiii)
            NumButtonIlist[iiii] = bpy.context.object.my_custom_props.add()
            
            #print(f"\n\n\n HERE HERE THE TOWN CRIER SAYS HEY WE CREATED This manyy proporites  \n\n\n HERE HERE")
            iiii+=1
        
        return {'FINISHED'}
def in_2_seconds():
    bpy.context.scene.my_custom_props.clear()
    bpy.context.scene.my_axis.clear()    
    iiii = 0
    NumButtonIlist = []
    while iiii < pygame.joystick.Joystick(0).get_numbuttons():
            NumButtonIlist.append(iiii)
            NumButtonIlist[iiii] = bpy.context.scene.my_custom_props.add()
            
            #print(f"\n\n\n HERE HERE THE TOWN CRIER SAYS HEY WE CREATED This manyy proporites  \n\n\n HERE HERE")
            iiii+=1
    iiii = 0
    while iiii < pygame.joystick.Joystick(0).get_numaxes():
        NumButtonIlist.append(iiii)
        NumButtonIlist[iiii] = bpy.context.scene.my_axis.add()
        iiii+=1

bpy.app.timers.register(in_2_seconds, first_interval=2)