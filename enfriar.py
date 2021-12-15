
import pyautogui as pt
import os
import time

tiempo_trabajo = 1
tiempo_dormir = 1
salir = True

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
    
    position = pt.locateCenterOnScreen(move)
    print(position)
    pt.moveTo(position) 
    if click == True:
        pt.click(button="left")
    time.sleep(1)
    pass


def reanudar():
    time.sleep(2)
    mover(busqueda["play"],True)
    mover(busqueda["opciones_inicio"])
    mover_abajo = pt.Point(0,10)
    pt.moveRel(mover_abajo)
    pt.click(button="left")
    mover(busqueda["opciones_cancelar"])
    mover(busqueda["aceptar"],True)
    pass

def detener():
    time.sleep(2)
    mover(busqueda["pausa"])
    mover(busqueda["pausa_causa"],True)
    mover(busqueda["detener"],True)
    pass

reanudar()
time.sleep(2)
detener()
