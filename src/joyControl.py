import pygame
import time
def joystickControl(mjoy): 
    x= True
    while x:
        e = pygame.event.wait()
        if (e.type== pygame.JOYAXISMOTION):
	  print "axis"
          ma0 = mjoy.get_axis(0)
          ma1 = mjoy.get_axis(1)
          if (ma1 < 0):
            return "Up"
          elif (ma1 > 0):
            return "Down"
          elif (ma0 < 0):
            return "Left"
          elif (ma0 > 0):
            return "Right"
        if (e.type== pygame.JOYBUTTONDOWN):
          mb0=mjoy.get_button(0)
          mb2=mjoy.get_button(2)
          if (mb0):
            return "button0"
          if (mb2):
            return "button2"
#pygame.joystick.init()
#pygame.display.init()
#if pygame.joystick.get_count():
#  mjoy = pygame.joystick.Joystick(0)
#  mjoy.init()
#  print mjoy.get_numaxes()
#  a = joystickControl()
#  print a
#  mjoy.quit()


#pygame.joystick.quit()

