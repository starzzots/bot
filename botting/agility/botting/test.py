from win32gui import FindWindow, GetWindowRect
import win32gui
import pyautogui as pg
from stuff import *


hwnd = win32gui.FindWindow(None, 'RuneLite')
window_rect = win32gui.GetWindowRect(hwnd)

#pg.moveTo(window_rect[0]+2,window_rect[1]+2)

Randomize((window_rect[0]+5,window_rect[0]+5,window_rect[1]+5,window_rect[1]+5)).dragmove(7,7)