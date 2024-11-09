import bpy
import os
os.environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
import pygame
from . HorseyTimeCloseWindowButton import CloseWindowOperator
from . HorseyTimeSpawnController import SpawnButtonsOperator
def update_func(self, context):
        print("my test function", self)
class MyFloatProp(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(default="")
    value: bpy.props.FloatProperty(default=0)

class MyMaterialProps(bpy.types.PropertyGroup):
    
    
    TrueFalse: bpy.props.BoolProperty(name="TrueFalse", default=False, update=update_func)  
class AxisProps(bpy.types.PropertyGroup):
    
    
    OneToNegOne: bpy.props.FloatProperty(name="TrueFalse", default=0, min = -1, max = 1, update=update_func)  
    

class TESTADDON_PT_TestPanel(bpy.types.Panel):
   
        
    bl_idname = "TESTADDON_PT_TestPanel"
    bl_label = "ControllerTest"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "ControllerTes"
    bl_context = "objectmode"
    
    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        
        
        column = layout.column()
        row = layout.row()
        row.operator(CloseWindowOperator.bl_idname, text= "ToggleButton?")
        row.operator(SpawnButtonsOperator.bl_idname, text="SpawnObjectsControls" )
    
class TESTADDON_PT_sub_panel(bpy.types.Panel):
    bl_label = "Buttons And Axeses"
    bl_idname = "TESTADDON_PT_sub_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Object Tools"
    bl_context = "objectmode"
    bl_parent_id = "TESTADDON_PT_TestPanel"

    def draw(self, context):
        layout = self.layout
        layout.label(text="SUBBY")
        layout.prop(bpy.context.scene,"my_custom_props")
        i=0
        for button in bpy.context.scene.my_custom_props:
            i+=1
            layout.prop(button, "TrueFalse",text=f"Button {i}")
        i=0

        for axis in bpy.context.scene.my_axis:
            i+=1
            layout.prop(axis, "OneToNegOne",text=f"Axis {i}")