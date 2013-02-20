import sys
import os
import pygame
import time

#only tested with Dual Shock based USB gamepads
def joystickControl(mjoy): 
    x = True
    while x:
        e = pygame.event.wait()
        if (e.type == pygame.JOYAXISMOTION):
	  print "axis"
          #  horizontal axis
	  sys.stdout = os.devnull
	  sys.stderr = os.devnull
          ma0 = mjoy.get_axis(0)
	  #  vertical axis
          ma1 = mjoy.get_axis(1)
	  sys.stdout = sys.__stdout__
	  sys.stderr = sys.__stderr__
          if (ma1 < 0):
            return "Up"
          elif (ma1 > 0):
            return "Down"
          elif (ma0 < 0):
            return "Left"
          elif (ma0 > 0):
            return "Right"
        if (e.type == pygame.JOYBUTTONDOWN):
	  sys.stdout = os.devnull
	  sys.stderr = os.devnull
          mb0 = mjoy.get_button(0)
          mb2 = mjoy.get_button(2)
	  sys.stdout = sys.__stdout__
	  sys.stderr = sys.__stderr__
          if (mb0):
            return "button0"
          if (mb2):
            return "button2"
