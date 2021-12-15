
import pyautogui as pt
import os
import time

timpo = 1

busqueda = {
    "play":"controll/play.png",
    "reanudar":"controll/reanudar.png",
    "pausa":"controll/pausa.png",
    "pausa_causa":"controll/pausa_causa.png",
    "opciones_inicio":"controll/opciones_inicio.png",
    "opciones_cancelar":"controll/opciones_cancelar.png",
    "detener":"controll/detener.png",
    "aceptar":"controll/aceptar.png"
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