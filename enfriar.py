
import pyautogui as pt
import os
import time

timpo = 1

busqueda = {
    "play":"controll/play.png"
}

def mover(move,click = False):
    time.sleep(2)
    position = pt.locateCenterOnScreen(move)
    print(position)
    pt.moveTo(position) 
    if click == True:
        pt.click(button="left")
    pass

mover(busqueda["play"])