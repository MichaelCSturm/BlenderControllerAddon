import bpy
import os
os.environ['SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS'] = '1'
import pygame
import queue


pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    
pygame.joystick.Joystick(0).init()

print(f" Get num axes {pygame.joystick.Joystick(0).get_numaxes()}")

print(f" Get numballs {pygame.joystick.Joystick(0).get_numballs()}")


print(f" Get numhats {pygame.joystick.Joystick(0).get_numhats()}")

print(f" Get NumButtons {pygame.joystick.Joystick(0).get_numbuttons()}")


# iiii = 0
# NumButtonIlist = []
# while iiii < pygame.joystick.Joystick(0).get_numbuttons():
#     NumButtonIlist.append(iiii)
#     NumButtonIlist[iiii] = bpy.context.object.my_custom_props.add()
    
#     print(f"\n\n\n HERE HERE THE TOWN CRIER SAYS HEY WE CREATED This manyy proporites {bpy.context.object.my_custom_props.count()} \n\n\n HERE HERE")
#     iiii+=1


#print(os.environ["SDL_HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS"])


class CloseWindowOperator(bpy.types.Operator):
    isRunning = True
    pygame.init() 
    bl_idname = "wm.hello_world"
    bl_label = "WindowCloser Operator"
    size = (600, 600)
    
    
    
    
    
    window= pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
    background_colour = (234, 212, 252) 
    window.fill(background_colour)
    def set_TrueFalse(self, value):
        self["testprop"] = value
        
    def initWindow(window):
        
            i=0
            CurrentWindowSize = window.get_size()
            numButtons = pygame.joystick.Joystick(0).get_numbuttons()
            marginScreen = CurrentWindowSize[0]/8
            PercentScreen = (CurrentWindowSize[0]-(marginScreen*2))
            YinterceptScreen = (CurrentWindowSize[0]-(marginScreen*3))
            pygame.draw.circle(window, (255, 255, 0), [525, 350], 10, 3)
            while i < numButtons:
                i+=1
                
                xlocal = ((PercentScreen/(numButtons-1)) *i)+ YinterceptScreen/(numButtons-1)
                #pygame.draw.circle(window, (255, 0, 0), [xlocal, 300], 10, 3)
  
            #print(CurrentWindowSize)
            pygame.display.update()
    initWindow(window)
    pygame.display.update()

    def execute(self, context):
        if CloseWindowOperator.isRunning:
            #bpy.context.object.my_settings.add()
            print("Closing Window")
            #pygame.display.quit()
            #pygame.QUIT
            #pygame.init()
            window= pygame.display.set_mode((800, 600), flags=pygame.HIDDEN)
            CloseWindowOperator.isRunning = False
            #bpy.app.timers.unregister(every_2_seconds)
            
             
        else:
            print("Reopening Window")
            #pygame.init()
            
            CloseWindowOperator.isRunning = True
            #pygame.display.init()
            window = pygame.display.set_mode((800, 600), flags=pygame.SHOWN)
            background_colour = (234, 212, 252) 
            # Fill the scree with white color
            window.fill(background_colour)
            pygame.display.update()
            CloseWindowOperator.initWindow(window)
            #bpy.app.timers.register(every_2_seconds)
        return {'FINISHED'}
    
    def stageSetting(window, buttonsPressed, TrueFalse):
            i=0
            #pygame.display.init()
            CurrentWindowSize = CloseWindowOperator.size
            numButtons = pygame.joystick.Joystick(0).get_numbuttons()
            marginScreen = CurrentWindowSize[0]/8
            PercentScreen = (CurrentWindowSize[0]-(marginScreen*2))
            YinterceptScreen = (CurrentWindowSize[0]-(marginScreen*3))
            window.fill(CloseWindowOperator.background_colour)
            pygame.draw.circle(window, (255, 255, 0), [525, 350], 10, 3)
            
            while i < numButtons:
                i+=1
                xlocal = ((PercentScreen/(numButtons-1)) *i)+ YinterceptScreen/(numButtons-1)
                pygame.draw.circle(window, (255, 0, 0), [xlocal, 300], 10, 3)
            for button in buttonsPressed:
                xlocal = ((PercentScreen/(numButtons-1)) *(button+1))+ YinterceptScreen/(numButtons-1)
                pygame.draw.circle(window, (255, 0, 0), [xlocal, 300], 10, 0)
                #print(TrueFalse)
                bpy.context.scene.my_custom_props[button].TrueFalse =TrueFalse
            #print(CurrentWindowSize)
            pygame.display.update()
def is_negativeDzone(a,b):
    print(f" A: {a},    B:{b}")
    if ( a > b):
        return a
    else:
        return b
def is_positive(num):
    return num > 0
def is_negative(num):
    return num < 0

def drawAxis( NewValue,  whichAxis):
    
    #pygame.display.init()
    bpy.context.scene.my_axis[whichAxis].OneToNegOne = NewValue
        
    #pygame.joystick.SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS =1
def every_2_seconds():
    #print(pygame.event.get())
    #print(joysticks[0].get_instance_id())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CloseWindowOperator.isRunning = False
            pygame.QUIT
            break
        if event.type == pygame.KEYDOWN:
           
            # if keydown event happened
            # than printing a string to output
            print("A key has been pressed")
        if event.type == pygame.JOYAXISMOTION:
            #print("JOY AXIS MOTION")
            try:
                drawAxis(joysticks[0].get_axis(event.axis) ,event.axis)
            except:
                print("error Initalizing")
           
           
        
        if event.type == pygame.JOYBUTTONUP:
            i=0
            buttonsPressed = []
            #print(event.button, "AAAAAAAAAAAAAAAAAAAAAAa YOY OYOYOYOY")
            #if event.button == 0:
                #print("HUHHHHHH AYO")
           # print(f"ButtonPressed {str( joysticks[0].g;;;;et_numbuttons())}")
            buttonsPressed.append(event.button)
        
            CloseWindowOperator.stageSetting(CloseWindowOperator.window, buttonsPressed, False)
        if event.type == pygame.JOYBUTTONDOWN:
            i=0
            buttonsPressed = []
            print(event.button, "AAAAAAAAAAAAAAAAAAAAAAa YOY OYOYOYOY")
            
           # print(f"ButtonPressed {str( joysticks[0].get_numbuttons())}")
            
                    #print(f"Button {i} Pressed")
                    
                    
                    #print(bpy.context.object.my_custom_props[i].TrueFalse)
            buttonsPressed.append(event.button)
                    #print(buttonsPressed.count)
                    
                
        
            CloseWindowOperator.stageSetting(CloseWindowOperator.window, buttonsPressed, True)
        
            
    
    return 0.05


bpy.app.timers.register(every_2_seconds)
    